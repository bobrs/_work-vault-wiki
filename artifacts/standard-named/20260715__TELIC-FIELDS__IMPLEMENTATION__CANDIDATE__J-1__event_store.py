from __future__ import annotations

import json
import sqlite3
import time
from pathlib import Path
from typing import Any

from .canonical import canonical_json, sha256_text, utc_now


class EventConflictError(RuntimeError):
    pass


class ConcurrentAppendError(RuntimeError):
    pass


class StaleObjectError(RuntimeError):
    pass


class EventStore:
    """SQLite append-only event store with serialized chain appends and optimistic object revisions."""

    def __init__(self, db_path: Path, *, timeout: float = 10.0):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self.db_path, timeout=timeout, check_same_thread=False, isolation_level=None)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA foreign_keys=ON")
        self._conn.execute("PRAGMA busy_timeout=10000")
        self._create_schema()

    def close(self) -> None:
        self._conn.close()

    def _create_schema(self) -> None:
        self._conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS events (
                seq INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id TEXT NOT NULL UNIQUE,
                event_type TEXT NOT NULL,
                subject TEXT NOT NULL,
                actor TEXT NOT NULL,
                valid_time TEXT NOT NULL,
                recorded_time TEXT NOT NULL,
                event_json TEXT NOT NULL,
                prev_hash TEXT NOT NULL,
                event_hash TEXT NOT NULL UNIQUE
            );

            CREATE TABLE IF NOT EXISTS objects (
                object_id TEXT PRIMARY KEY,
                family TEXT NOT NULL,
                status TEXT NOT NULL,
                revision INTEGER NOT NULL DEFAULT 1,
                object_json TEXT NOT NULL,
                object_hash TEXT NOT NULL,
                last_event_id TEXT,
                updated_at TEXT NOT NULL,
                FOREIGN KEY(last_event_id) REFERENCES events(event_id)
            );

            CREATE TABLE IF NOT EXISTS edges (
                origin_id TEXT NOT NULL,
                descendant_id TEXT NOT NULL,
                relation TEXT NOT NULL,
                status TEXT NOT NULL,
                PRIMARY KEY(origin_id, descendant_id, relation)
            );

            CREATE TABLE IF NOT EXISTS meta (
                key TEXT PRIMARY KEY,
                value_json TEXT NOT NULL
            );
            """
        )

    def append_event(self, event: dict[str, Any], *, expected_prev_hash: str | None = None, retries: int = 4) -> dict[str, Any]:
        required = {"event_id", "event_type", "subject", "actor", "valid_time", "recorded_time"}
        missing = sorted(required - set(event))
        if missing:
            raise ValueError(f"Event missing fields: {missing}")
        event_json = canonical_json(event)
        for attempt in range(retries):
            try:
                self._conn.execute("BEGIN IMMEDIATE")
                existing = self._conn.execute(
                    "SELECT seq, event_json, prev_hash, event_hash FROM events WHERE event_id = ?",
                    (event["event_id"],),
                ).fetchone()
                if existing:
                    if existing["event_json"] != event_json:
                        self._conn.execute("ROLLBACK")
                        raise EventConflictError(f"Event id reused with different content: {event['event_id']}")
                    self._conn.execute("COMMIT")
                    return {
                        "seq": existing["seq"],
                        "event": event,
                        "prev_hash": existing["prev_hash"],
                        "event_hash": existing["event_hash"],
                        "idempotent_replay": True,
                    }
                previous = self._conn.execute("SELECT event_hash FROM events ORDER BY seq DESC LIMIT 1").fetchone()
                prev_hash = previous["event_hash"] if previous else "0" * 64
                if expected_prev_hash is not None and expected_prev_hash != prev_hash:
                    self._conn.execute("ROLLBACK")
                    raise ConcurrentAppendError("Event-chain head changed before append")
                event_hash = sha256_text(prev_hash + "\n" + event_json)
                cursor = self._conn.execute(
                    """
                    INSERT INTO events (
                        event_id, event_type, subject, actor, valid_time, recorded_time,
                        event_json, prev_hash, event_hash
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        event["event_id"], event["event_type"], event["subject"], event["actor"],
                        event["valid_time"], event["recorded_time"], event_json, prev_hash, event_hash,
                    ),
                )
                self._conn.execute("COMMIT")
                return {
                    "seq": cursor.lastrowid,
                    "event": event,
                    "prev_hash": prev_hash,
                    "event_hash": event_hash,
                    "idempotent_replay": False,
                }
            except sqlite3.OperationalError as exc:
                try:
                    self._conn.execute("ROLLBACK")
                except sqlite3.OperationalError:
                    pass
                if "locked" not in str(exc).lower() or attempt + 1 >= retries:
                    raise
                time.sleep(0.02 * (attempt + 1))
        raise ConcurrentAppendError("Could not serialize event append")

    def chain_head(self) -> str:
        row = self._conn.execute("SELECT event_hash FROM events ORDER BY seq DESC LIMIT 1").fetchone()
        return row["event_hash"] if row else "0" * 64

    def upsert_object(
        self,
        family: str,
        record: dict[str, Any],
        last_event_id: str | None = None,
        *,
        expected_revision: int | None = None,
    ) -> int:
        object_id = (record.get("id") or record.get("event_id") or record.get("context_id") or record.get("profile_id") or record.get("report_id") or record.get("transaction_id") or record.get("policy_id") or record.get("signature_id"))
        if not object_id:
            raise ValueError("Object record requires id or event_id")
        status = str(record.get("status", "unknown"))
        payload = canonical_json(record)
        object_hash = sha256_text(payload)
        self._conn.execute("BEGIN IMMEDIATE")
        try:
            existing = self._conn.execute(
                "SELECT revision FROM objects WHERE object_id = ?", (object_id,)
            ).fetchone()
            if existing:
                current_revision = int(existing["revision"])
                if expected_revision is not None and current_revision != expected_revision:
                    raise StaleObjectError(
                        f"Object {object_id} revision {current_revision} does not match expected {expected_revision}"
                    )
                new_revision = current_revision + 1
                self._conn.execute(
                    """
                    UPDATE objects SET family=?, status=?, revision=?, object_json=?, object_hash=?,
                    last_event_id=?, updated_at=? WHERE object_id=?
                    """,
                    (family, status, new_revision, payload, object_hash, last_event_id, utc_now(), object_id),
                )
            else:
                if expected_revision not in (None, 0):
                    raise StaleObjectError(f"Object {object_id} does not exist")
                new_revision = 1
                self._conn.execute(
                    """
                    INSERT INTO objects(object_id, family, status, revision, object_json, object_hash, last_event_id, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (object_id, family, status, new_revision, payload, object_hash, last_event_id, utc_now()),
                )
            self._conn.execute("COMMIT")
            return new_revision
        except Exception:
            self._conn.execute("ROLLBACK")
            raise

    def get_object(self, object_id: str) -> dict[str, Any] | None:
        row = self._conn.execute(
            "SELECT family, object_json, object_hash, revision, last_event_id FROM objects WHERE object_id = ?",
            (object_id,),
        ).fetchone()
        if not row:
            return None
        return {
            "family": row["family"],
            "record": json.loads(row["object_json"]),
            "object_hash": row["object_hash"],
            "revision": row["revision"],
            "last_event_id": row["last_event_id"],
        }

    def list_objects(self, family: str | None = None) -> list[dict[str, Any]]:
        if family:
            rows = self._conn.execute(
                "SELECT object_id, family, object_json, object_hash, revision, last_event_id FROM objects WHERE family=? ORDER BY object_id",
                (family,),
            ).fetchall()
        else:
            rows = self._conn.execute(
                "SELECT object_id, family, object_json, object_hash, revision, last_event_id FROM objects ORDER BY family, object_id"
            ).fetchall()
        return [
            {
                "object_id": row["object_id"],
                "family": row["family"],
                "record": json.loads(row["object_json"]),
                "object_hash": row["object_hash"],
                "revision": row["revision"],
                "last_event_id": row["last_event_id"],
            }
            for row in rows
        ]

    def add_edge(self, origin_id: str, descendant_id: str, relation: str = "derives_from", status: str = "active") -> None:
        with self._conn:
            self._conn.execute(
                """
                INSERT INTO edges(origin_id, descendant_id, relation, status) VALUES (?, ?, ?, ?)
                ON CONFLICT(origin_id, descendant_id, relation) DO UPDATE SET status=excluded.status
                """,
                (origin_id, descendant_id, relation, status),
            )

    def descendants(self, origin_id: str, *, recursive: bool = True) -> list[dict[str, str]]:
        if not recursive:
            rows = self._conn.execute(
                "SELECT origin_id, descendant_id, relation, status FROM edges WHERE origin_id=? ORDER BY descendant_id",
                (origin_id,),
            ).fetchall()
            return [dict(row) for row in rows]
        rows = self._conn.execute(
            """
            WITH RECURSIVE walk(origin_id, descendant_id, relation, status) AS (
                SELECT origin_id, descendant_id, relation, status FROM edges WHERE origin_id=?
                UNION
                SELECT e.origin_id, e.descendant_id, e.relation, e.status
                FROM edges e JOIN walk w ON e.origin_id = w.descendant_id
            )
            SELECT DISTINCT origin_id, descendant_id, relation, status FROM walk ORDER BY descendant_id
            """,
            (origin_id,),
        ).fetchall()
        return [dict(row) for row in rows]

    def get_event(self, event_id: str) -> dict[str, Any] | None:
        row = self._conn.execute(
            "SELECT seq, event_json, prev_hash, event_hash FROM events WHERE event_id=?", (event_id,)
        ).fetchone()
        if not row:
            return None
        return {
            "seq": row["seq"],
            "event": json.loads(row["event_json"]),
            "prev_hash": row["prev_hash"],
            "event_hash": row["event_hash"],
        }

    def list_events(self) -> list[dict[str, Any]]:
        rows = self._conn.execute(
            "SELECT seq, event_json, prev_hash, event_hash FROM events ORDER BY seq"
        ).fetchall()
        return [
            {
                "seq": row["seq"],
                "event": json.loads(row["event_json"]),
                "prev_hash": row["prev_hash"],
                "event_hash": row["event_hash"],
            }
            for row in rows
        ]

    def verify_chain(self) -> tuple[bool, list[str]]:
        errors: list[str] = []
        expected_prev = "0" * 64
        for item in self.list_events():
            if item["prev_hash"] != expected_prev:
                errors.append(f"seq {item['seq']}: prev_hash mismatch")
            expected_hash = sha256_text(item["prev_hash"] + "\n" + canonical_json(item["event"]))
            if item["event_hash"] != expected_hash:
                errors.append(f"seq {item['seq']}: event_hash mismatch")
            expected_prev = item["event_hash"]
        return (not errors, errors)

    def set_meta(self, key: str, value: Any) -> None:
        with self._conn:
            self._conn.execute(
                """
                INSERT INTO meta(key, value_json) VALUES (?, ?)
                ON CONFLICT(key) DO UPDATE SET value_json=excluded.value_json
                """,
                (key, canonical_json(value)),
            )

    def get_meta(self, key: str, default: Any = None) -> Any:
        row = self._conn.execute("SELECT value_json FROM meta WHERE key=?", (key,)).fetchone()
        return json.loads(row["value_json"]) if row else default

    def all_meta(self) -> dict[str, Any]:
        rows = self._conn.execute("SELECT key, value_json FROM meta ORDER BY key").fetchall()
        return {row["key"]: json.loads(row["value_json"]) for row in rows}

    def snapshot_database(self, target: Path) -> None:
        target = Path(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        backup = sqlite3.connect(target)
        try:
            self._conn.backup(backup)
        finally:
            backup.close()

    def clear(self) -> None:
        with self._conn:
            self._conn.execute("DELETE FROM edges")
            self._conn.execute("DELETE FROM objects")
            self._conn.execute("DELETE FROM events")
            self._conn.execute("DELETE FROM meta")

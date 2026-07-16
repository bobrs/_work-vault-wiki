from __future__ import annotations

import json
import shutil
import sqlite3
from pathlib import Path
from typing import Any, Iterable

from .canonical import canonical_json, sha256_text, utc_now


class EventConflictError(RuntimeError):
    pass


class EventStore:
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self.db_path)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA foreign_keys=ON")
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
                object_json TEXT NOT NULL,
                last_event_id TEXT,
                updated_at TEXT NOT NULL,
                FOREIGN KEY(last_event_id) REFERENCES events(event_id)
            );

            CREATE TABLE IF NOT EXISTS meta (
                key TEXT PRIMARY KEY,
                value_json TEXT NOT NULL
            );
            """
        )
        self._conn.commit()

    def append_event(self, event: dict[str, Any]) -> dict[str, Any]:
        required = {"event_id", "event_type", "subject", "actor", "valid_time", "recorded_time"}
        missing = sorted(required - set(event))
        if missing:
            raise ValueError(f"Event missing fields: {missing}")

        event_json = canonical_json(event)
        existing = self._conn.execute(
            "SELECT seq, event_json, prev_hash, event_hash FROM events WHERE event_id = ?",
            (event["event_id"],),
        ).fetchone()
        if existing:
            if existing["event_json"] != event_json:
                raise EventConflictError(f"Event id reused with different content: {event['event_id']}")
            return {
                "seq": existing["seq"],
                "event": event,
                "prev_hash": existing["prev_hash"],
                "event_hash": existing["event_hash"],
                "idempotent_replay": True,
            }

        previous = self._conn.execute("SELECT event_hash FROM events ORDER BY seq DESC LIMIT 1").fetchone()
        prev_hash = previous["event_hash"] if previous else "0" * 64
        event_hash = sha256_text(prev_hash + "\n" + event_json)
        with self._conn:
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
        return {
            "seq": cursor.lastrowid,
            "event": event,
            "prev_hash": prev_hash,
            "event_hash": event_hash,
            "idempotent_replay": False,
        }

    def upsert_object(self, family: str, record: dict[str, Any], last_event_id: str | None = None) -> None:
        object_id = record.get("id") or record.get("event_id")
        if not object_id:
            raise ValueError("Object record requires id or event_id")
        status = str(record.get("status", "unknown"))
        payload = canonical_json(record)
        with self._conn:
            self._conn.execute(
                """
                INSERT INTO objects(object_id, family, status, object_json, last_event_id, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(object_id) DO UPDATE SET
                    family=excluded.family,
                    status=excluded.status,
                    object_json=excluded.object_json,
                    last_event_id=excluded.last_event_id,
                    updated_at=excluded.updated_at
                """,
                (object_id, family, status, payload, last_event_id, utc_now()),
            )

    def get_object(self, object_id: str) -> dict[str, Any] | None:
        row = self._conn.execute(
            "SELECT family, object_json, last_event_id FROM objects WHERE object_id = ?",
            (object_id,),
        ).fetchone()
        if not row:
            return None
        return {
            "family": row["family"],
            "record": json.loads(row["object_json"]),
            "last_event_id": row["last_event_id"],
        }

    def list_objects(self, family: str | None = None) -> list[dict[str, Any]]:
        if family:
            rows = self._conn.execute(
                "SELECT object_id, family, object_json, last_event_id FROM objects WHERE family = ? ORDER BY object_id",
                (family,),
            ).fetchall()
        else:
            rows = self._conn.execute(
                "SELECT object_id, family, object_json, last_event_id FROM objects ORDER BY family, object_id"
            ).fetchall()
        return [
            {
                "object_id": row["object_id"],
                "family": row["family"],
                "record": json.loads(row["object_json"]),
                "last_event_id": row["last_event_id"],
            }
            for row in rows
        ]


    def get_event(self, event_id: str) -> dict[str, Any] | None:
        row = self._conn.execute(
            "SELECT seq, event_json, prev_hash, event_hash FROM events WHERE event_id = ?",
            (event_id,),
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
        row = self._conn.execute("SELECT value_json FROM meta WHERE key = ?", (key,)).fetchone()
        return json.loads(row["value_json"]) if row else default

    def all_meta(self) -> dict[str, Any]:
        rows = self._conn.execute("SELECT key, value_json FROM meta ORDER BY key").fetchall()
        return {row["key"]: json.loads(row["value_json"]) for row in rows}

    def snapshot_database(self, target: Path) -> None:
        target = Path(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        self._conn.commit()
        backup = sqlite3.connect(target)
        try:
            self._conn.backup(backup)
        finally:
            backup.close()

    def clear(self) -> None:
        with self._conn:
            self._conn.execute("DELETE FROM objects")
            self._conn.execute("DELETE FROM events")
            self._conn.execute("DELETE FROM meta")

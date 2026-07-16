from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any, Callable

from .canonical import canonical_json, utc_now


class SimulatedNetworkTimeout(TimeoutError):
    pass


class DurableDeliveryQueue:
    """Durable local queue with explicit fault injection and idempotent effects."""

    def __init__(self, path: Path):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS messages(
                message_id TEXT PRIMARY KEY,
                dedupe_key TEXT NOT NULL,
                sequence_no INTEGER NOT NULL,
                payload_json TEXT NOT NULL,
                status TEXT NOT NULL,
                attempts INTEGER NOT NULL DEFAULT 0,
                last_error TEXT,
                created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS effects(
                dedupe_key TEXT PRIMARY KEY,
                result_json TEXT NOT NULL,
                applied_at TEXT NOT NULL
            );
            """
        )

    def enqueue(self, *, message_id: str, dedupe_key: str, sequence_no: int, payload: dict[str, Any]) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT OR IGNORE INTO messages(message_id,dedupe_key,sequence_no,payload_json,status,created_at) VALUES(?,?,?,?,?,?)",
                (message_id, dedupe_key, sequence_no, canonical_json(payload), "pending", utc_now()),
            )

    def _effect(self, dedupe_key: str) -> dict[str, Any] | None:
        row = self.conn.execute("SELECT result_json FROM effects WHERE dedupe_key=?", (dedupe_key,)).fetchone()
        return json.loads(row["result_json"]) if row else None

    def process_one(
        self,
        handler: Callable[[dict[str, Any]], dict[str, Any]],
        *,
        fault: str | None = None,
        reverse_order: bool = False,
    ) -> dict[str, Any] | None:
        order = "DESC" if reverse_order else "ASC"
        row = self.conn.execute(
            f"SELECT * FROM messages WHERE status IN ('pending','retry') ORDER BY sequence_no {order}, message_id LIMIT 1"
        ).fetchone()
        if not row:
            return None
        message = dict(row)
        payload = json.loads(message["payload_json"])
        with self.conn:
            self.conn.execute(
                "UPDATE messages SET attempts=attempts+1,status='delivering',last_error=NULL WHERE message_id=?",
                (message["message_id"],),
            )
        prior = self._effect(message["dedupe_key"])
        if prior is not None:
            with self.conn:
                self.conn.execute("UPDATE messages SET status='delivered' WHERE message_id=?", (message["message_id"],))
            return {"message_id":message["message_id"],"deduplicated":True,"result":prior}
        result = handler(payload)
        with self.conn:
            self.conn.execute(
                "INSERT OR IGNORE INTO effects(dedupe_key,result_json,applied_at) VALUES(?,?,?)",
                (message["dedupe_key"], canonical_json(result), utc_now()),
            )
        if fault == "timeout_after_apply":
            with self.conn:
                self.conn.execute(
                    "UPDATE messages SET status='retry',last_error='simulated timeout after apply' WHERE message_id=?",
                    (message["message_id"],),
                )
            raise SimulatedNetworkTimeout("simulated timeout after effect application")
        with self.conn:
            self.conn.execute("UPDATE messages SET status='delivered' WHERE message_id=?", (message["message_id"],))
        return {"message_id":message["message_id"],"deduplicated":False,"result":result}

    def process_duplicate(self, handler: Callable[[dict[str, Any]], dict[str, Any]]) -> list[dict[str, Any]]:
        first = self.process_one(handler)
        if first is None:
            return []
        row = self.conn.execute("SELECT * FROM messages WHERE message_id=?", (first["message_id"],)).fetchone()
        payload = json.loads(row["payload_json"])
        prior = self._effect(row["dedupe_key"])
        return [first, {"message_id":row["message_id"],"deduplicated":True,"result":prior,"duplicate_delivery":True,"payload":payload}]

    def status(self) -> list[dict[str, Any]]:
        rows = self.conn.execute("SELECT message_id,dedupe_key,sequence_no,status,attempts,last_error FROM messages ORDER BY sequence_no,message_id").fetchall()
        return [dict(row) for row in rows]

    def effect_count(self) -> int:
        return int(self.conn.execute("SELECT COUNT(*) AS n FROM effects").fetchone()["n"])

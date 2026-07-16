from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


class SchemaTests(unittest.TestCase):
    def test_all_twelve_schemas_are_valid(self) -> None:
        paths = sorted((ROOT/"schemas").glob("*.json"))
        self.assertEqual(len(paths), 12)
        for path in paths:
            Draft202012Validator.check_schema(json.loads(path.read_text(encoding="utf-8")))

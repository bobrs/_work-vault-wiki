from __future__ import annotations

import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from telic_j2.scenario import ReferencePilot

ROOT = Path(__file__).resolve().parents[1]


class DisclosurePrivacyTests(unittest.TestCase):
    def test_public_view_redacts_direct_source_and_consent(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            export = Path(name)/"witness.zip"
            pilot = ReferencePilot(Path(name)/"run", ROOT/"schemas")
            pilot.run_full(export)
            with zipfile.ZipFile(export) as archive:
                public = json.loads(archive.read("views/public-view.json"))
                participant = json.loads(archive.read("views/participant-view.json"))
            public_text = json.dumps(public)
            participant_text = json.dumps(participant)
            self.assertNotIn("daytime transit is inaccessible", public_text)
            self.assertNotIn('"training_reuse": false', public_text.lower())
            self.assertIn("omitted_commitments", public)
            self.assertIn("accessible transit", participant_text)

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

from telic_j1.scenario import ReferencePilot
from telic_j1.witness import verify_export

ROOT = Path(__file__).resolve().parents[1]


class ReferenceHardeningTests(unittest.TestCase):
    def test_full_scenario_and_signed_selective_export(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            export = Path(name)/"witness.zip"
            pilot = ReferencePilot(Path(name)/"run", ROOT/"schemas")
            result = pilot.run_full(export)
            self.assertTrue(all(result["witness"]["proofs"].values()))
            verified = verify_export(export)
            self.assertTrue(verified["valid"], verified["errors"])
            self.assertTrue(verified["manifest_signature_valid"])
            self.assertEqual(verified["views_verified"], 4)
            self.assertGreaterEqual(verified["records_validated"], 40)

    def test_standalone_verifier_has_no_package_dependency(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            export = Path(name)/"witness.zip"
            pilot = ReferencePilot(Path(name)/"run", ROOT/"schemas")
            pilot.run_full(export)
            env = dict(os.environ)
            env["PYTHONPATH"] = ""
            proc = subprocess.run(
                [sys.executable, str(ROOT/"verifier"/"verify_witness.py"), str(export)],
                cwd=name, env=env, capture_output=True, text=True, check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            result = json.loads(proc.stdout)
            self.assertTrue(result["valid"])
            self.assertEqual(result["verifier"], "standalone-no-telic-j1-import")

    def test_partial_failure_compensates_before_retry(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            pilot = ReferencePilot(Path(name), ROOT/"schemas")
            result = pilot.execute_with_partial_failure_and_rotation()
            self.assertEqual(result["partial"]["status"], "compensated")
            self.assertTrue(result["partial"]["compensation"]["reservation_released"])
            self.assertTrue(result["old_key_rejected"])
            self.assertEqual(result["transaction"]["status"], "complete")
    def test_tampered_manifest_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            export = Path(name)/"witness.zip"
            tampered = Path(name)/"tampered.zip"
            pilot = ReferencePilot(Path(name)/"run", ROOT/"schemas")
            pilot.run_full(export)
            extract = Path(name)/"extract"
            with zipfile.ZipFile(export) as archive:
                archive.extractall(extract)
            manifest_path = extract/"manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["scope"] = "tampered scope"
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
            with zipfile.ZipFile(tampered, "w", zipfile.ZIP_DEFLATED) as archive:
                for path in sorted(extract.rglob("*")):
                    if path.is_file():
                        archive.write(path, path.relative_to(extract).as_posix())
            result = verify_export(tampered)
            self.assertFalse(result["valid"])
            self.assertTrue(any("manifest" in error.lower() or "checksum" in error.lower() or "signature" in error.lower() for error in result["errors"]))

    def test_restart_restores_policy_key_status_and_retirement(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            workdir = Path(name)/"run"
            export = Path(name)/"witness.zip"
            first = ReferencePilot(workdir, ROOT/"schemas")
            first.run_full(export)
            first.store.close()
            second = ReferencePilot(workdir, ROOT/"schemas")
            status = second.status()
            self.assertEqual(status["active_policy"]["version"], 2)
            self.assertFalse(status["tool_credential_active"])
            self.assertEqual(status["gate_keys"]["gate-k3"], "active")
            self.assertEqual(status["gate_keys"]["gate-k2"], "revoked")


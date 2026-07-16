#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT / "src"))

from telic_j2.release import build_release_candidate
from telic_j2.threshold import ThresholdCustody
from telic_j2.trial import ReleaseCandidateTrial


def copy_release_inputs(staging: Path, witness: Path) -> None:
    staging.mkdir(parents=True, exist_ok=True)
    directories = ["src", "schemas", "verifier", "scripts", "examples"]
    for name in directories:
        src = PACKAGE_ROOT / name
        if src.exists():
            shutil.copytree(src, staging / name, dirs_exist_ok=True, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    files = [
        "README.md", "ARCHITECTURE.md", "CONFORMANCE-CLAIM.md", "MULTI-PARTY-TRIAL-REPORT.md",
        "AUTHENTICATION-AND-SPLIT-CUSTODY.md", "POLICY-MIGRATION-AND-ROLLBACK.md",
        "NETWORK-QUEUE-FAULT-INJECTION.md", "PRIVACY-REVIEW.md",
        "ACCESSIBILITY-ASSISTIVE-TECH-REVIEW.md", "RELEASE-CANDIDATE-REPRODUCIBILITY.md",
        "EXTERNAL-REVIEW-READINESS.md", "DEMO-TRANSCRIPT.md", "SECURITY-AND-THREAT-MODEL.md",
        "requirements.txt", "pyproject.toml",
    ]
    for name in files:
        src = PACKAGE_ROOT / name
        if src.exists():
            shutil.copy2(src, staging / name)
    (staging / "exports").mkdir(exist_ok=True)
    shutil.copy2(witness, staging / "exports" / "tf-mvi-1-j2-witness.zip")


def main() -> int:
    demo_work = PACKAGE_ROOT / "demo" / "release-candidate-trial"
    witness = PACKAGE_ROOT / "exports" / "tf-mvi-1-j2-witness.zip"
    if demo_work.exists():
        shutil.rmtree(demo_work)
    trial = ReleaseCandidateTrial(demo_work, PACKAGE_ROOT / "schemas")
    trial_result = trial.run_full(witness)
    custody = trial.custody

    output = PACKAGE_ROOT / "exports" / "telic-fields-j2-rc1.zip"
    output_2 = PACKAGE_ROOT / "demo" / "telic-fields-j2-rc1-second-build.zip"
    with tempfile.TemporaryDirectory(prefix="telic-j2-stage-a-") as a_name, tempfile.TemporaryDirectory(prefix="telic-j2-stage-b-") as b_name:
        stage_a = Path(a_name)
        stage_b = Path(b_name)
        copy_release_inputs(stage_a, witness)
        copy_release_inputs(stage_b, witness)
        result_a = build_release_candidate(
            staging_dir=stage_a,
            output_zip=output,
            custody=custody,
            approving_custodians=["custodian-operator", "custodian-verifier"],
        )
        result_b = build_release_candidate(
            staging_dir=stage_b,
            output_zip=output_2,
            custody=custody,
            approving_custodians=["custodian-operator", "custodian-verifier"],
        )
    result = {
        "trial": trial_result,
        "first_build": result_a,
        "second_build": result_b,
        "reproducible": result_a["archive_digest"] == result_b["archive_digest"],
        "private_key_material_in_release": False,
        "external_human_review_complete": False,
    }
    path = PACKAGE_ROOT / "demo" / "release-build-results.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["reproducible"] and result_a["threshold_result"]["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

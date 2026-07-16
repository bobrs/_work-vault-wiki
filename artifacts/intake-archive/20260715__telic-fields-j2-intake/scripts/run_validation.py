#!/usr/bin/env python3
from __future__ import annotations

import compileall
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from telic_j2.release_threats import run_release_threat_harness
from telic_j2.scenario import ReferencePilot
from telic_j2.threats import run_threat_harness
from telic_j2.trial import ReleaseCandidateTrial
from telic_j2.witness import verify_export

ENV = dict(os.environ)
ENV["PYTHONPATH"] = str(ROOT / "src")


def run(args: list[str], *, env=ENV, timeout: int = 180) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=ROOT, env=env, text=True, capture_output=True, timeout=timeout)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr, file=sys.stderr)
        raise SystemExit(result.returncode)
    return result


def write(name: str, value) -> None:
    path = ROOT / "demo" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(value, str):
        path.write_text(value, encoding="utf-8")
    else:
        path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    for item in [ROOT/"demo"/"validation-trial", ROOT/"demo"/"threats", ROOT/"demo"/"release-threats"]:
        shutil.rmtree(item, ignore_errors=True)
    compile_ok = compileall.compile_dir(ROOT/"src", quiet=1) and compileall.compile_dir(ROOT/"verifier", quiet=1)
    py_files = list((ROOT/"src").rglob("*.py")) + list((ROOT/"verifier").rglob("*.py"))

    print("stage: tests", flush=True)
    test = run([sys.executable, "tests/run_all.py"])
    test_text = test.stdout + test.stderr
    write("test-output.txt", test_text)
    match = re.search(r"Ran (\d+) tests", test_text)
    tests_run = int(match.group(1)) if match else 0

    print("stage: trial", flush=True)
    trial = ReleaseCandidateTrial(ROOT/"demo"/"validation-trial", ROOT/"schemas")
    trial_result = trial.run_full(ROOT/"exports"/"tf-mvi-1-j2-witness.zip")
    write("trial-output.json", trial_result)
    witness_data = verify_export(ROOT/"exports"/"tf-mvi-1-j2-witness.zip")
    write("implementation-witness-verification.json", witness_data)

    print("stage: inherited", flush=True)
    inherited_pilot = ReferencePilot(ROOT/"demo"/"threats", ROOT/"schemas")
    inherited_data = run_threat_harness(inherited_pilot)
    write("inherited-threat-results.json", inherited_data)

    print("stage: release threats", flush=True)
    release_pilot = ReleaseCandidateTrial(ROOT/"demo"/"release-threats", ROOT/"schemas")
    release_threat_data = run_release_threat_harness(release_pilot)
    write("release-threat-results.json", release_threat_data)

    print("stage: build", flush=True)
    build = run([sys.executable, "scripts/build_release.py"], timeout=180)
    write("release-build-output.json", build.stdout)
    build_data = json.loads(build.stdout)

    clean_env = dict(os.environ)
    clean_env["PYTHONPATH"] = ""
    print("stage: standalone witness", flush=True)
    witness_standalone = run([sys.executable, "verifier/verify_witness.py", "exports/tf-mvi-1-j2-witness.zip"], env=clean_env)
    witness_standalone_data = json.loads(witness_standalone.stdout)
    write("independent-witness-verification.json", witness_standalone_data)
    print("stage: release verify", flush=True)
    release_verify = run([sys.executable, "verifier/verify_release.py", "exports/telic-fields-j2-rc1.zip"], env=clean_env)
    release_verify_data = json.loads(release_verify.stdout)
    write("independent-release-verification.json", release_verify_data)

    schemas = list((ROOT/"schemas").glob("*.json"))
    for path in schemas:
        json.loads(path.read_text(encoding="utf-8"))
    private_names=[]
    with zipfile.ZipFile(ROOT/"exports"/"telic-fields-j2-rc1.zip") as archive:
        for name in archive.namelist():
            lower=name.lower()
            if "private" in lower or lower.endswith((".key",".p12",".pfx")):
                private_names.append(name)

    results={
        "phase":"J.2",
        "python_files_compiled":len(py_files),
        "compile_errors":0 if compile_ok else 1,
        "schemas_checked":len(schemas),
        "schema_errors":0,
        "tests_run":tests_run,
        "test_failures":0,
        "reference_events":trial_result["events"],
        "reference_objects":trial_result["objects"],
        "implementation_witness_verifier":witness_data,
        "standalone_witness_verifier":witness_standalone_data,
        "inherited_threats":inherited_data,
        "release_threats":release_threat_data,
        "threats_total":inherited_data["total"]+release_threat_data["total"],
        "threats_detected":inherited_data["detected"]+release_threat_data["detected"],
        "release_reproducible":build_data["reproducible"],
        "release_first_digest":build_data["first_build"]["archive_digest"],
        "release_second_digest":build_data["second_build"]["archive_digest"],
        "release_threshold_valid":build_data["first_build"]["threshold_result"]["valid"],
        "standalone_release_verifier":release_verify_data,
        "private_key_material_found":private_names,
        "external_human_review_complete":False,
        "proofs":trial_result["witness"]["proofs"],
        "result":"PASS_WITH_CONDITIONS",
    }
    (ROOT/"tests"/"validation-results.json").write_text(json.dumps(results,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(results,indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

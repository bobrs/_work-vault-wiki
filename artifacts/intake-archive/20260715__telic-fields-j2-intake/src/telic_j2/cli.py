from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from .scenario import ReferencePilot
from .threats import run_threat_harness
from .release_threats import run_release_threat_harness
from .trial import ReleaseCandidateTrial
from .webapp import serve
from .witness import verify_export


def package_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main() -> int:
    parser = argparse.ArgumentParser(prog="telic-j2", description="Telic Fields J.2 multi-party trial and release candidate")
    sub = parser.add_subparsers(dest="command", required=True)

    demo = sub.add_parser("demo", help="Run the inherited J.1 hardened demonstration")
    demo.add_argument("--workdir", type=Path, default=package_root()/"demo"/"j1-compatible")
    demo.add_argument("--export", type=Path, default=package_root()/"exports"/"tf-mvi-1-j2-compatible-witness.zip")

    trial = sub.add_parser("trial", help="Run the J.2 authenticated multi-party trial")
    trial.add_argument("--workdir", type=Path, default=package_root()/"demo"/"release-candidate-trial")
    trial.add_argument("--export", type=Path, default=package_root()/"exports"/"tf-mvi-1-j2-witness.zip")

    verify = sub.add_parser("verify", help="Verify a J.2 witness")
    verify.add_argument("export", type=Path)

    verify_release = sub.add_parser("verify-release", help="Run the standalone release verifier")
    verify_release.add_argument("release", type=Path)

    build_release = sub.add_parser("build-release", help="Build the reproducible threshold-approved RC1 archive")

    inspect = sub.add_parser("inspect")
    inspect.add_argument("--workdir", type=Path, default=package_root()/"demo"/"release-candidate-trial")

    threats = sub.add_parser("threats")
    threats.add_argument("--workdir", type=Path, default=package_root()/"demo"/"threats")

    release_threats = sub.add_parser("release-threats")
    release_threats.add_argument("--workdir", type=Path, default=package_root()/"demo"/"release-threats")

    server = sub.add_parser("serve")
    server.add_argument("--workdir", type=Path, default=package_root()/"demo"/"web")
    server.add_argument("--host", default="127.0.0.1")
    server.add_argument("--port", type=int, default=8767)

    args = parser.parse_args()
    schemas = package_root()/"schemas"

    if args.command == "demo":
        pilot = ReferencePilot(args.workdir, schemas)
        print(json.dumps(pilot.run_full(args.export), indent=2, default=str))
        return 0
    if args.command == "trial":
        pilot = ReleaseCandidateTrial(args.workdir, schemas)
        print(json.dumps(pilot.run_full(args.export), indent=2, default=str))
        return 0
    if args.command == "verify":
        result = verify_export(args.export)
        print(json.dumps(result, indent=2))
        return 0 if result["valid"] else 1
    if args.command == "verify-release":
        script = package_root()/"verifier"/"verify_release.py"
        return subprocess.call([sys.executable, str(script), str(args.release)])
    if args.command == "build-release":
        script = package_root()/"scripts"/"build_release.py"
        return subprocess.call([sys.executable, str(script)])
    if args.command == "inspect":
        pilot = ReleaseCandidateTrial(args.workdir, schemas)
        print(json.dumps({"status":pilot.status(),"events":pilot.store.list_events(),"objects":pilot.store.list_objects()}, indent=2, default=str))
        return 0
    if args.command == "threats":
        pilot = ReferencePilot(args.workdir, schemas)
        result = run_threat_harness(pilot)
        print(json.dumps(result, indent=2))
        return 0 if result["pass"] else 1
    if args.command == "release-threats":
        pilot = ReleaseCandidateTrial(args.workdir, schemas)
        result = run_release_threat_harness(pilot)
        print(json.dumps(result, indent=2))
        return 0 if result["pass"] else 1
    if args.command == "serve":
        serve(args.workdir, schemas, args.host, args.port)
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

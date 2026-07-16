from __future__ import annotations

import argparse
import json
from pathlib import Path

from .scenario import ReferencePilot
from .webapp import serve
from .witness import verify_export
from .threats import run_threat_harness


def package_root() -> Path:
    return Path(__file__).resolve().parents[2]


def main() -> int:
    parser = argparse.ArgumentParser(prog="telic-j0", description="Telic Fields J.0 reference implementation")
    sub = parser.add_subparsers(dest="command", required=True)

    demo = sub.add_parser("demo", help="Run the full deterministic reference scenario")
    demo.add_argument("--workdir", type=Path, default=package_root() / "demo" / "run")
    demo.add_argument("--export", type=Path, default=package_root() / "exports" / "tf-mvi-1-witness.zip")

    verify = sub.add_parser("verify", help="Verify an independent witness export")
    verify.add_argument("export", type=Path)

    inspect = sub.add_parser("inspect", help="Inspect a demo database")
    inspect.add_argument("--workdir", type=Path, default=package_root() / "demo" / "run")

    threats = sub.add_parser("threats", help="Run the consolidated adversarial threat harness")
    threats.add_argument("--workdir", type=Path, default=package_root() / "demo" / "threats")

    server = sub.add_parser("serve", help="Run the local-first pilot web interface")
    server.add_argument("--workdir", type=Path, default=package_root() / "demo" / "web")
    server.add_argument("--host", default="127.0.0.1")
    server.add_argument("--port", type=int, default=8765)

    args = parser.parse_args()
    schemas = package_root() / "schemas"

    if args.command == "demo":
        pilot = ReferencePilot(args.workdir, schemas)
        result = pilot.run_full(args.export)
        print(json.dumps(result, indent=2, default=str))
        return 0
    if args.command == "verify":
        result = verify_export(args.export)
        print(json.dumps(result, indent=2))
        return 0 if result["valid"] else 1
    if args.command == "inspect":
        pilot = ReferencePilot(args.workdir, schemas)
        print(json.dumps({"status": pilot.status(), "events": pilot.store.list_events(), "objects": pilot.store.list_objects()}, indent=2))
        return 0
    if args.command == "threats":
        pilot = ReferencePilot(args.workdir, schemas)
        result = run_threat_harness(pilot)
        print(json.dumps(result, indent=2))
        return 0 if result["pass"] else 1
    if args.command == "serve":
        serve(args.workdir, schemas, args.host, args.port)
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

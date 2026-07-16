#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PYTHONPATH= python "$ROOT/verifier/verify_release.py" "${1:-$ROOT/exports/telic-fields-j2-rc1.zip}"

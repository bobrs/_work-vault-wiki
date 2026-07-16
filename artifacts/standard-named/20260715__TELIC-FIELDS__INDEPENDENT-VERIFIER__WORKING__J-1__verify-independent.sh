#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
PYTHONPATH= python "$ROOT/verifier/verify_witness.py" "${1:-$ROOT/exports/tf-mvi-1-j1-witness.zip}"

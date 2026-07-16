#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
export PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}"
rm -rf "$ROOT/demo/run"
python -m telic_j1 demo --workdir "$ROOT/demo/run" --export "$ROOT/exports/tf-mvi-1-j1-witness.zip"

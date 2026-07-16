#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
export PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}"
rm -rf "$ROOT/demo/release-candidate-trial"
python -m telic_j2 trial --workdir "$ROOT/demo/release-candidate-trial" --export "$ROOT/exports/tf-mvi-1-j2-witness.zip"

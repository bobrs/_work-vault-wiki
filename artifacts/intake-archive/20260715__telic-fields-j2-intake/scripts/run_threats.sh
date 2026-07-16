#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "$0")/.." && pwd)
export PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}"
rm -rf "$ROOT/demo/threats" "$ROOT/demo/release-threats"
python -m telic_j2 threats --workdir "$ROOT/demo/threats"
python -m telic_j2 release-threats --workdir "$ROOT/demo/release-threats"

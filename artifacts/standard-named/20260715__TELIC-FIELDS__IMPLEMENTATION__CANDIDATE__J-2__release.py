from __future__ import annotations

import hashlib
import json
import os
import zipfile
from pathlib import Path
from typing import Any

from .canonical import canonical_json, sha256_bytes, utc_now
from .ids import urn
from .threshold import ThresholdCustody


FIXED_ZIP_TIME = (2020, 1, 1, 0, 0, 0)


def file_digest(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def deterministic_zip(output: Path, root: Path, files: list[Path]) -> str:
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(files, key=lambda p: p.relative_to(root).as_posix()):
            rel = path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(rel, FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    return file_digest(output)


def build_release_candidate(
    *,
    staging_dir: Path,
    output_zip: Path,
    custody: ThresholdCustody,
    approving_custodians: list[str],
    source_date_epoch: int = 1784160000,
) -> dict[str, Any]:
    staging_dir = Path(staging_dir)
    output_zip = Path(output_zip)
    records = []
    for path in sorted(p for p in staging_dir.rglob("*") if p.is_file() and p.name not in {"release-manifest.json", "release-approvals.json"}):
        records.append({
            "path": path.relative_to(staging_dir).as_posix(),
            "sha256": file_digest(path),
            "size": path.stat().st_size,
        })
    manifest = {
        "release_id": urn("release", "telic-fields-j2-rc1"),
        "release_name": "Telic Fields J.2 Release Candidate 1",
        "version": "0.1.0-rc1",
        "source_date_epoch": source_date_epoch,
        "files": records,
        "private_key_material_included": False,
        "production_claim": False,
        "external_human_review_complete": False,
        "created_at": "2026-07-15T00:00:00Z",
    }
    manifest_path = staging_dir / "release-manifest.json"
    manifest_path.write_text(canonical_json(manifest) + "\n", encoding="utf-8")
    digest = file_digest(manifest_path)
    approvals = [
        custody.approve(custodian_id=custodian, release_id=manifest["release_id"], manifest_digest=digest, approved_at="2026-07-15T00:00:00Z")
        for custodian in approving_custodians
    ]
    approval_record = {
        "release_id": manifest["release_id"],
        "manifest_digest": digest,
        "threshold": custody.threshold,
        "approvals": approvals,
        "public_custody": custody.public_bundle(),
    }
    (staging_dir / "release-approvals.json").write_text(canonical_json(approval_record) + "\n", encoding="utf-8")
    files = [p for p in staging_dir.rglob("*") if p.is_file()]
    archive_digest = deterministic_zip(output_zip, staging_dir, files)
    return {
        "release_id": manifest["release_id"],
        "manifest_digest": digest,
        "archive_digest": archive_digest,
        "approvals": approvals,
        "threshold_result": custody.verify_threshold(approvals, release_id=manifest["release_id"], manifest_digest=digest),
        "output": str(output_zip),
    }

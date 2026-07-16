from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from telic_j2.release import build_release_candidate
from telic_j2.threshold import ThresholdCustody


class ReleaseReproducibilityTests(unittest.TestCase):
    def test_two_builds_match_and_threshold_passes(self):
        with tempfile.TemporaryDirectory() as name:
            root=Path(name)
            custody=ThresholdCustody(root/"keys",{"a":"operator","b":"privacy","c":"verifier"},threshold=2)
            digests=[]
            for n in [1,2]:
                stage=root/f"stage{n}"
                stage.mkdir()
                (stage/"README.md").write_text("same source\n",encoding="utf-8")
                result=build_release_candidate(staging_dir=stage,output_zip=root/f"r{n}.zip",custody=custody,approving_custodians=["a","c"])
                self.assertTrue(result["threshold_result"]["valid"])
                digests.append(result["archive_digest"])
            self.assertEqual(digests[0],digests[1])


if __name__ == "__main__":
    unittest.main()

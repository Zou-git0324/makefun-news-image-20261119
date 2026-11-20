"""Entry point for the make.fun news-image-20261119 bounty.

The image itself is bundled in this repository as ``entry.png``: a
one-page infographic summing up the world news of Thursday
19 November 2026. This program only copies that file, byte for byte,
to the output directory, so the two grading runs produce identical
output. Standard library only, no network.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        raise FileNotFoundError(f"bundled image missing: {src}")
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)  # byte-for-byte copy: both runs identical
    print(f"wrote {dst} ({dst.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

"""docs/RUNTIME.md shows the mini model verbatim: whole files and contiguous excerpts."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BLOCK = re.compile(r"<!-- (file|excerpt): (\S+) -->\n```python\n(.*?)```\n", re.DOTALL)


def test_doc_blocks_match_mini_model():
    doc = (ROOT / "docs" / "RUNTIME.md").read_text()
    blocks = BLOCK.findall(doc)
    assert len(blocks) >= 7
    for kind, path, code in blocks:
        source = (ROOT / path).read_text()
        if kind == "file":
            assert code == source, f"docs/RUNTIME.md block differs from {path}"
        else:
            assert code.rstrip("\n") in source, f"docs/RUNTIME.md excerpt not found in {path}"

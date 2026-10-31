"""Regenerate ``src/cim_python_sdk/model/**`` and ``src/cim_python_sdk/_registry.py``.

uv run python tools/regen.py          # generate into a temp dir, format, swap in
uv run python tools/regen.py --check  # exit 1 and list differing files if out of date
"""

from __future__ import annotations

import argparse
import filecmp
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from codegen.generate import generate
from codegen.normalize import load_model, normalize

PKG = ROOT / "src" / "cim_python_sdk"
OUTPUTS = ("model", "_registry.py")


def build(outdir: Path) -> None:
    """Generate into `outdir` (laid out like src/cim_python_sdk) and run ruff format on it.

    The input is the CIM100 IR snapshot merged with the CGMES European extensions
    (codegen/snapshot/eu_ir.json), see `codegen.normalize.load_model`."""
    model = load_model()
    generate(normalize(model), model, outdir)
    cmd = [sys.executable, "-m", "ruff", "format", "--config", str(ROOT / "pyproject.toml"), "-q"]
    subprocess.run([*cmd, str(outdir)], check=True)


def _files(base: Path) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for name in OUTPUTS:
        p = base / name
        if p.is_file():
            out[name] = p
        elif p.is_dir():
            for f in p.rglob("*"):
                if f.is_file() and "__pycache__" not in f.parts and f.suffix != ".pyc":
                    out[str(f.relative_to(base))] = f
    return out


def diff(new: Path, old: Path) -> list[str]:
    a, b = _files(new), _files(old)
    lines = [f"missing: {k}" for k in sorted(a.keys() - b.keys())]
    lines += [f"stale: {k}" for k in sorted(b.keys() - a.keys())]
    lines += [
        f"differs: {k}"
        for k in sorted(a.keys() & b.keys())
        if not filecmp.cmp(a[k], b[k], shallow=False)
    ]
    return lines


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="do not write; exit 1 if out of date")
    args = ap.parse_args()
    (ROOT / "build").mkdir(exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="regen-", dir=ROOT / "build"))
    try:
        build(tmp)
        if args.check:
            lines = diff(tmp, PKG)
            if lines:
                print(f"generated output is out of date ({len(lines)} files):")
                print("\n".join(lines[:200]))
                if len(lines) > 200:
                    print(f"... and {len(lines) - 200} more")
                return 1
            print("generated output is up to date")
            return 0
        for name in OUTPUTS:
            dest = PKG / name
            old = PKG / (name + ".old")
            if dest.exists():
                dest.rename(old)
            (tmp / name).rename(dest)
            if old.is_dir():
                shutil.rmtree(old)
            elif old.exists():
                old.unlink()
        print(f"regenerated {len(_files(PKG))} files")
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())

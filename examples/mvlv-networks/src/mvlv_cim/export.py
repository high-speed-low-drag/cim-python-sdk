"""Writing the built networks as CIMXML and JSON-LD."""

from __future__ import annotations

import datetime as dt
import os
import re
import warnings
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from cim_python_sdk.serialization import write_cimxml, write_jsonld

from mvlv_cim.builder import BuiltNetwork, build_network

#: Team-Nando/MV-LV-Networks checkout: $MVLV_DATA, else ./MV-LV-Networks (relative to cwd).
DEFAULT_SOURCE = Path(os.environ.get("MVLV_DATA", "MV-LV-Networks"))
SOURCE_URL = "https://github.com/Team-Nando/MV-LV-Networks"
LICENCE = "BSD-3-Clause"
AUTHORITY_SET = "urn:x-mvlv-cim:authority:ausnet-mv-lv-networks"
FORMATS = {"cimxml": ".xml", "jsonld": ".jsonld"}
_WORKBOOK = re.compile(r"Network_(\d+)_.*\.xlsx$")


@dataclass(frozen=True)
class Workbook:
    number: int
    path: Path

    @property
    def stem(self) -> str:
        return self.path.stem


def find_workbooks(source: Path, numbers: Iterable[int] | None = None) -> list[Workbook]:
    """The ``Network_<n>_*.xlsx`` files of ``source``, optionally only those in ``numbers``."""
    found = []
    for p in sorted(Path(source).glob("Network_*.xlsx")):
        m = _WORKBOOK.match(p.name)
        if m:
            found.append(Workbook(int(m.group(1)), p))
    found.sort(key=lambda w: w.number)
    if numbers is not None:
        wanted = set(numbers)
        missing = wanted - {w.number for w in found}
        if missing:
            raise ValueError(f"no workbook for network(s) {sorted(missing)} in {source}")
        found = [w for w in found if w.number in wanted]
    return found


def created_from_mtime(path: Path) -> str:
    """UTC time of the source file's mtime, to the second (deterministic per source file)."""
    t = dt.datetime.fromtimestamp(path.stat().st_mtime, dt.UTC).replace(microsecond=0)
    return t.strftime("%Y-%m-%dT%H:%M:%SZ")


def make_header(wb: Workbook, net: BuiltNetwork, created: str | None = None) -> dict[str, Any]:
    return {
        "created": created or created_from_mtime(wb.path),
        "version": "1",
        "modelingAuthoritySet": AUTHORITY_SET,
        "description": [
            f"CIM100 model of {wb.stem} (feeder {net.feeder.name}); "
            "MV network with LV equivalents (EquivalentInjection per distribution transformer)",
            f"Source data: {SOURCE_URL} (workbook {wb.path.name}), licence {LICENCE}, "
            "(c) 2024 Team Nando",
        ],
    }


def out_path(out: Path, wb: Workbook, fmt: str) -> Path:
    return Path(out) / (wb.stem + FORMATS[fmt])


def write_files(net: BuiltNetwork, header: dict[str, Any], paths: dict[str, Path]) -> list[str]:
    """Write ``net`` in each requested format; returns the warnings the writers raised."""
    msgs: list[str] = []
    for fmt, path in paths.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        writer = write_cimxml if fmt == "cimxml" else write_jsonld
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            writer(net.objects, path, header=header)
        msgs.extend(f"{fmt}: {w.message}" for w in caught)
    return msgs


def export_network(
    wb: Workbook, out: Path, formats: Iterable[str], created: str | None = None
) -> dict[str, Path]:
    net = build_network(wb.path)
    paths = {f: out_path(out, wb, f) for f in formats}
    write_files(net, make_header(wb, net, created), paths)
    return paths

"""Shared fixtures: the four workbooks, each built once per test session."""

from __future__ import annotations

import os
import time
from pathlib import Path

import pytest

from mvlv_cim.builder import BuiltNetwork, build_network

DATA_DIR = Path(os.environ.get("MVLV_DATA", Path(__file__).resolve().parents[1] / "MV-LV-Networks"))
NETWORKS = (
    "Network_1_Rural_SMR8",
    "Network_2_Rural_KLO14",
    "Network_3_Urban_HPK11",
    "Network_4_Urban_CRE21",
)

#: Filled by the tests, printed at the end of the run.
REPORT: dict[str, dict[str, object]] = {}
_CACHE: dict[str, BuiltNetwork] = {}


def network_path(name: str) -> Path:
    path = DATA_DIR / f"{name}.xlsx"
    if not path.exists():
        pytest.skip(f"{path} not found (set MVLV_DATA to the MV-LV-Networks checkout)")
    return path


@pytest.fixture(scope="session", params=NETWORKS)
def built(request: pytest.FixtureRequest) -> BuiltNetwork:
    name = request.param
    if name not in _CACHE:
        t0 = time.perf_counter()
        _CACHE[name] = build_network(network_path(name))
        REPORT.setdefault(name, {})["build_s"] = time.perf_counter() - t0
    return _CACHE[name]


def pytest_terminal_summary(terminalreporter: pytest.TerminalReporter) -> None:
    if not REPORT:
        return
    tr = terminalreporter
    tr.section("S3 network builds")
    tr.write_line(
        f"{'network':24} {'build s':>8} {'peak MiB':>9} {'objects':>8}  issues / validate"
    )
    for name in NETWORKS:
        r = REPORT.get(name)
        if not r:
            continue
        peak = r.get("peak_mib")
        tr.write_line(
            f"{name:24} {r.get('build_s', float('nan')):8.2f} "
            f"{peak if peak is None else format(peak, '9.1f'):>9} {r.get('objects', ''):>8}  "
            f"{r.get('issues', '')} / {r.get('validate', '')}"
        )
        if r.get("islands"):
            tr.write_line(f"    islands: {r['islands']}")

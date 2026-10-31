"""Micro-benchmark of the association runtime on the hand-written mini model.

Usage: uv run python tools/bench_runtime.py [N]
"""

from __future__ import annotations

import sys
import time
import tracemalloc
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tests.runtime.minimodel.asset import Asset
from tests.runtime.minimodel.conducting_equipment import ConductingEquipment
from tests.runtime.minimodel.power_system_resource import PowerSystemResource
from tests.runtime.minimodel.terminal import Terminal


def timed(label: str, n: int, fn) -> object:
    t = time.perf_counter()
    r = fn()
    dt = time.perf_counter() - t
    print(f"{label:<48} {dt * 1000:8.1f} ms  {dt / n * 1e6:6.2f} us/op")
    return r


def main(n: int = 100_000) -> None:
    ces = timed(f"create {n} ConductingEquipment", n, lambda: [ConductingEquipment() for _ in range(n)])
    ts = timed(f"create {n} Terminal", n, lambda: [Terminal(mrid=str(i)) for i in range(n)])
    timed(f"link {n} Terminal.conducting_equipment", n, lambda: [
        setattr(t, "conducting_equipment", ces[i // 2]) for i, t in enumerate(ts)
    ])
    timed(f"relink {n} (replace target, N:1)", n, lambda: [
        setattr(t, "conducting_equipment", ces[-1 - i // 2]) for i, t in enumerate(ts)
    ])
    timed(f"read {n} ce.terminals", n, lambda: [c.terminals for c in ces])
    timed(f"{n} Terminal(conducting_equipment=ce) kwargs", n, lambda: [
        Terminal(conducting_equipment=ces[i % 1000]) for i in range(n)
    ])
    assets = [Asset() for _ in range(n // 10)]
    psrs = [PowerSystemResource() for _ in range(n // 10)]
    timed(f"{n} N:M add_power_system_resource", n, lambda: [
        assets[i % len(assets)].add_power_system_resource(psrs[(i * 7) % len(psrs)])
        for i in range(n)
    ])
    timed(f"clear {len(ces)} ce.terminals", len(ces), lambda: [c.clear_terminals() for c in ces])
    timed(f"validate {n} Terminal", n, lambda: [t.validate() for t in ts])

    tracemalloc.start()
    objs = [Terminal(mrid="x") for _ in range(10_000)]
    size, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"memory per unlinked Terminal (mrid shared): {size / len(objs):.0f} B")
    tracemalloc.start()
    objs2 = [ConductingEquipment(mrid="x") for _ in range(10_000)]
    size, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"memory per unlinked ConductingEquipment:    {size / len(objs2):.0f} B")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 100_000)

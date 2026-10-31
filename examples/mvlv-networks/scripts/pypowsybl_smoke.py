"""Load a CGMES file set written by ``mvlv-cim export --format cgmes`` into pypowsybl.

pypowsybl is not a dependency of this project. Run it in a throwaway environment:

    uv run mvlv-cim export -n 3 --format cgmes --zip --out out
    uv run --no-project --with pypowsybl python scripts/pypowsybl_smoke.py \
        out/Network_3_Urban_HPK11_CGMES.zip

It prints element counts and runs an AC load flow. The export has no load and no dispatch values
(see docs/EXPORT_REPORT.md) and its infeed has min/max Q = 0, which the load flow reads as "cannot
control voltage". So that a slack bus exists, this script (not the export) gives the infeed a
voltage setpoint of the source's nominal voltage and wide reactive limits. With zero load the
result only shows that the topology, impedances and units are consistent: voltages near 1.0 pu.
"""

from __future__ import annotations

import sys

import pandas as pd
import pypowsybl as pp
import pypowsybl.loadflow as lf


def main(path: str) -> int:
    n = pp.network.load(path)
    counts = {
        "substations": len(n.get_substations()),
        "voltage levels": len(n.get_voltage_levels()),
        "buses": len(n.get_buses()),
        "lines": len(n.get_lines()),
        "2-winding transformers": len(n.get_2_windings_transformers()),
        "loads": len(n.get_loads()),
        "generators": len(n.get_generators()),
        "shunt compensators": len(n.get_shunt_compensators()),
        "ratio tap changers": len(n.get_ratio_tap_changers()),
        "operational limits": len(n.get_operational_limits()),
    }
    print("loaded:", ", ".join(f"{v} {k}" for k, v in counts.items()))
    vls = n.get_voltage_levels()
    gens = n.get_generators().join(vls[["nominal_v"]], on="voltage_level_id")
    source = gens[gens.nominal_v == gens.nominal_v.max()]
    if len(source) != 1:
        print(f"expected one infeed at the highest voltage level, found {len(source)}")
        return 1
    sid, kv = source.index[0], float(source.nominal_v.iloc[0])
    n.update_generators(id=sid, target_v=kv, target_p=0.0)
    n.update_generators(id=sid, voltage_regulator_on=True)
    n.create_minmax_reactive_limits(
        pd.DataFrame(index=[sid], data={"min_q": [-1e6], "max_q": [1e6]})
    )
    res = lf.run_ac(n)
    for r in res:
        print(f"AC load flow: {r.status.name} ({r.status_text}), {r.iteration_count} iteration(s)")
    buses = n.get_buses().join(vls[["nominal_v"]], on="voltage_level_id")
    buses["pu"] = buses.v_mag / buses.nominal_v
    print(buses.groupby("nominal_v").pu.describe()[["count", "min", "mean", "max"]].to_string())
    return 0 if all(r.status.name == "CONVERGED" for r in res) else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))

"""A small network that is valid against CGMES 3.0 EQ (and TP when `topology=True`)."""

from __future__ import annotations

import cim_python_sdk as c


def build_eq(lines: int = 1, *, topology: bool = False) -> dict[str, object]:
    bv = c.BaseVoltage(mrid="bv", name="22kV", nominal_voltage=22000.0)
    region = c.GeographicalRegion(mrid="gr", name="Region")
    sub_region = c.SubGeographicalRegion(mrid="sgr", name="Sub region", region=region)
    sub = c.Substation(mrid="sub", name="Sub", region=sub_region)
    vl = c.VoltageLevel(mrid="vl", name="VL", substation=sub, base_voltage=bv)
    out: dict[str, object] = {"bv": bv, "sub": sub, "vl": vl}
    nodes = []
    for i in range(lines + 1):
        cn = c.ConnectivityNode(mrid=f"cn{i}", name=f"CN{i}", connectivity_node_container=vl)
        nodes.append(cn)
    tns = []
    if topology:
        for i, cn in enumerate(nodes):
            tn = c.TopologicalNode(
                mrid=f"tn{i}", name=f"TN{i}", base_voltage=bv, connectivity_node_container=vl
            )
            cn.topological_node = tn
            tns.append(tn)
    for i in range(lines):
        line = c.ACLineSegment(
            mrid=f"line{i}", name=f"Line{i}", r=1.0, x=2.0, bch=1e-6, gch=0.0, length=3.0,
            base_voltage=bv, equipment_container=vl,
        )  # fmt: skip
        for seq in (1, 2):
            t = c.Terminal(
                mrid=f"line{i}-t{seq}", name=f"T{seq}", sequence_number=seq,
                conducting_equipment=line, connectivity_node=nodes[i + seq - 1],
            )  # fmt: skip
            if topology:
                t.topological_node = tns[i + seq - 1]
        out[f"line{i}"] = line
    return out

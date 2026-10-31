"""A small bus-branch network with CGMES 3.0 EQ, SSH, TP and SV content.

Voltage-controlled generator -- line -- load between two nodes, with a current limit
(``eu:LimitKind``), an ``eu:IdentifiedObject.shortName``, solved voltages and flows. `validate_profile` against
EQ+SSH+TP+SV is clean. mRIDs are fixed UUIDs (uuid5 of a short name), as CGMES expects.
"""

from __future__ import annotations

import uuid

import cim_python_sdk as c


def uid(name: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"cim100-test:{name}"))


def build_cgmes() -> dict[str, c.CimObject]:
    bv = c.BaseVoltage(mrid=uid("bv"), name="110kV", nominal_voltage=110e3)
    gr = c.GeographicalRegion(mrid=uid("gr"), name="Region")
    sgr = c.SubGeographicalRegion(mrid=uid("sgr"), name="Sub region", region=gr)
    sub = c.Substation(mrid=uid("sub"), name="Sub", region=sgr)
    vl = c.VoltageLevel(mrid=uid("vl"), name="VL", substation=sub, base_voltage=bv)
    cns, tns = [], []
    for i in range(2):
        tn = c.TopologicalNode(
            mrid=uid(f"tn{i}"), name=f"TN{i}", base_voltage=bv, connectivity_node_container=vl
        )
        cn = c.ConnectivityNode(
            mrid=uid(f"cn{i}"), name=f"CN{i}", connectivity_node_container=vl, topological_node=tn
        )
        cns.append(cn)
        tns.append(tn)

    def terminal(eq: c.ConductingEquipment, seq: int, i: int) -> c.Terminal:
        return c.Terminal(
            mrid=uid(f"{eq.name}-t{seq}"), name=f"{eq.name} T{seq}", sequence_number=seq,
            phases=c.PhaseCode.ABC, conducting_equipment=eq, connectivity_node=cns[i],
            topological_node=tns[i], connected=True,
        )  # fmt: skip

    line = c.ACLineSegment(
        mrid=uid("line"), name="Line", short_name="L1", r=1.0, x=10.0, bch=1e-5, gch=0.0,
        length=10e3, base_voltage=bv, equipment_container=vl, in_service=True,
    )  # fmt: skip
    lt1, lt2 = terminal(line, 1, 0), terminal(line, 2, 1)
    gu = c.ThermalGeneratingUnit(
        mrid=uid("gu"), name="GU", max_operating_p=200e6, min_operating_p=0.0, normal_pf=1.0,
        in_service=True, equipment_container=sub,
    )  # fmt: skip
    gen = c.SynchronousMachine(
        mrid=uid("gen"), name="Gen", type=c.SynchronousMachineKind.generator, rated_s=250e6,
        rated_u=110e3, max_q=100e6, min_q=-100e6, generating_unit=gu, equipment_container=vl,
        in_service=True, control_enabled=True, p=-50e6, q=-10e6,
        operating_mode=c.SynchronousMachineOperatingMode.generator, reference_priority=1,
    )  # fmt: skip
    gt = terminal(gen, 1, 0)
    rc = c.RegulatingControl(
        mrid=uid("rc"), name="RC", mode=c.RegulatingControlModeKind.voltage, terminal=gt,
        discrete=False, enabled=True, target_value=110.0,
        target_value_unit_multiplier=c.UnitMultiplier.k,
    )  # fmt: skip
    gen.regulating_control = rc
    load = c.EnergyConsumer(
        mrid=uid("load"), name="Load", equipment_container=vl, in_service=True, p=50e6, q=10e6
    )
    ldt = terminal(load, 1, 1)
    olt = c.OperationalLimitType(
        mrid=uid("olt"), name="PATL", kind=c.LimitKind.patl, is_infinite_duration=True,
        direction=c.OperationalLimitDirectionKind.absoluteValue,
    )  # fmt: skip
    ols = c.OperationalLimitSet(mrid=uid("ols"), name="Limits", terminal=lt1, equipment=line)
    lim = c.CurrentLimit(
        mrid=uid("lim"), name="PATL", normal_value=500.0, value=450.0, operational_limit_set=ols,
        operational_limit_type=olt,
    )  # fmt: skip
    island = c.TopologicalIsland(
        mrid=uid("island"), name="Island", topological_nodes=tns, angle_ref_topological_node=tns[0]
    )
    sv = [
        c.SvVoltage(v=110e3, angle=0.0, topological_node=tns[0]),
        c.SvVoltage(v=109.5e3, angle=-0.5, topological_node=tns[1]),
        c.SvPowerFlow(p=-50e6, q=-10e6, terminal=gt),
        c.SvPowerFlow(p=50e6, q=10e6, terminal=ldt),
        c.SvPowerFlow(p=50e6, q=10e6, terminal=lt1),
        c.SvPowerFlow(p=-50e6, q=-10e6, terminal=lt2),
    ]
    out: dict[str, c.CimObject] = {
        "bv": bv, "sub": sub, "vl": vl, "line": line, "lt1": lt1, "lt2": lt2, "gen": gen,
        "gu": gu, "rc": rc, "load": load, "olt": olt, "ols": ols, "lim": lim, "island": island,
        "tn0": tns[0], "tn1": tns[1], "cn0": cns[0], "cn1": cns[1],
    }  # fmt: skip
    for i, o in enumerate(sv):
        out[f"sv{i}"] = o
    return out

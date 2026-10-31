"""CIM enumeration FlowDirectionKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class FlowDirectionKind(CimEnum):
    """Kind of flow direction for reading/measured values proper to some commodities such as,
    for example, energy, power, demand."""

    none = "none"
    forward = "forward"
    lagging = "lagging"
    leading = "leading"
    net = "net"
    q1plusQ2 = "q1plusQ2"
    q1plusQ3 = "q1plusQ3"
    q1plusQ4 = "q1plusQ4"
    q1minusQ4 = "q1minusQ4"
    q2plusQ3 = "q2plusQ3"
    q2plusQ4 = "q2plusQ4"
    q2minusQ3 = "q2minusQ3"
    q3plusQ4 = "q3plusQ4"
    q3minusQ2 = "q3minusQ2"
    quadrant1 = "quadrant1"
    quadrant2 = "quadrant2"
    quadrant3 = "quadrant3"
    quadrant4 = "quadrant4"
    reverse = "reverse"
    total = "total"
    totalByPhase = "totalByPhase"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="FlowDirectionKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{CBEAA8A6-BD51-4960-B930-6A371FCDFA91}",
            kind="enumeration",
        )
    )

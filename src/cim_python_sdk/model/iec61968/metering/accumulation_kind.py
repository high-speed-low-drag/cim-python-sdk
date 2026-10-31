"""CIM enumeration AccumulationKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AccumulationKind(CimEnum):
    """Kind of accumulation behaviour for read / measured values from individual end points."""

    none = "none"
    bulkQuantity = "bulkQuantity"
    continuousCumulative = "continuousCumulative"
    cumulative = "cumulative"
    deltaData = "deltaData"
    indicating = "indicating"
    summation = "summation"
    timeDelay = "timeDelay"
    instantaneous = "instantaneous"
    latchingQuantity = "latchingQuantity"
    boundedQuantity = "boundedQuantity"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AccumulationKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{519F992F-632E-473a-BBC0-582B9734F927}",
            kind="enumeration",
        )
    )

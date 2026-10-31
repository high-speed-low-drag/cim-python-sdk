"""CIM enumeration AggregateKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AggregateKind(CimEnum):
    """Kind of aggregation for read / measured values from multiple end points."""

    none = "none"
    average = "average"
    excess = "excess"
    highThreshold = "highThreshold"
    lowThreshold = "lowThreshold"
    maximum = "maximum"
    minimum = "minimum"
    nominal = "nominal"
    normal = "normal"
    secondMaximum = "secondMaximum"
    secondMinimum = "secondMinimum"
    thirdMaximum = "thirdMaximum"
    fourthMaximum = "fourthMaximum"
    fifthMaximum = "fifthMaximum"
    sum = "sum"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AggregateKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{62D8C9AB-8C4C-4ecf-B14B-7548CF58CFA4}",
            kind="enumeration",
        )
    )

"""CIM enumeration CalculationIntervalUnitKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CalculationIntervalUnitKind(CimEnum):
    """Units in which calculation interval period is defined."""

    milliSecond = "milliSecond"
    perCycle = "perCycle"
    cycle = "cycle"
    second = "second"
    minute = "minute"
    day = "day"
    hour = "hour"
    week = "week"
    month = "month"
    year = "year"
    season = "season"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CalculationIntervalUnitKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{363640F5-D9CD-4faf-8391-6EC9DD3B2E17}",
            kind="enumeration",
        )
    )

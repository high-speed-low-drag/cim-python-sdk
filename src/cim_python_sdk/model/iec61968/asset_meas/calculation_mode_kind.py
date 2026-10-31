"""CIM enumeration CalculationModeKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CalculationModeKind(CimEnum):
    """The mode of the calculation (total, periodic, sliding).

    ."""

    total = "total"
    period = "period"
    sliding = "sliding"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CalculationModeKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{91395ECA-E9D9-4a79-8F11-4F9720C59655}",
            kind="enumeration",
        )
    )

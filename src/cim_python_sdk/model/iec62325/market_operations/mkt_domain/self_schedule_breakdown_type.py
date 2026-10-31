"""CIM enumeration SelfScheduleBreakdownType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SelfScheduleBreakdownType(CimEnum):
    """Self schedule breakdown type."""

    ETC = "ETC"
    TOR = "TOR"
    LPT = "LPT"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SelfScheduleBreakdownType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{1F46DF6C-CAA9-41cb-92BA-F92C1FF8F771}",
            kind="enumeration",
        )
    )

"""CIM enumeration CheckOutType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CheckOutType(CimEnum):
    """To indicate a check out type such as adjusted capacity or dispatch capacity."""

    PRE_HOUR = "PRE_HOUR"
    PRE_SCHEDULE = "PRE_SCHEDULE"
    AFTER_THE_FACT = "AFTER_THE_FACT"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CheckOutType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{22857E68-E659-4640-99B1-9776F7607D96}",
            kind="enumeration",
        )
    )

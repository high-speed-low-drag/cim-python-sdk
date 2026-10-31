"""CIM enumeration MarketType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MarketType(CimEnum):
    """Market type."""

    DAM = "DAM"
    RTM = "RTM"
    HAM = "HAM"
    RUC = "RUC"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MarketType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{9974A28A-9581-48c6-B7F9-B019B1E1DC80}",
            kind="enumeration",
        )
    )

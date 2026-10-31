"""CIM enumeration MarketProductSelfSchedType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MarketProductSelfSchedType(CimEnum):
    """Market product self schedule bid types."""

    ETC = "ETC"
    TOR = "TOR"
    RMR = "RMR"
    RGMR = "RGMR"
    RMT = "RMT"
    PT = "PT"
    LPT = "LPT"
    SP = "SP"
    RA = "RA"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MarketProductSelfSchedType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{502B95E5-B0D2-4eb0-B86F-9E1C5166CE2E}",
            kind="enumeration",
        )
    )

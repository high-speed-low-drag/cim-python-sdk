"""CIM enumeration TradeProductType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TradeProductType(CimEnum):
    """CIM enumeration TradeProductType."""

    PHY = "PHY"
    APN = "APN"
    RUT = "RUT"
    RDT = "RDT"
    SRT = "SRT"
    NRT = "NRT"
    CAP = "CAP"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TradeProductType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{CDAFD9DB-9506-4d0c-A42C-4F5159E63E23}",
            kind="enumeration",
        )
    )

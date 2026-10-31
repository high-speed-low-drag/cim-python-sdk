"""CIM enumeration CleanTradeProductType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CleanTradeProductType(CimEnum):
    """CIM enumeration CleanTradeProductType."""

    PHY = "PHY"
    APN = "APN"
    CPT = "CPT"
    RUT = "RUT"
    RDT = "RDT"
    SRT = "SRT"
    NRT = "NRT"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CleanTradeProductType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{948F8057-E20F-4cfb-A1B4-BA9212DCD1A7}",
            kind="enumeration",
        )
    )

"""CIM enumeration MarketProductType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MarketProductType(CimEnum):
    """For example:

    Energy, Reg Up, Reg Down, Spin Reserve, Nonspin Reserve, RUC, Load Folloing Up, and Load
    Following Down."""

    EN = "EN"
    RU = "RU"
    RD = "RD"
    SR = "SR"
    NR = "NR"
    RC = "RC"
    LFU = "LFU"
    LFD = "LFD"
    REG = "REG"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MarketProductType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{1920E8CD-6BD4-4056-B957-9776FC340CA1}",
            kind="enumeration",
        )
    )

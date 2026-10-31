"""CIM enumeration MarketProductTypeAsReq (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MarketProductTypeAsReq(CimEnum):
    """RU - Regulation Up

    RD - Regulation Down

    SR - Spin Reserve

    NR - Nonspin Reserve

    AS - Upward Ancillary Service"""

    RU = "RU"
    RD = "RD"
    SR = "SR"
    NR = "NR"
    AS = "AS"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MarketProductTypeAsReq",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{EB7283D5-CE00-42e9-83EC-8DE0B089271F}",
            kind="enumeration",
        )
    )

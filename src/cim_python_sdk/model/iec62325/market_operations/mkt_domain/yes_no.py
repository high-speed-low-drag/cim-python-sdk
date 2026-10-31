"""CIM enumeration YesNo (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class YesNo(CimEnum):
    """Used as a flag set to Yes or No."""

    YES = "YES"
    NO = "NO"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="YesNo",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{7D3890C4-A74E-4e42-9493-07D941668D9C}",
            kind="enumeration",
        )
    )

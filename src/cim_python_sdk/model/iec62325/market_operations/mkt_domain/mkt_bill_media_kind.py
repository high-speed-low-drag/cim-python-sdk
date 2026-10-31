"""CIM enumeration MktBillMediaKind (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MktBillMediaKind(CimEnum):
    """Kind of bill media."""

    paper = "paper"
    electronic = "electronic"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MktBillMediaKind",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{A247AC71-10FA-4d51-80E3-83B671EAD70C}",
            kind="enumeration",
        )
    )

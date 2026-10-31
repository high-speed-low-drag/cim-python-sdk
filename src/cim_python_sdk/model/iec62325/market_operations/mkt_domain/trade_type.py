"""CIM enumeration TradeType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TradeType(CimEnum):
    """Trade type."""

    IST = "IST"
    AST = "AST"
    UCT = "UCT"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TradeType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{FD67B160-B7BF-4b89-82C2-ACA6CCB6FE63}",
            kind="enumeration",
        )
    )

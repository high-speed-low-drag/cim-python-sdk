"""CIM enumeration MktAccountKind (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MktAccountKind(CimEnum):
    """Kind of Market account."""

    normal = "normal"
    reversal = "reversal"
    statistical = "statistical"
    estimate = "estimate"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MktAccountKind",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{3C1B1532-00FF-4d12-99CA-7A793AFCEE15}",
            kind="enumeration",
        )
    )

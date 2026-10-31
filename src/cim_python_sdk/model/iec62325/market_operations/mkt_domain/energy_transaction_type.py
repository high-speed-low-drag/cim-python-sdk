"""CIM enumeration EnergyTransactionType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EnergyTransactionType(CimEnum):
    """Defines the state of a transaction."""

    approve = "approve"
    deny = "deny"
    study = "study"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EnergyTransactionType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{3C2349F8-E1BD-4fe3-943C-28C8A18116D1}",
            kind="enumeration",
        )
    )

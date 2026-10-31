"""CIM enumeration ReserveRequirementType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ReserveRequirementType(CimEnum):
    """For example:

    Operating Reserve, Regulation, Contingency"""

    OPRSV = "OPRSV"
    CONT = "CONT"
    REG = "REG"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ReserveRequirementType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{649D7C9C-6861-4f39-B603-6CD796C5FCB2}",
            kind="enumeration",
        )
    )

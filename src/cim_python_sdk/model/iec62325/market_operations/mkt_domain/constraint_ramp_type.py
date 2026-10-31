"""CIM enumeration ConstraintRampType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ConstraintRampType(CimEnum):
    """Constraint Ramp type."""

    FAST = "FAST"
    SLOW = "SLOW"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ConstraintRampType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{99FB8664-490F-451b-8347-F5B6E29E5553}",
            kind="enumeration",
        )
    )

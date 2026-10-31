"""CIM enumeration ADSInstructionTypeOOS (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ADSInstructionTypeOOS(CimEnum):
    """MIN_CONSTRAINT

    MAX_CONSTRAINT

    FIXED_CONSTRAINT"""

    MIN_CONSTRAINT = "MIN_CONSTRAINT"
    MAX_CONSTRAINT = "MAX_CONSTRAINT"
    FIXED_CONSTRAINT = "FIXED_CONSTRAINT"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ADSInstructionTypeOOS",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{6B50D9E2-ACFF-4dcd-AA03-2E2F1EF34878}",
            kind="enumeration",
        )
    )

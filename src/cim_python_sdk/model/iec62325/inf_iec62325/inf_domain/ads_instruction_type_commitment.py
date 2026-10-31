"""CIM enumeration ADSInstructionTypeCommitment (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ADSInstructionTypeCommitment(CimEnum):
    """CIM enumeration ADSInstructionTypeCommitment."""

    START_UP = "START_UP"
    SHUT_DOWN = "SHUT_DOWN"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ADSInstructionTypeCommitment",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{A7302B16-BDEA-44f4-84C3-BB14238B3A89}",
            kind="enumeration",
        )
    )

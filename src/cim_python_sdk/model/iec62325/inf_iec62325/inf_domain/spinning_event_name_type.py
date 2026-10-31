"""CIM enumeration SpinningEventNameType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SpinningEventNameType(CimEnum):
    """CIM enumeration SpinningEventNameType."""

    EASTERN = "EASTERN"
    RFC_SR = "RFC-SR"
    SOUTH_S = "SOUTH-S"
    PJM = "PJM"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SpinningEventNameType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{676FDD34-A716-4bff-BB1D-A7FC37736ED5}",
            kind="enumeration",
        )
    )

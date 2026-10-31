"""CIM enumeration JobStartEndType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class JobStartEndType(CimEnum):
    """CIM enumeration JobStartEndType."""

    NA = "NA"
    START = "START"
    END = "END"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="JobStartEndType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{CBBA25CF-115A-485f-A32F-09D8073180A0}",
            kind="enumeration",
        )
    )

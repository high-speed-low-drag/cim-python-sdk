"""CIM enumeration SystemType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SystemType(CimEnum):
    """CIM enumeration SystemType."""

    OASIS = "OASIS"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SystemType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{DF554719-7CB9-459c-97CB-BF50631359CC}",
            kind="enumeration",
        )
    )

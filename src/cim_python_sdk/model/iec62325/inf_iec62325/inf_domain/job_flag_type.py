"""CIM enumeration JobFlagType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class JobFlagType(CimEnum):
    """CIM enumeration JobFlagType."""

    CREATED = "CREATED"
    MODIFIED = "MODIFIED"
    DELETED = "DELETED"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="JobFlagType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{DD9F3A69-9DA0-4b75-BF91-FE984AB783F3}",
            kind="enumeration",
        )
    )

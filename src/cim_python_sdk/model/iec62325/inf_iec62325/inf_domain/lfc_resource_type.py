"""CIM enumeration LFCResourceType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class LFCResourceType(CimEnum):
    """CIM enumeration LFCResourceType."""

    GEN = "GEN"
    PUMP = "PUMP"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="LFCResourceType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{9C05F8D9-4C2F-409f-908A-BC1DBFA90996}",
            kind="enumeration",
        )
    )

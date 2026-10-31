"""CIM enumeration CIGREStandardKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CIGREStandardKind(CimEnum):
    """List of CIGRE standards."""

    TB_170 = "TB 170"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CIGREStandardKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{C95BEFED-E3E1-4068-A095-DC5A87035AD7}",
            kind="enumeration",
        )
    )

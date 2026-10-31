"""CIM enumeration CIGREStandardEditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CIGREStandardEditionKind(CimEnum):
    """List of editions for CIGRE standards."""

    v2000 = "2000"
    none = "none"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CIGREStandardEditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{FED3D9B8-BD73-4dea-85A4-1556F72C59B7}",
            kind="enumeration",
        )
    )

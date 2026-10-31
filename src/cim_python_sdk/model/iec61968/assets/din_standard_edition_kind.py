"""CIM enumeration DINStandardEditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DINStandardEditionKind(CimEnum):
    """List of editions for DIN standards."""

    v1985 = "1985"
    none = "none"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DINStandardEditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{D918E627-FC16-4619-BCA9-7D247824D070}",
            kind="enumeration",
        )
    )

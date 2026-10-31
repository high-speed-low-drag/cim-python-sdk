"""CIM enumeration EPAStandardEditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EPAStandardEditionKind(CimEnum):
    """List of editions for EPA standards."""

    A = "A"
    none = "none"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EPAStandardEditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{5930F0B9-A581-4897-B001-D8552902E2AE}",
            kind="enumeration",
        )
    )

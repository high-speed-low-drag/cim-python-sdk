"""CIM enumeration EPAStandardKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EPAStandardKind(CimEnum):
    """List of EPA standards."""

    v8082 = "8082"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EPAStandardKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{6E4D6FF6-FFD8-4982-85D8-51BA27F3245F}",
            kind="enumeration",
        )
    )

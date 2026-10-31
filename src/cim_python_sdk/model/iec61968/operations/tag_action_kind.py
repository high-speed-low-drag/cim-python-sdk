"""CIM enumeration TagActionKind (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TagActionKind(CimEnum):
    """Kind of action on tag."""

    place = "place"
    remove = "remove"
    verify = "verify"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TagActionKind",
            package="TC57CIM/IEC61968/Operations",
            guid="{6BC03167-2A28-4eab-8411-8FDAE36C1B3F}",
            kind="enumeration",
        )
    )

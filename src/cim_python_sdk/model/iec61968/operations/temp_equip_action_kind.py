"""CIM enumeration TempEquipActionKind (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TempEquipActionKind(CimEnum):
    """Kind of action on temporary equipment (such as cut, jumper, ground, energy source)."""

    place = "place"
    remove = "remove"
    connect = "connect"
    disconnect = "disconnect"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TempEquipActionKind",
            package="TC57CIM/IEC61968/Operations",
            guid="{1049668D-02E1-4336-86E4-306D60B6CE13}",
            kind="enumeration",
        )
    )

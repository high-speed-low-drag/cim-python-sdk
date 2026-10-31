"""CIM enumeration WorkActionKind (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WorkActionKind(CimEnum):
    """Kinds of activities to be performed on a Compatible Unit."""

    install = "install"
    remove = "remove"
    abandon = "abandon"
    transfer = "transfer"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WorkActionKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfWork",
            guid="{20BAC52F-3C56-468a-B36F-0EBD262D55D9}",
            kind="enumeration",
        )
    )

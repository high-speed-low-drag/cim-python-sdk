"""CIM enumeration BatteryStateKind (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BatteryStateKind(CimEnum):
    """The state of the battery unit."""

    discharging = "discharging"
    full = "full"
    waiting = "waiting"
    charging = "charging"
    empty = "empty"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BatteryStateKind",
            package="TC57CIM/IEC61970/Base/Generation/Production",
            guid="{A7535AFF-0EA1-4791-B2C9-D5D366BB427A}",
            kind="enumeration",
        )
    )

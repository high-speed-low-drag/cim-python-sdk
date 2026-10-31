"""CIM enumeration GeneratorControlMode (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class GeneratorControlMode(CimEnum):
    """Unit control modes."""

    setpoint = "setpoint"
    pulse = "pulse"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="GeneratorControlMode",
            package="TC57CIM/IEC61970/Base/Generation/Production",
            guid="{F30D1912-7652-4857-9FA5-2EADBFF160E6}",
            kind="enumeration",
        )
    )

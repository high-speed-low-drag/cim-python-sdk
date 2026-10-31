"""CIM enumeration CsPpccControlKind (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CsPpccControlKind(CimEnum):
    """Active power control modes for HVDC line operating as Current Source Converter."""

    activePower = "activePower"
    dcVoltage = "dcVoltage"
    dcCurrent = "dcCurrent"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CsPpccControlKind",
            package="TC57CIM/IEC61970/Base/DC",
            guid="{C5B4CF4C-2315-467f-9238-26B1ED7BAEBB}",
            kind="enumeration",
        )
    )

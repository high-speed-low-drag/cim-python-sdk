"""CIM enumeration ControlAreaTypeKind (TC57CIM/IEC61970/Base/ControlArea). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ControlAreaTypeKind(CimEnum):
    """The type of control area."""

    AGC = "AGC"
    Forecast = "Forecast"
    Interchange = "Interchange"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ControlAreaTypeKind",
            package="TC57CIM/IEC61970/Base/ControlArea",
            guid="{43F2CD5E-92F8-4668-968F-1250CA99B754}",
            kind="enumeration",
        )
    )

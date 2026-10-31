"""CIM class Sensor (TC57CIM/IEC61970/Base/AuxiliaryEquipment). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.auxiliary_equipment.auxiliary_equipment import (
    AuxiliaryEquipment,
)


class Sensor(AuxiliaryEquipment):
    """This class describe devices that transform a measured quantity into signals that can be
    presented at displays, used in control or be recorded."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="Sensor",
        package="TC57CIM/IEC61970/Base/AuxiliaryEquipment",
        guid="{0697374C-946D-4033-A892-BA0929F3D30A}",
    )

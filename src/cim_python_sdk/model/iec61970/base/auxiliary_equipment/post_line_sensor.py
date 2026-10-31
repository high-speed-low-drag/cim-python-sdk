"""CIM class PostLineSensor (TC57CIM/IEC61970/Base/AuxiliaryEquipment). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.auxiliary_equipment.sensor import Sensor


class PostLineSensor(Sensor):
    """A sensor used mainly in overhead distribution networks as the source of both current and
    voltage measurements."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="PostLineSensor",
        package="TC57CIM/IEC61970/Base/AuxiliaryEquipment",
        guid="{7B763652-C385-4903-9FB1-E780E0C52E57}",
    )

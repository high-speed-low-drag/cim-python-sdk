"""CIM class SurgeArrester (TC57CIM/IEC61970/Base/AuxiliaryEquipment). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.auxiliary_equipment.auxiliary_equipment import (
    AuxiliaryEquipment,
)


class SurgeArrester(AuxiliaryEquipment):
    """Shunt device, installed on the network, usually in the proximity of electrical equipment
    in order to protect the said equipment against transient voltage transients caused by
    lightning or switching activity."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="SurgeArrester",
        package="TC57CIM/IEC61970/Base/AuxiliaryEquipment",
        guid="{5B376A76-B1BA-48a1-B0BF-A0EAE8B4C61B}",
    )

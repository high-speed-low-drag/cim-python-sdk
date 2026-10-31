"""CIM class DCChopper (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.dc.dc_conducting_equipment import DCConductingEquipment


class DCChopper(DCConductingEquipment):
    """Low resistance equipment used in the internal DC circuit to balance voltages. It has
    typically positive and negative pole terminals and a ground."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="DCChopper",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{D96FC474-26B0-4d61-893F-89BA88CB8B1A}",
    )

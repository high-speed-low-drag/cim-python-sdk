"""CIM class FaultIndicator (TC57CIM/IEC61970/Base/AuxiliaryEquipment). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.auxiliary_equipment.auxiliary_equipment import (
    AuxiliaryEquipment,
)


class FaultIndicator(AuxiliaryEquipment):
    """A FaultIndicator is typically only an indicator (which may or may not be remotely
    monitored), and not a piece of equipment that actually initiates a protection event. It
    is used for FLISR (Fault Location, Isolation and Restoration) purposes, assisting with
    the dispatch of crews to "most likely" part of the network (i.e. assists with
    determining circuit section where the fault most likely happened)."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="FaultIndicator",
        package="TC57CIM/IEC61970/Base/AuxiliaryEquipment",
        guid="{E0096FB8-0394-4d99-9726-5FBD336FD801}",
    )

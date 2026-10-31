"""CIM class StationSupply (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.wires.energy_consumer import EnergyConsumer


class StationSupply(EnergyConsumer):
    """Station supply with load derived from the station output."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="StationSupply",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{67147C58-10F8-4463-93B7-7905358489FD}",
    )

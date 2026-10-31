"""CIM class PowerCutZone (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.energy_consumer import EnergyConsumer


class PowerCutZone(PowerSystemResource):
    """An area or zone of the power system which is used for load shedding purposes."""

    __slots__ = ("_energy_consumers", "cut_level1", "cut_level2")

    cut_level1: float | None  # PerCent
    cut_level2: float | None  # PerCent

    energy_consumers: Many[EnergyConsumer] = Many(
        EndMeta(
            name="energy_consumers",
            cim_role="EnergyConsumers",
            target="cim_python_sdk.model.iec61970.base.wires.energy_consumer:EnergyConsumer",
            many=True,
            lower=1,
            upper=None,
            inverse="power_cut_zone",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PowerCutZone",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{8B5E449E-F8E0-4b7a-93B4-2A0D37E5677C}",
        attributes=(
            AttrMeta("cut_level1", "cutLevel1", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("cut_level2", "cutLevel2", "PerCent", 0, 1, "cimdatatype"),
        ),
        ends=(energy_consumers.meta,),
    )

    def __init__(
        self,
        *,
        cut_level1: float | None = None,
        cut_level2: float | None = None,
        energy_consumers: Iterable[EnergyConsumer] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cut_level1 = cut_level1
        self.cut_level2 = cut_level2
        if energy_consumers is not None:
            PowerCutZone.energy_consumers.extend(self, energy_consumers)

    def add_energy_consumer(self, energy_consumer: EnergyConsumer) -> Self:
        return PowerCutZone.energy_consumers.add(self, energy_consumer)

    def remove_energy_consumer(self, energy_consumer: EnergyConsumer) -> Self:
        return PowerCutZone.energy_consumers.remove(self, energy_consumer)

    def clear_energy_consumers(self) -> Self:
        return PowerCutZone.energy_consumers.clear(self)

    def num_energy_consumer(self) -> int:
        return PowerCutZone.energy_consumers.count(self)

    def get_energy_consumer_by_mrid(self, mrid: str) -> EnergyConsumer | None:
        return PowerCutZone.energy_consumers.get_by_mrid(self, mrid)

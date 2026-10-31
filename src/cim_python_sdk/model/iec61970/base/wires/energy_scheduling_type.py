"""CIM class EnergySchedulingType (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.energy_source import EnergySource


class EnergySchedulingType(IdentifiedObject):
    """Used to define the type of generation for scheduling purposes."""

    __slots__ = ("_energy_source",)

    energy_source: Many[EnergySource] = Many(
        EndMeta(
            name="energy_source",
            cim_role="EnergySource",
            target="cim_python_sdk.model.iec61970.base.wires.energy_source:EnergySource",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_scheduling_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergySchedulingType",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{8FD4114B-3942-4e7c-8E33-9600BA19CF38}",
        ends=(energy_source.meta,),
    )

    def __init__(
        self,
        *,
        energy_source: Iterable[EnergySource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if energy_source is not None:
            EnergySchedulingType.energy_source.extend(self, energy_source)

    def add_energy_source(self, energy_source: EnergySource) -> Self:
        return EnergySchedulingType.energy_source.add(self, energy_source)

    def remove_energy_source(self, energy_source: EnergySource) -> Self:
        return EnergySchedulingType.energy_source.remove(self, energy_source)

    def clear_energy_source(self) -> Self:
        return EnergySchedulingType.energy_source.clear(self)

    def num_energy_source(self) -> int:
        return EnergySchedulingType.energy_source.count(self)

    def get_energy_source_by_mrid(self, mrid: str) -> EnergySource | None:
        return EnergySchedulingType.energy_source.get_by_mrid(self, mrid)

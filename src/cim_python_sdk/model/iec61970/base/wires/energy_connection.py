"""CIM class EnergyConnection (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_component import (
        EnergyComponent,
    )


class EnergyConnection(ConductingEquipment):
    """A connection of energy generation or consumption on the power system model."""

    __slots__ = ("_energy_components",)

    energy_components: Many[EnergyComponent] = Many(
        EndMeta(
            name="energy_components",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_component:EnergyComponent",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_connection",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyConnection",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{13966DE6-BE71-4f50-8051-2A082891138D}",
        ends=(energy_components.meta,),
    )

    def __init__(
        self,
        *,
        energy_components: Iterable[EnergyComponent] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if energy_components is not None:
            EnergyConnection.energy_components.extend(self, energy_components)

    def add_energy_component(self, energy_component: EnergyComponent) -> Self:
        return EnergyConnection.energy_components.add(self, energy_component)

    def remove_energy_component(self, energy_component: EnergyComponent) -> Self:
        return EnergyConnection.energy_components.remove(self, energy_component)

    def clear_energy_components(self) -> Self:
        return EnergyConnection.energy_components.clear(self)

    def num_energy_component(self) -> int:
        return EnergyConnection.energy_components.count(self)

    def get_energy_component_by_mrid(self, mrid: str) -> EnergyComponent | None:
        return EnergyConnection.energy_components.get_by_mrid(self, mrid)

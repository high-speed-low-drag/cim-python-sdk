"""CIM class EquipmentContainer (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.connectivity_node_container import (
    ConnectivityNodeContainer,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment


class EquipmentContainer(ConnectivityNodeContainer):
    """A modelling construct to provide a root class for containing equipment."""

    __slots__ = ("_additional_grouped_equipment", "_equipments")

    additional_grouped_equipment: Many[Equipment] = Many(
        EndMeta(
            name="additional_grouped_equipment",
            cim_role="AdditionalGroupedEquipment",
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=True,
            lower=0,
            upper=None,
            inverse="additional_equipment_container",
            aggregation="none",
        )
    )
    equipments: Many[Equipment] = Many(
        EndMeta(
            name="equipments",
            cim_role="Equipments",
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=True,
            lower=0,
            upper=None,
            inverse="equipment_container",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EquipmentContainer",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{F465B7B4-B488-46c5-8D05-8036F09A03A0}",
        ends=(
            additional_grouped_equipment.meta,
            equipments.meta,
        ),
    )

    def __init__(
        self,
        *,
        additional_grouped_equipment: Iterable[Equipment] | None = None,
        equipments: Iterable[Equipment] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if additional_grouped_equipment is not None:
            EquipmentContainer.additional_grouped_equipment.extend(
                self, additional_grouped_equipment
            )
        if equipments is not None:
            EquipmentContainer.equipments.extend(self, equipments)

    def add_additional_grouped_equipment(self, additional_grouped_equipment: Equipment) -> Self:
        return EquipmentContainer.additional_grouped_equipment.add(
            self, additional_grouped_equipment
        )

    def remove_additional_grouped_equipment(self, additional_grouped_equipment: Equipment) -> Self:
        return EquipmentContainer.additional_grouped_equipment.remove(
            self, additional_grouped_equipment
        )

    def clear_additional_grouped_equipment(self) -> Self:
        return EquipmentContainer.additional_grouped_equipment.clear(self)

    def num_additional_grouped_equipment(self) -> int:
        return EquipmentContainer.additional_grouped_equipment.count(self)

    def get_additional_grouped_equipment_by_mrid(self, mrid: str) -> Equipment | None:
        return EquipmentContainer.additional_grouped_equipment.get_by_mrid(self, mrid)

    def add_equipment(self, equipment: Equipment) -> Self:
        return EquipmentContainer.equipments.add(self, equipment)

    def remove_equipment(self, equipment: Equipment) -> Self:
        return EquipmentContainer.equipments.remove(self, equipment)

    def clear_equipments(self) -> Self:
        return EquipmentContainer.equipments.clear(self)

    def num_equipment(self) -> int:
        return EquipmentContainer.equipments.count(self)

    def get_equipment_by_mrid(self, mrid: str) -> Equipment | None:
        return EquipmentContainer.equipments.get_by_mrid(self, mrid)

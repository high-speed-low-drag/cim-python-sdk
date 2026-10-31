"""CIM class EquivalentNetwork (TC57CIM/IEC61970/Base/Equivalents). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.connectivity_node_container import (
    ConnectivityNodeContainer,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.equivalents.equivalent_equipment import (
        EquivalentEquipment,
    )


class EquivalentNetwork(ConnectivityNodeContainer):
    """A class that groups electrical equivalents, including internal nodes, of a network that
    has been reduced. The ConnectivityNodes contained in the equivalent are intended to
    reflect internal nodes of the equivalent. The boundary Connectivity nodes where the
    equivalent connects outside itself are not contained by the equivalent."""

    __slots__ = ("_equivalent_equipments",)

    equivalent_equipments: Many[EquivalentEquipment] = Many(
        EndMeta(
            name="equivalent_equipments",
            cim_role="EquivalentEquipments",
            target="cim_python_sdk.model.iec61970.base.equivalents.equivalent_equipment:EquivalentEquipment",
            many=True,
            lower=0,
            upper=None,
            inverse="equivalent_network",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EquivalentNetwork",
        package="TC57CIM/IEC61970/Base/Equivalents",
        guid="{1FCEE6DF-2D36-4ee8-8CB9-0EFC3F000799}",
        ends=(equivalent_equipments.meta,),
    )

    def __init__(
        self,
        *,
        equivalent_equipments: Iterable[EquivalentEquipment] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if equivalent_equipments is not None:
            EquivalentNetwork.equivalent_equipments.extend(self, equivalent_equipments)

    def add_equivalent_equipment(self, equivalent_equipment: EquivalentEquipment) -> Self:
        return EquivalentNetwork.equivalent_equipments.add(self, equivalent_equipment)

    def remove_equivalent_equipment(self, equivalent_equipment: EquivalentEquipment) -> Self:
        return EquivalentNetwork.equivalent_equipments.remove(self, equivalent_equipment)

    def clear_equivalent_equipments(self) -> Self:
        return EquivalentNetwork.equivalent_equipments.clear(self)

    def num_equivalent_equipment(self) -> int:
        return EquivalentNetwork.equivalent_equipments.count(self)

    def get_equivalent_equipment_by_mrid(self, mrid: str) -> EquivalentEquipment | None:
        return EquivalentNetwork.equivalent_equipments.get_by_mrid(self, mrid)

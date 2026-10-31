"""CIM class EnergyTypeReference (TC57CIM/IEC61970/InfIEC61970/EnergyArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_group import EnergyGroup
    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_type_kind import (
        EnergyTypeKind,
    )


class EnergyTypeReference(IdentifiedObject):
    """CIM class EnergyTypeReference."""

    __slots__ = ("_energy_groups", "kind")

    kind: EnergyTypeKind | None

    energy_groups: Many[EnergyGroup] = Many(
        EndMeta(
            name="energy_groups",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_group:EnergyGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_type_reference",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyTypeReference",
        package="TC57CIM/IEC61970/InfIEC61970/EnergyArea",
        guid="{235A7C92-A579-44fb-BDF1-7741E42009B3}",
        attributes=(AttrMeta("kind", "kind", "EnergyTypeKind", 0, 1, "enumeration"),),
        ends=(energy_groups.meta,),
    )

    def __init__(
        self,
        *,
        kind: EnergyTypeKind | None = None,
        energy_groups: Iterable[EnergyGroup] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if energy_groups is not None:
            EnergyTypeReference.energy_groups.extend(self, energy_groups)

    def add_energy_group(self, energy_group: EnergyGroup) -> Self:
        return EnergyTypeReference.energy_groups.add(self, energy_group)

    def remove_energy_group(self, energy_group: EnergyGroup) -> Self:
        return EnergyTypeReference.energy_groups.remove(self, energy_group)

    def clear_energy_groups(self) -> Self:
        return EnergyTypeReference.energy_groups.clear(self)

    def num_energy_group(self) -> int:
        return EnergyTypeReference.energy_groups.count(self)

    def get_energy_group_by_mrid(self, mrid: str) -> EnergyGroup | None:
        return EnergyTypeReference.energy_groups.get_by_mrid(self, mrid)

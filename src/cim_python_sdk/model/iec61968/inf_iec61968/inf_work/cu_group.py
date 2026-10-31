"""CIM class CUGroup (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit import CompatibleUnit
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location_cu import (
        DesignLocationCU,
    )


class CUGroup(WorkIdentifiedObject):
    """A Compatible Unit Group identifies a set of compatible units which may be jointly
    utilized for estimating and designating jobs."""

    __slots__ = (
        "_child_cu_groups",
        "_compatible_units",
        "_design_location_cus",
        "_parent_cu_groups",
        "status",
    )

    status: Status | None

    design_location_cus: Many[DesignLocationCU] = Many(
        EndMeta(
            name="design_location_cus",
            cim_role="DesignLocationCUs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location_cu:DesignLocationCU",
            many=True,
            lower=0,
            upper=None,
            inverse="cu_groups",
            aggregation="none",
        )
    )
    compatible_units: Many[CompatibleUnit] = Many(
        EndMeta(
            name="compatible_units",
            cim_role="CompatibleUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit:CompatibleUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="cu_group",
            aggregation="none",
        )
    )
    child_cu_groups: Many[CUGroup] = Many(
        EndMeta(
            name="child_cu_groups",
            cim_role="ChildCUGroups",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_group:CUGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="parent_cu_groups",
            aggregation="none",
        )
    )
    parent_cu_groups: Many[CUGroup] = Many(
        EndMeta(
            name="parent_cu_groups",
            cim_role="ParentCUGroups",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_group:CUGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="child_cu_groups",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CUGroup",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{E982DB17-483A-4dcc-B45E-2765C09C6E46}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(
            design_location_cus.meta,
            compatible_units.meta,
            child_cu_groups.meta,
            parent_cu_groups.meta,
        ),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        design_location_cus: Iterable[DesignLocationCU] | None = None,
        compatible_units: Iterable[CompatibleUnit] | None = None,
        child_cu_groups: Iterable[CUGroup] | None = None,
        parent_cu_groups: Iterable[CUGroup] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if design_location_cus is not None:
            CUGroup.design_location_cus.extend(self, design_location_cus)
        if compatible_units is not None:
            CUGroup.compatible_units.extend(self, compatible_units)
        if child_cu_groups is not None:
            CUGroup.child_cu_groups.extend(self, child_cu_groups)
        if parent_cu_groups is not None:
            CUGroup.parent_cu_groups.extend(self, parent_cu_groups)

    def add_design_location_cu(self, design_location_cu: DesignLocationCU) -> Self:
        return CUGroup.design_location_cus.add(self, design_location_cu)

    def remove_design_location_cu(self, design_location_cu: DesignLocationCU) -> Self:
        return CUGroup.design_location_cus.remove(self, design_location_cu)

    def clear_design_location_cus(self) -> Self:
        return CUGroup.design_location_cus.clear(self)

    def num_design_location_cu(self) -> int:
        return CUGroup.design_location_cus.count(self)

    def get_design_location_cu_by_mrid(self, mrid: str) -> DesignLocationCU | None:
        return CUGroup.design_location_cus.get_by_mrid(self, mrid)

    def add_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CUGroup.compatible_units.add(self, compatible_unit)

    def remove_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CUGroup.compatible_units.remove(self, compatible_unit)

    def clear_compatible_units(self) -> Self:
        return CUGroup.compatible_units.clear(self)

    def num_compatible_unit(self) -> int:
        return CUGroup.compatible_units.count(self)

    def get_compatible_unit_by_mrid(self, mrid: str) -> CompatibleUnit | None:
        return CUGroup.compatible_units.get_by_mrid(self, mrid)

    def add_child_cu_group(self, child_cu_group: CUGroup) -> Self:
        return CUGroup.child_cu_groups.add(self, child_cu_group)

    def remove_child_cu_group(self, child_cu_group: CUGroup) -> Self:
        return CUGroup.child_cu_groups.remove(self, child_cu_group)

    def clear_child_cu_groups(self) -> Self:
        return CUGroup.child_cu_groups.clear(self)

    def num_child_cu_group(self) -> int:
        return CUGroup.child_cu_groups.count(self)

    def get_child_cu_group_by_mrid(self, mrid: str) -> CUGroup | None:
        return CUGroup.child_cu_groups.get_by_mrid(self, mrid)

    def add_parent_cu_group(self, parent_cu_group: CUGroup) -> Self:
        return CUGroup.parent_cu_groups.add(self, parent_cu_group)

    def remove_parent_cu_group(self, parent_cu_group: CUGroup) -> Self:
        return CUGroup.parent_cu_groups.remove(self, parent_cu_group)

    def clear_parent_cu_groups(self) -> Self:
        return CUGroup.parent_cu_groups.clear(self)

    def num_parent_cu_group(self) -> int:
        return CUGroup.parent_cu_groups.count(self)

    def get_parent_cu_group_by_mrid(self, mrid: str) -> CUGroup | None:
        return CUGroup.parent_cu_groups.get_by_mrid(self, mrid)

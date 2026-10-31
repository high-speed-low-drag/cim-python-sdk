"""CIM class DesignLocationCU (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit import CompatibleUnit
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.condition_factor import ConditionFactor
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_group import CUGroup
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design import Design
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location import DesignLocation
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task import OldWorkTask
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_action_kind import WorkActionKind
    from cim_python_sdk.model.iec61970.base.domain.integer_quantity import IntegerQuantity


class DesignLocationCU(WorkIdentifiedObject):
    """Compatible unit at a given design location."""

    __slots__ = (
        "_compatible_units",
        "_condition_factors",
        "_cu_groups",
        "_design_location",
        "_designs",
        "_work_tasks",
        "cu_account",
        "cu_action",
        "cu_quantity",
        "cu_usage",
        "removal_date",
        "status",
        "to_be_energised",
    )

    cu_quantity: IntegerQuantity | None
    cu_action: WorkActionKind | None
    cu_usage: str | None
    cu_account: str | None
    to_be_energised: bool | None
    removal_date: _dt.date | None
    status: Status | None

    cu_groups: Many[CUGroup] = Many(
        EndMeta(
            name="cu_groups",
            cim_role="CUGroups",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_group:CUGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="design_location_cus",
            aggregation="none",
        )
    )
    designs: Many[Design] = Many(
        EndMeta(
            name="designs",
            cim_role="Designs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design:Design",
            many=True,
            lower=0,
            upper=None,
            inverse="design_locations_cus",
            aggregation="none",
        )
    )
    design_location: One[DesignLocation] = One(
        EndMeta(
            name="design_location",
            cim_role="DesignLocation",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location:DesignLocation",
            many=False,
            lower=0,
            upper=1,
            inverse="design_location_cus",
            aggregation="none",
        )
    )
    condition_factors: Many[ConditionFactor] = Many(
        EndMeta(
            name="condition_factors",
            cim_role="ConditionFactors",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.condition_factor:ConditionFactor",
            many=True,
            lower=0,
            upper=None,
            inverse="design_location_cus",
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
            inverse="design_location_cus",
            aggregation="none",
        )
    )
    work_tasks: Many[OldWorkTask] = Many(
        EndMeta(
            name="work_tasks",
            cim_role="WorkTasks",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task:OldWorkTask",
            many=True,
            lower=0,
            upper=None,
            inverse="design_location_cus",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DesignLocationCU",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{F7726C92-5D4D-4254-B628-8E3DE89B0D83}",
        attributes=(
            AttrMeta("cu_quantity", "cuQuantity", "IntegerQuantity", 0, 1, "compound"),
            AttrMeta("cu_action", "cuAction", "WorkActionKind", 0, 1, "enumeration"),
            AttrMeta("cu_usage", "cuUsage", "str", 0, 1, "primitive"),
            AttrMeta("cu_account", "cuAccount", "str", 0, 1, "primitive"),
            AttrMeta("to_be_energised", "toBeEnergised", "bool", 0, 1, "primitive"),
            AttrMeta("removal_date", "removalDate", "date", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            cu_groups.meta,
            designs.meta,
            design_location.meta,
            condition_factors.meta,
            compatible_units.meta,
            work_tasks.meta,
        ),
    )

    def __init__(
        self,
        *,
        cu_quantity: IntegerQuantity | None = None,
        cu_action: WorkActionKind | None = None,
        cu_usage: str | None = None,
        cu_account: str | None = None,
        to_be_energised: bool | None = None,
        removal_date: _dt.date | None = None,
        status: Status | None = None,
        cu_groups: Iterable[CUGroup] | None = None,
        designs: Iterable[Design] | None = None,
        design_location: DesignLocation | None = None,
        condition_factors: Iterable[ConditionFactor] | None = None,
        compatible_units: Iterable[CompatibleUnit] | None = None,
        work_tasks: Iterable[OldWorkTask] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cu_quantity = cu_quantity
        self.cu_action = cu_action
        self.cu_usage = cu_usage
        self.cu_account = cu_account
        self.to_be_energised = to_be_energised
        self.removal_date = removal_date
        self.status = status
        if cu_groups is not None:
            DesignLocationCU.cu_groups.extend(self, cu_groups)
        if designs is not None:
            DesignLocationCU.designs.extend(self, designs)
        if design_location is not None:
            self.design_location = design_location
        if condition_factors is not None:
            DesignLocationCU.condition_factors.extend(self, condition_factors)
        if compatible_units is not None:
            DesignLocationCU.compatible_units.extend(self, compatible_units)
        if work_tasks is not None:
            DesignLocationCU.work_tasks.extend(self, work_tasks)

    def add_cu_group(self, cu_group: CUGroup) -> Self:
        return DesignLocationCU.cu_groups.add(self, cu_group)

    def remove_cu_group(self, cu_group: CUGroup) -> Self:
        return DesignLocationCU.cu_groups.remove(self, cu_group)

    def clear_cu_groups(self) -> Self:
        return DesignLocationCU.cu_groups.clear(self)

    def num_cu_group(self) -> int:
        return DesignLocationCU.cu_groups.count(self)

    def get_cu_group_by_mrid(self, mrid: str) -> CUGroup | None:
        return DesignLocationCU.cu_groups.get_by_mrid(self, mrid)

    def add_design(self, design: Design) -> Self:
        return DesignLocationCU.designs.add(self, design)

    def remove_design(self, design: Design) -> Self:
        return DesignLocationCU.designs.remove(self, design)

    def clear_designs(self) -> Self:
        return DesignLocationCU.designs.clear(self)

    def num_design(self) -> int:
        return DesignLocationCU.designs.count(self)

    def get_design_by_mrid(self, mrid: str) -> Design | None:
        return DesignLocationCU.designs.get_by_mrid(self, mrid)

    def add_condition_factor(self, condition_factor: ConditionFactor) -> Self:
        return DesignLocationCU.condition_factors.add(self, condition_factor)

    def remove_condition_factor(self, condition_factor: ConditionFactor) -> Self:
        return DesignLocationCU.condition_factors.remove(self, condition_factor)

    def clear_condition_factors(self) -> Self:
        return DesignLocationCU.condition_factors.clear(self)

    def num_condition_factor(self) -> int:
        return DesignLocationCU.condition_factors.count(self)

    def get_condition_factor_by_mrid(self, mrid: str) -> ConditionFactor | None:
        return DesignLocationCU.condition_factors.get_by_mrid(self, mrid)

    def add_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return DesignLocationCU.compatible_units.add(self, compatible_unit)

    def remove_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return DesignLocationCU.compatible_units.remove(self, compatible_unit)

    def clear_compatible_units(self) -> Self:
        return DesignLocationCU.compatible_units.clear(self)

    def num_compatible_unit(self) -> int:
        return DesignLocationCU.compatible_units.count(self)

    def get_compatible_unit_by_mrid(self, mrid: str) -> CompatibleUnit | None:
        return DesignLocationCU.compatible_units.get_by_mrid(self, mrid)

    def add_work_task(self, work_task: OldWorkTask) -> Self:
        return DesignLocationCU.work_tasks.add(self, work_task)

    def remove_work_task(self, work_task: OldWorkTask) -> Self:
        return DesignLocationCU.work_tasks.remove(self, work_task)

    def clear_work_tasks(self) -> Self:
        return DesignLocationCU.work_tasks.clear(self)

    def num_work_task(self) -> int:
        return DesignLocationCU.work_tasks.count(self)

    def get_work_task_by_mrid(self, mrid: str) -> OldWorkTask | None:
        return DesignLocationCU.work_tasks.get_by_mrid(self, mrid)

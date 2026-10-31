"""CIM class PropertyUnit (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_material_item import CUMaterialItem
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_action_kind import WorkActionKind
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail import WorkCostDetail


class PropertyUnit(WorkIdentifiedObject):
    """Unit of property for reporting purposes."""

    __slots__ = (
        "_compatible_units",
        "_cu_material_items",
        "_work_cost_details",
        "accounting_usage",
        "activity_code",
        "property_account",
        "status",
    )

    activity_code: WorkActionKind | None
    property_account: str | None
    accounting_usage: str | None
    status: Status | None

    compatible_units: Many[CompatibleUnit] = Many(
        EndMeta(
            name="compatible_units",
            cim_role="CompatibleUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit:CompatibleUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="property_unit",
            aggregation="none",
        )
    )
    work_cost_details: Many[WorkCostDetail] = Many(
        EndMeta(
            name="work_cost_details",
            cim_role="WorkCostDetails",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail:WorkCostDetail",
            many=True,
            lower=0,
            upper=None,
            inverse="property_units",
            aggregation="none",
        )
    )
    cu_material_items: Many[CUMaterialItem] = Many(
        EndMeta(
            name="cu_material_items",
            cim_role="CUMaterialItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cu_material_item:CUMaterialItem",
            many=True,
            lower=0,
            upper=None,
            inverse="property_units",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PropertyUnit",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{4364909D-8DDE-40db-B0C8-E3CF7EC2EABC}",
        attributes=(
            AttrMeta("activity_code", "activityCode", "WorkActionKind", 0, 1, "enumeration"),
            AttrMeta("property_account", "propertyAccount", "str", 0, 1, "primitive"),
            AttrMeta("accounting_usage", "accountingUsage", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            compatible_units.meta,
            work_cost_details.meta,
            cu_material_items.meta,
        ),
    )

    def __init__(
        self,
        *,
        activity_code: WorkActionKind | None = None,
        property_account: str | None = None,
        accounting_usage: str | None = None,
        status: Status | None = None,
        compatible_units: Iterable[CompatibleUnit] | None = None,
        work_cost_details: Iterable[WorkCostDetail] | None = None,
        cu_material_items: Iterable[CUMaterialItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.activity_code = activity_code
        self.property_account = property_account
        self.accounting_usage = accounting_usage
        self.status = status
        if compatible_units is not None:
            PropertyUnit.compatible_units.extend(self, compatible_units)
        if work_cost_details is not None:
            PropertyUnit.work_cost_details.extend(self, work_cost_details)
        if cu_material_items is not None:
            PropertyUnit.cu_material_items.extend(self, cu_material_items)

    def add_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return PropertyUnit.compatible_units.add(self, compatible_unit)

    def remove_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return PropertyUnit.compatible_units.remove(self, compatible_unit)

    def clear_compatible_units(self) -> Self:
        return PropertyUnit.compatible_units.clear(self)

    def num_compatible_unit(self) -> int:
        return PropertyUnit.compatible_units.count(self)

    def get_compatible_unit_by_mrid(self, mrid: str) -> CompatibleUnit | None:
        return PropertyUnit.compatible_units.get_by_mrid(self, mrid)

    def add_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return PropertyUnit.work_cost_details.add(self, work_cost_detail)

    def remove_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return PropertyUnit.work_cost_details.remove(self, work_cost_detail)

    def clear_work_cost_details(self) -> Self:
        return PropertyUnit.work_cost_details.clear(self)

    def num_work_cost_detail(self) -> int:
        return PropertyUnit.work_cost_details.count(self)

    def get_work_cost_detail_by_mrid(self, mrid: str) -> WorkCostDetail | None:
        return PropertyUnit.work_cost_details.get_by_mrid(self, mrid)

    def add_cu_material_item(self, cu_material_item: CUMaterialItem) -> Self:
        return PropertyUnit.cu_material_items.add(self, cu_material_item)

    def remove_cu_material_item(self, cu_material_item: CUMaterialItem) -> Self:
        return PropertyUnit.cu_material_items.remove(self, cu_material_item)

    def clear_cu_material_items(self) -> Self:
        return PropertyUnit.cu_material_items.clear(self)

    def num_cu_material_item(self) -> int:
        return PropertyUnit.cu_material_items.count(self)

    def get_cu_material_item_by_mrid(self, mrid: str) -> CUMaterialItem | None:
        return PropertyUnit.cu_material_items.get_by_mrid(self, mrid)

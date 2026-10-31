"""CIM class CostType (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_journal_entry import (
        ErpJournalEntry,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit import CompatibleUnit
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail import WorkCostDetail


class CostType(WorkIdentifiedObject):
    """A categorization for resources, often costs, in accounting transactions. Examples
    include: material components, building in service, coal sales, overhead, etc."""

    __slots__ = (
        "_child_cost_types",
        "_compatible_units",
        "_erp_journal_entries",
        "_parent_cost_type",
        "_work_cost_details",
        "amount_assignable",
        "code",
        "level",
        "stage",
        "status",
    )

    code: str | None
    level: str | None
    amount_assignable: bool | None
    stage: str | None
    status: Status | None

    compatible_units: Many[CompatibleUnit] = Many(
        EndMeta(
            name="compatible_units",
            cim_role="CompatibleUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.compatible_unit:CompatibleUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="cost_type",
            aggregation="none",
        )
    )
    erp_journal_entries: Many[ErpJournalEntry] = Many(
        EndMeta(
            name="erp_journal_entries",
            cim_role="ErpJournalEntries",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_journal_entry:ErpJournalEntry",
            many=True,
            lower=0,
            upper=None,
            inverse="cost_types",
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
            inverse="cost_type",
            aggregation="none",
        )
    )
    child_cost_types: Many[CostType] = Many(
        EndMeta(
            name="child_cost_types",
            cim_role="ChildCostTypes",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cost_type:CostType",
            many=True,
            lower=0,
            upper=None,
            inverse="parent_cost_type",
            aggregation="none",
        )
    )
    parent_cost_type: One[CostType] = One(
        EndMeta(
            name="parent_cost_type",
            cim_role="ParentCostType",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cost_type:CostType",
            many=False,
            lower=0,
            upper=1,
            inverse="child_cost_types",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CostType",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{53228BC5-8B43-4db9-BADE-6C63046E1D52}",
        attributes=(
            AttrMeta("code", "code", "str", 0, 1, "primitive"),
            AttrMeta("level", "level", "str", 0, 1, "primitive"),
            AttrMeta("amount_assignable", "amountAssignable", "bool", 0, 1, "primitive"),
            AttrMeta("stage", "stage", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            compatible_units.meta,
            erp_journal_entries.meta,
            work_cost_details.meta,
            child_cost_types.meta,
            parent_cost_type.meta,
        ),
    )

    def __init__(
        self,
        *,
        code: str | None = None,
        level: str | None = None,
        amount_assignable: bool | None = None,
        stage: str | None = None,
        status: Status | None = None,
        compatible_units: Iterable[CompatibleUnit] | None = None,
        erp_journal_entries: Iterable[ErpJournalEntry] | None = None,
        work_cost_details: Iterable[WorkCostDetail] | None = None,
        child_cost_types: Iterable[CostType] | None = None,
        parent_cost_type: CostType | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.code = code
        self.level = level
        self.amount_assignable = amount_assignable
        self.stage = stage
        self.status = status
        if compatible_units is not None:
            CostType.compatible_units.extend(self, compatible_units)
        if erp_journal_entries is not None:
            CostType.erp_journal_entries.extend(self, erp_journal_entries)
        if work_cost_details is not None:
            CostType.work_cost_details.extend(self, work_cost_details)
        if child_cost_types is not None:
            CostType.child_cost_types.extend(self, child_cost_types)
        if parent_cost_type is not None:
            self.parent_cost_type = parent_cost_type

    def add_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CostType.compatible_units.add(self, compatible_unit)

    def remove_compatible_unit(self, compatible_unit: CompatibleUnit) -> Self:
        return CostType.compatible_units.remove(self, compatible_unit)

    def clear_compatible_units(self) -> Self:
        return CostType.compatible_units.clear(self)

    def num_compatible_unit(self) -> int:
        return CostType.compatible_units.count(self)

    def get_compatible_unit_by_mrid(self, mrid: str) -> CompatibleUnit | None:
        return CostType.compatible_units.get_by_mrid(self, mrid)

    def add_erp_journal_entry(self, erp_journal_entry: ErpJournalEntry) -> Self:
        return CostType.erp_journal_entries.add(self, erp_journal_entry)

    def remove_erp_journal_entry(self, erp_journal_entry: ErpJournalEntry) -> Self:
        return CostType.erp_journal_entries.remove(self, erp_journal_entry)

    def clear_erp_journal_entries(self) -> Self:
        return CostType.erp_journal_entries.clear(self)

    def num_erp_journal_entry(self) -> int:
        return CostType.erp_journal_entries.count(self)

    def get_erp_journal_entry_by_mrid(self, mrid: str) -> ErpJournalEntry | None:
        return CostType.erp_journal_entries.get_by_mrid(self, mrid)

    def add_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return CostType.work_cost_details.add(self, work_cost_detail)

    def remove_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return CostType.work_cost_details.remove(self, work_cost_detail)

    def clear_work_cost_details(self) -> Self:
        return CostType.work_cost_details.clear(self)

    def num_work_cost_detail(self) -> int:
        return CostType.work_cost_details.count(self)

    def get_work_cost_detail_by_mrid(self, mrid: str) -> WorkCostDetail | None:
        return CostType.work_cost_details.get_by_mrid(self, mrid)

    def add_child_cost_type(self, child_cost_type: CostType) -> Self:
        return CostType.child_cost_types.add(self, child_cost_type)

    def remove_child_cost_type(self, child_cost_type: CostType) -> Self:
        return CostType.child_cost_types.remove(self, child_cost_type)

    def clear_child_cost_types(self) -> Self:
        return CostType.child_cost_types.clear(self)

    def num_child_cost_type(self) -> int:
        return CostType.child_cost_types.count(self)

    def get_child_cost_type_by_mrid(self, mrid: str) -> CostType | None:
        return CostType.child_cost_types.get_by_mrid(self, mrid)

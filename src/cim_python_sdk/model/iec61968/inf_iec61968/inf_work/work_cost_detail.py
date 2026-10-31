"""CIM class WorkCostDetail (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_project_accounting import (
        ErpProjectAccounting,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.contractor_item import ContractorItem
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cost_type import CostType
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design import Design
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.labor_item import LaborItem
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.misc_cost_item import MiscCostItem
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task import OldWorkTask
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.overhead_cost import OverheadCost
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.property_unit import PropertyUnit
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_summary import (
        WorkCostSummary,
    )
    from cim_python_sdk.model.iec61968.work.work import Work


class WorkCostDetail(WorkDocument):
    """A collection of all of the individual cost items collected from multiple sources."""

    __slots__ = (
        "_contractor_items",
        "_cost_type",
        "_design",
        "_erp_project_accounting",
        "_labor_items",
        "_misc_cost_items",
        "_overhead_cost",
        "_property_units",
        "_work_cost_summary",
        "_work_task",
        "_works",
        "amount",
        "is_debit",
        "transaction_date_time",
    )

    amount: _decimal.Decimal | None  # Money
    is_debit: bool | None
    transaction_date_time: _dt.datetime | None

    erp_project_accounting: One[ErpProjectAccounting] = One(
        EndMeta(
            name="erp_project_accounting",
            cim_role="ErpProjectAccounting",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_project_accounting:ErpProjectAccounting",
            many=False,
            lower=1,
            upper=1,
            inverse="work_cost_details",
            aggregation="none",
        )
    )
    cost_type: One[CostType] = One(
        EndMeta(
            name="cost_type",
            cim_role="CostType",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.cost_type:CostType",
            many=False,
            lower=1,
            upper=1,
            inverse="work_cost_details",
            aggregation="none",
        )
    )
    work_task: One[OldWorkTask] = One(
        EndMeta(
            name="work_task",
            cim_role="WorkTask",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task:OldWorkTask",
            many=False,
            lower=0,
            upper=1,
            inverse="work_cost_details",
            aggregation="none",
        )
    )
    design: One[Design] = One(
        EndMeta(
            name="design",
            cim_role="Design",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design:Design",
            many=False,
            lower=0,
            upper=1,
            inverse="work_cost_details",
            aggregation="none",
        )
    )
    work_cost_summary: One[WorkCostSummary] = One(
        EndMeta(
            name="work_cost_summary",
            cim_role="WorkCostSummary",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_summary:WorkCostSummary",
            many=False,
            lower=0,
            upper=1,
            inverse="work_cost_detail",
            aggregation="none",
        )
    )
    labor_items: Many[LaborItem] = Many(
        EndMeta(
            name="labor_items",
            cim_role="LaborItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.labor_item:LaborItem",
            many=True,
            lower=0,
            upper=None,
            inverse="work_cost_detail",
            aggregation="none",
        )
    )
    contractor_items: Many[ContractorItem] = Many(
        EndMeta(
            name="contractor_items",
            cim_role="ContractorItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.contractor_item:ContractorItem",
            many=True,
            lower=0,
            upper=None,
            inverse="work_cost_detail",
            aggregation="none",
        )
    )
    property_units: Many[PropertyUnit] = Many(
        EndMeta(
            name="property_units",
            cim_role="PropertyUnits",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.property_unit:PropertyUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="work_cost_details",
            aggregation="none",
        )
    )
    overhead_cost: One[OverheadCost] = One(
        EndMeta(
            name="overhead_cost",
            cim_role="OverheadCost",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.overhead_cost:OverheadCost",
            many=False,
            lower=0,
            upper=1,
            inverse="work_cost_details",
            aggregation="none",
        )
    )
    works: Many[Work] = Many(
        EndMeta(
            name="works",
            cim_role="Works",
            target="cim_python_sdk.model.iec61968.work.work:Work",
            many=True,
            lower=0,
            upper=None,
            inverse="work_cost_details",
            aggregation="none",
        )
    )
    misc_cost_items: Many[MiscCostItem] = Many(
        EndMeta(
            name="misc_cost_items",
            cim_role="MiscCostItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.misc_cost_item:MiscCostItem",
            many=True,
            lower=0,
            upper=None,
            inverse="work_cost_detail",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WorkCostDetail",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{9EC4A363-1D2C-4ecf-AD53-D7122EA5FC4F}",
        attributes=(
            AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("is_debit", "isDebit", "bool", 0, 1, "primitive"),
            AttrMeta("transaction_date_time", "transactionDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            erp_project_accounting.meta,
            cost_type.meta,
            work_task.meta,
            design.meta,
            work_cost_summary.meta,
            labor_items.meta,
            contractor_items.meta,
            property_units.meta,
            overhead_cost.meta,
            works.meta,
            misc_cost_items.meta,
        ),
    )

    def __init__(
        self,
        *,
        amount: _decimal.Decimal | None = None,
        is_debit: bool | None = None,
        transaction_date_time: _dt.datetime | None = None,
        erp_project_accounting: ErpProjectAccounting | None = None,
        cost_type: CostType | None = None,
        work_task: OldWorkTask | None = None,
        design: Design | None = None,
        work_cost_summary: WorkCostSummary | None = None,
        labor_items: Iterable[LaborItem] | None = None,
        contractor_items: Iterable[ContractorItem] | None = None,
        property_units: Iterable[PropertyUnit] | None = None,
        overhead_cost: OverheadCost | None = None,
        works: Iterable[Work] | None = None,
        misc_cost_items: Iterable[MiscCostItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.amount = amount
        self.is_debit = is_debit
        self.transaction_date_time = transaction_date_time
        if erp_project_accounting is not None:
            self.erp_project_accounting = erp_project_accounting
        if cost_type is not None:
            self.cost_type = cost_type
        if work_task is not None:
            self.work_task = work_task
        if design is not None:
            self.design = design
        if work_cost_summary is not None:
            self.work_cost_summary = work_cost_summary
        if labor_items is not None:
            WorkCostDetail.labor_items.extend(self, labor_items)
        if contractor_items is not None:
            WorkCostDetail.contractor_items.extend(self, contractor_items)
        if property_units is not None:
            WorkCostDetail.property_units.extend(self, property_units)
        if overhead_cost is not None:
            self.overhead_cost = overhead_cost
        if works is not None:
            WorkCostDetail.works.extend(self, works)
        if misc_cost_items is not None:
            WorkCostDetail.misc_cost_items.extend(self, misc_cost_items)

    def add_labor_item(self, labor_item: LaborItem) -> Self:
        return WorkCostDetail.labor_items.add(self, labor_item)

    def remove_labor_item(self, labor_item: LaborItem) -> Self:
        return WorkCostDetail.labor_items.remove(self, labor_item)

    def clear_labor_items(self) -> Self:
        return WorkCostDetail.labor_items.clear(self)

    def num_labor_item(self) -> int:
        return WorkCostDetail.labor_items.count(self)

    def get_labor_item_by_mrid(self, mrid: str) -> LaborItem | None:
        return WorkCostDetail.labor_items.get_by_mrid(self, mrid)

    def add_contractor_item(self, contractor_item: ContractorItem) -> Self:
        return WorkCostDetail.contractor_items.add(self, contractor_item)

    def remove_contractor_item(self, contractor_item: ContractorItem) -> Self:
        return WorkCostDetail.contractor_items.remove(self, contractor_item)

    def clear_contractor_items(self) -> Self:
        return WorkCostDetail.contractor_items.clear(self)

    def num_contractor_item(self) -> int:
        return WorkCostDetail.contractor_items.count(self)

    def get_contractor_item_by_mrid(self, mrid: str) -> ContractorItem | None:
        return WorkCostDetail.contractor_items.get_by_mrid(self, mrid)

    def add_property_unit(self, property_unit: PropertyUnit) -> Self:
        return WorkCostDetail.property_units.add(self, property_unit)

    def remove_property_unit(self, property_unit: PropertyUnit) -> Self:
        return WorkCostDetail.property_units.remove(self, property_unit)

    def clear_property_units(self) -> Self:
        return WorkCostDetail.property_units.clear(self)

    def num_property_unit(self) -> int:
        return WorkCostDetail.property_units.count(self)

    def get_property_unit_by_mrid(self, mrid: str) -> PropertyUnit | None:
        return WorkCostDetail.property_units.get_by_mrid(self, mrid)

    def add_work(self, work: Work) -> Self:
        return WorkCostDetail.works.add(self, work)

    def remove_work(self, work: Work) -> Self:
        return WorkCostDetail.works.remove(self, work)

    def clear_works(self) -> Self:
        return WorkCostDetail.works.clear(self)

    def num_work(self) -> int:
        return WorkCostDetail.works.count(self)

    def get_work_by_mrid(self, mrid: str) -> Work | None:
        return WorkCostDetail.works.get_by_mrid(self, mrid)

    def add_misc_cost_item(self, misc_cost_item: MiscCostItem) -> Self:
        return WorkCostDetail.misc_cost_items.add(self, misc_cost_item)

    def remove_misc_cost_item(self, misc_cost_item: MiscCostItem) -> Self:
        return WorkCostDetail.misc_cost_items.remove(self, misc_cost_item)

    def clear_misc_cost_items(self) -> Self:
        return WorkCostDetail.misc_cost_items.clear(self)

    def num_misc_cost_item(self) -> int:
        return WorkCostDetail.misc_cost_items.count(self)

    def get_misc_cost_item_by_mrid(self, mrid: str) -> MiscCostItem | None:
        return WorkCostDetail.misc_cost_items.get_by_mrid(self, mrid)

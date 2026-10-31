"""CIM class WorkTask (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.work.base_work import BaseWork

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.procedure_data_set import ProcedureDataSet
    from cim_python_sdk.model.iec61968.common.crew import Crew
    from cim_python_sdk.model.iec61968.operations.switching_plan import SwitchingPlan
    from cim_python_sdk.model.iec61968.operations.trouble_order import TroubleOrder
    from cim_python_sdk.model.iec61968.work.material_item import MaterialItem
    from cim_python_sdk.model.iec61968.work.work import Work
    from cim_python_sdk.model.iec61968.work.work_task_kind import WorkTaskKind


class WorkTask(BaseWork):
    """A task within a set of work."""

    __slots__ = (
        "_assets",
        "_crews",
        "_material_items",
        "_old_asset",
        "_procedure_data_set",
        "_switching_plan",
        "_trouble_order",
        "_work",
        "completed_date_time",
        "contractor_cost",
        "crew_eta",
        "estimated_completion_time",
        "instruction",
        "labor_cost",
        "labor_hours",
        "materiall_cost",
        "sched_override",
        "started_date_time",
        "task_kind",
        "tool_cost",
    )

    task_kind: WorkTaskKind | None
    instruction: str | None
    sched_override: str | None
    crew_eta: _dt.datetime | None
    started_date_time: _dt.datetime | None
    completed_date_time: _dt.datetime | None
    labor_hours: float | None  # Hours
    contractor_cost: _decimal.Decimal | None  # Money
    labor_cost: _decimal.Decimal | None  # Money
    materiall_cost: _decimal.Decimal | None  # Money
    tool_cost: _decimal.Decimal | None  # Money
    estimated_completion_time: _dt.datetime | None

    trouble_order: One[TroubleOrder] = One(
        EndMeta(
            name="trouble_order",
            cim_role="TroubleOrder",
            target="cim_python_sdk.model.iec61968.operations.trouble_order:TroubleOrder",
            many=False,
            lower=0,
            upper=1,
            inverse="work_task",
            aggregation="none",
        )
    )
    switching_plan: One[SwitchingPlan] = One(
        EndMeta(
            name="switching_plan",
            cim_role="SwitchingPlan",
            target="cim_python_sdk.model.iec61968.operations.switching_plan:SwitchingPlan",
            many=False,
            lower=0,
            upper=1,
            inverse="work_tasks",
            aggregation="none",
        )
    )
    procedure_data_set: Many[ProcedureDataSet] = Many(
        EndMeta(
            name="procedure_data_set",
            cim_role="ProcedureDataSet",
            target="cim_python_sdk.model.iec61968.assets.procedure_data_set:ProcedureDataSet",
            many=True,
            lower=0,
            upper=None,
            inverse="work_task",
            aggregation="none",
        )
    )
    assets: Many[Asset] = Many(
        EndMeta(
            name="assets",
            cim_role="Assets",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="work_tasks",
            aggregation="none",
        )
    )
    material_items: Many[MaterialItem] = Many(
        EndMeta(
            name="material_items",
            cim_role="MaterialItems",
            target="cim_python_sdk.model.iec61968.work.material_item:MaterialItem",
            many=True,
            lower=0,
            upper=None,
            inverse="work_task",
            aggregation="none",
        )
    )
    crews: Many[Crew] = Many(
        EndMeta(
            name="crews",
            cim_role="Crews",
            target="cim_python_sdk.model.iec61968.common.crew:Crew",
            many=True,
            lower=0,
            upper=None,
            inverse="work_tasks",
            aggregation="none",
        )
    )
    old_asset: Many[Asset] = Many(
        EndMeta(
            name="old_asset",
            cim_role="OldAsset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=True,
            lower=0,
            upper=None,
            inverse="replacement_work_tasks",
            aggregation="none",
        )
    )
    work: One[Work] = One(
        EndMeta(
            name="work",
            cim_role="Work",
            target="cim_python_sdk.model.iec61968.work.work:Work",
            many=False,
            lower=1,
            upper=1,
            inverse="work_tasks",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WorkTask",
        package="TC57CIM/IEC61968/Work",
        guid="{E374758E-4AC0-4b81-9D2E-D56E1D8C5F50}",
        attributes=(
            AttrMeta("task_kind", "taskKind", "WorkTaskKind", 0, 1, "enumeration"),
            AttrMeta("instruction", "instruction", "str", 0, 1, "primitive"),
            AttrMeta("sched_override", "schedOverride", "str", 0, 1, "primitive"),
            AttrMeta("crew_eta", "crewETA", "datetime", 0, 1, "primitive"),
            AttrMeta("started_date_time", "startedDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("completed_date_time", "completedDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("labor_hours", "laborHours", "Hours", 0, 1, "cimdatatype"),
            AttrMeta("contractor_cost", "contractorCost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("labor_cost", "laborCost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("materiall_cost", "materiallCost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("tool_cost", "toolCost", "Money", 0, 1, "cimdatatype"),
            AttrMeta(
                "estimated_completion_time",
                "estimatedCompletionTime",
                "datetime",
                0,
                1,
                "primitive",
            ),
        ),
        ends=(
            trouble_order.meta,
            switching_plan.meta,
            procedure_data_set.meta,
            assets.meta,
            material_items.meta,
            crews.meta,
            old_asset.meta,
            work.meta,
        ),
    )

    def __init__(
        self,
        *,
        task_kind: WorkTaskKind | None = None,
        instruction: str | None = None,
        sched_override: str | None = None,
        crew_eta: _dt.datetime | None = None,
        started_date_time: _dt.datetime | None = None,
        completed_date_time: _dt.datetime | None = None,
        labor_hours: float | None = None,
        contractor_cost: _decimal.Decimal | None = None,
        labor_cost: _decimal.Decimal | None = None,
        materiall_cost: _decimal.Decimal | None = None,
        tool_cost: _decimal.Decimal | None = None,
        estimated_completion_time: _dt.datetime | None = None,
        trouble_order: TroubleOrder | None = None,
        switching_plan: SwitchingPlan | None = None,
        procedure_data_set: Iterable[ProcedureDataSet] | None = None,
        assets: Iterable[Asset] | None = None,
        material_items: Iterable[MaterialItem] | None = None,
        crews: Iterable[Crew] | None = None,
        old_asset: Iterable[Asset] | None = None,
        work: Work | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.task_kind = task_kind
        self.instruction = instruction
        self.sched_override = sched_override
        self.crew_eta = crew_eta
        self.started_date_time = started_date_time
        self.completed_date_time = completed_date_time
        self.labor_hours = labor_hours
        self.contractor_cost = contractor_cost
        self.labor_cost = labor_cost
        self.materiall_cost = materiall_cost
        self.tool_cost = tool_cost
        self.estimated_completion_time = estimated_completion_time
        if trouble_order is not None:
            self.trouble_order = trouble_order
        if switching_plan is not None:
            self.switching_plan = switching_plan
        if procedure_data_set is not None:
            WorkTask.procedure_data_set.extend(self, procedure_data_set)
        if assets is not None:
            WorkTask.assets.extend(self, assets)
        if material_items is not None:
            WorkTask.material_items.extend(self, material_items)
        if crews is not None:
            WorkTask.crews.extend(self, crews)
        if old_asset is not None:
            WorkTask.old_asset.extend(self, old_asset)
        if work is not None:
            self.work = work

    def add_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return WorkTask.procedure_data_set.add(self, procedure_data_set)

    def remove_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return WorkTask.procedure_data_set.remove(self, procedure_data_set)

    def clear_procedure_data_set(self) -> Self:
        return WorkTask.procedure_data_set.clear(self)

    def num_procedure_data_set(self) -> int:
        return WorkTask.procedure_data_set.count(self)

    def get_procedure_data_set_by_mrid(self, mrid: str) -> ProcedureDataSet | None:
        return WorkTask.procedure_data_set.get_by_mrid(self, mrid)

    def add_asset(self, asset: Asset) -> Self:
        return WorkTask.assets.add(self, asset)

    def remove_asset(self, asset: Asset) -> Self:
        return WorkTask.assets.remove(self, asset)

    def clear_assets(self) -> Self:
        return WorkTask.assets.clear(self)

    def num_asset(self) -> int:
        return WorkTask.assets.count(self)

    def get_asset_by_mrid(self, mrid: str) -> Asset | None:
        return WorkTask.assets.get_by_mrid(self, mrid)

    def add_material_item(self, material_item: MaterialItem) -> Self:
        return WorkTask.material_items.add(self, material_item)

    def remove_material_item(self, material_item: MaterialItem) -> Self:
        return WorkTask.material_items.remove(self, material_item)

    def clear_material_items(self) -> Self:
        return WorkTask.material_items.clear(self)

    def num_material_item(self) -> int:
        return WorkTask.material_items.count(self)

    def get_material_item_by_mrid(self, mrid: str) -> MaterialItem | None:
        return WorkTask.material_items.get_by_mrid(self, mrid)

    def add_crew(self, crew: Crew) -> Self:
        return WorkTask.crews.add(self, crew)

    def remove_crew(self, crew: Crew) -> Self:
        return WorkTask.crews.remove(self, crew)

    def clear_crews(self) -> Self:
        return WorkTask.crews.clear(self)

    def num_crew(self) -> int:
        return WorkTask.crews.count(self)

    def get_crew_by_mrid(self, mrid: str) -> Crew | None:
        return WorkTask.crews.get_by_mrid(self, mrid)

    def add_old_asset(self, old_asset: Asset) -> Self:
        return WorkTask.old_asset.add(self, old_asset)

    def remove_old_asset(self, old_asset: Asset) -> Self:
        return WorkTask.old_asset.remove(self, old_asset)

    def clear_old_asset(self) -> Self:
        return WorkTask.old_asset.clear(self)

    def num_old_asset(self) -> int:
        return WorkTask.old_asset.count(self)

    def get_old_asset_by_mrid(self, mrid: str) -> Asset | None:
        return WorkTask.old_asset.get_by_mrid(self, mrid)

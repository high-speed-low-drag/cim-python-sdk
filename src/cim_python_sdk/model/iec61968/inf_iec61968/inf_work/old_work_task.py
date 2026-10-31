"""CIM class OldWorkTask (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.work.work_task import WorkTask

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.capability import Capability
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.contractor_item import ContractorItem
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design import Design
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location_cu import (
        DesignLocationCU,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.labor_item import LaborItem
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.misc_cost_item import MiscCostItem
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.overhead_cost import OverheadCost
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.qualification_requirement import (
        QualificationRequirement,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.usage import Usage
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail import WorkCostDetail
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_flow_step import WorkFlowStep


class OldWorkTask(WorkTask):
    """A set of tasks is required to implement a design."""

    __slots__ = (
        "_capabilities",
        "_contractor_items",
        "_design",
        "_design_location_cus",
        "_labor_items",
        "_misc_cost_items",
        "_overhead_cost",
        "_qualification_requirements",
        "_usages",
        "_work_cost_details",
        "_work_flow_step",
    )

    contractor_items: Many[ContractorItem] = Many(
        EndMeta(
            name="contractor_items",
            cim_role="ContractorItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.contractor_item:ContractorItem",
            many=True,
            lower=0,
            upper=None,
            inverse="work_task",
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
            inverse="work_task",
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
            inverse="work_tasks",
            aggregation="none",
        )
    )
    capabilities: Many[Capability] = Many(
        EndMeta(
            name="capabilities",
            cim_role="Capabilities",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.capability:Capability",
            many=True,
            lower=0,
            upper=None,
            inverse="work_tasks",
            aggregation="none",
        )
    )
    usages: Many[Usage] = Many(
        EndMeta(
            name="usages",
            cim_role="Usages",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.usage:Usage",
            many=True,
            lower=0,
            upper=None,
            inverse="work_task",
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
            inverse="work_task",
            aggregation="none",
        )
    )
    qualification_requirements: Many[QualificationRequirement] = Many(
        EndMeta(
            name="qualification_requirements",
            cim_role="QualificationRequirements",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.qualification_requirement:QualificationRequirement",
            many=True,
            lower=0,
            upper=None,
            inverse="work_tasks",
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
            inverse="work_tasks",
            aggregation="none",
        )
    )
    work_flow_step: One[WorkFlowStep] = One(
        EndMeta(
            name="work_flow_step",
            cim_role="WorkFlowStep",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_flow_step:WorkFlowStep",
            many=False,
            lower=0,
            upper=1,
            inverse="work_tasks",
            aggregation="none",
        )
    )
    design_location_cus: Many[DesignLocationCU] = Many(
        EndMeta(
            name="design_location_cus",
            cim_role="DesignLocationCUs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location_cu:DesignLocationCU",
            many=True,
            lower=0,
            upper=None,
            inverse="work_tasks",
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
            inverse="work_task",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OldWorkTask",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{1C3C4B03-3764-42d0-8B12-D4E3EA08748D}",
        ends=(
            contractor_items.meta,
            work_cost_details.meta,
            design.meta,
            capabilities.meta,
            usages.meta,
            misc_cost_items.meta,
            qualification_requirements.meta,
            overhead_cost.meta,
            work_flow_step.meta,
            design_location_cus.meta,
            labor_items.meta,
        ),
    )

    def __init__(
        self,
        *,
        contractor_items: Iterable[ContractorItem] | None = None,
        work_cost_details: Iterable[WorkCostDetail] | None = None,
        design: Design | None = None,
        capabilities: Iterable[Capability] | None = None,
        usages: Iterable[Usage] | None = None,
        misc_cost_items: Iterable[MiscCostItem] | None = None,
        qualification_requirements: Iterable[QualificationRequirement] | None = None,
        overhead_cost: OverheadCost | None = None,
        work_flow_step: WorkFlowStep | None = None,
        design_location_cus: Iterable[DesignLocationCU] | None = None,
        labor_items: Iterable[LaborItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if contractor_items is not None:
            OldWorkTask.contractor_items.extend(self, contractor_items)
        if work_cost_details is not None:
            OldWorkTask.work_cost_details.extend(self, work_cost_details)
        if design is not None:
            self.design = design
        if capabilities is not None:
            OldWorkTask.capabilities.extend(self, capabilities)
        if usages is not None:
            OldWorkTask.usages.extend(self, usages)
        if misc_cost_items is not None:
            OldWorkTask.misc_cost_items.extend(self, misc_cost_items)
        if qualification_requirements is not None:
            OldWorkTask.qualification_requirements.extend(self, qualification_requirements)
        if overhead_cost is not None:
            self.overhead_cost = overhead_cost
        if work_flow_step is not None:
            self.work_flow_step = work_flow_step
        if design_location_cus is not None:
            OldWorkTask.design_location_cus.extend(self, design_location_cus)
        if labor_items is not None:
            OldWorkTask.labor_items.extend(self, labor_items)

    def add_contractor_item(self, contractor_item: ContractorItem) -> Self:
        return OldWorkTask.contractor_items.add(self, contractor_item)

    def remove_contractor_item(self, contractor_item: ContractorItem) -> Self:
        return OldWorkTask.contractor_items.remove(self, contractor_item)

    def clear_contractor_items(self) -> Self:
        return OldWorkTask.contractor_items.clear(self)

    def num_contractor_item(self) -> int:
        return OldWorkTask.contractor_items.count(self)

    def get_contractor_item_by_mrid(self, mrid: str) -> ContractorItem | None:
        return OldWorkTask.contractor_items.get_by_mrid(self, mrid)

    def add_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return OldWorkTask.work_cost_details.add(self, work_cost_detail)

    def remove_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return OldWorkTask.work_cost_details.remove(self, work_cost_detail)

    def clear_work_cost_details(self) -> Self:
        return OldWorkTask.work_cost_details.clear(self)

    def num_work_cost_detail(self) -> int:
        return OldWorkTask.work_cost_details.count(self)

    def get_work_cost_detail_by_mrid(self, mrid: str) -> WorkCostDetail | None:
        return OldWorkTask.work_cost_details.get_by_mrid(self, mrid)

    def add_capability(self, capability: Capability) -> Self:
        return OldWorkTask.capabilities.add(self, capability)

    def remove_capability(self, capability: Capability) -> Self:
        return OldWorkTask.capabilities.remove(self, capability)

    def clear_capabilities(self) -> Self:
        return OldWorkTask.capabilities.clear(self)

    def num_capability(self) -> int:
        return OldWorkTask.capabilities.count(self)

    def get_capability_by_mrid(self, mrid: str) -> Capability | None:
        return OldWorkTask.capabilities.get_by_mrid(self, mrid)

    def add_usage(self, usage: Usage) -> Self:
        return OldWorkTask.usages.add(self, usage)

    def remove_usage(self, usage: Usage) -> Self:
        return OldWorkTask.usages.remove(self, usage)

    def clear_usages(self) -> Self:
        return OldWorkTask.usages.clear(self)

    def num_usage(self) -> int:
        return OldWorkTask.usages.count(self)

    def get_usage_by_mrid(self, mrid: str) -> Usage | None:
        return OldWorkTask.usages.get_by_mrid(self, mrid)

    def add_misc_cost_item(self, misc_cost_item: MiscCostItem) -> Self:
        return OldWorkTask.misc_cost_items.add(self, misc_cost_item)

    def remove_misc_cost_item(self, misc_cost_item: MiscCostItem) -> Self:
        return OldWorkTask.misc_cost_items.remove(self, misc_cost_item)

    def clear_misc_cost_items(self) -> Self:
        return OldWorkTask.misc_cost_items.clear(self)

    def num_misc_cost_item(self) -> int:
        return OldWorkTask.misc_cost_items.count(self)

    def get_misc_cost_item_by_mrid(self, mrid: str) -> MiscCostItem | None:
        return OldWorkTask.misc_cost_items.get_by_mrid(self, mrid)

    def add_qualification_requirement(
        self, qualification_requirement: QualificationRequirement
    ) -> Self:
        return OldWorkTask.qualification_requirements.add(self, qualification_requirement)

    def remove_qualification_requirement(
        self, qualification_requirement: QualificationRequirement
    ) -> Self:
        return OldWorkTask.qualification_requirements.remove(self, qualification_requirement)

    def clear_qualification_requirements(self) -> Self:
        return OldWorkTask.qualification_requirements.clear(self)

    def num_qualification_requirement(self) -> int:
        return OldWorkTask.qualification_requirements.count(self)

    def get_qualification_requirement_by_mrid(self, mrid: str) -> QualificationRequirement | None:
        return OldWorkTask.qualification_requirements.get_by_mrid(self, mrid)

    def add_design_location_cu(self, design_location_cu: DesignLocationCU) -> Self:
        return OldWorkTask.design_location_cus.add(self, design_location_cu)

    def remove_design_location_cu(self, design_location_cu: DesignLocationCU) -> Self:
        return OldWorkTask.design_location_cus.remove(self, design_location_cu)

    def clear_design_location_cus(self) -> Self:
        return OldWorkTask.design_location_cus.clear(self)

    def num_design_location_cu(self) -> int:
        return OldWorkTask.design_location_cus.count(self)

    def get_design_location_cu_by_mrid(self, mrid: str) -> DesignLocationCU | None:
        return OldWorkTask.design_location_cus.get_by_mrid(self, mrid)

    def add_labor_item(self, labor_item: LaborItem) -> Self:
        return OldWorkTask.labor_items.add(self, labor_item)

    def remove_labor_item(self, labor_item: LaborItem) -> Self:
        return OldWorkTask.labor_items.remove(self, labor_item)

    def clear_labor_items(self) -> Self:
        return OldWorkTask.labor_items.clear(self)

    def num_labor_item(self) -> int:
        return OldWorkTask.labor_items.count(self)

    def get_labor_item_by_mrid(self, mrid: str) -> LaborItem | None:
        return OldWorkTask.labor_items.get_by_mrid(self, mrid)

"""CIM class Design (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_bom import ErpBOM
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote_line_item import (
        ErpQuoteLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.condition_factor import ConditionFactor
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_kind import DesignKind
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location import DesignLocation
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location_cu import (
        DesignLocationCU,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.old_work_task import OldWorkTask
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_cost_detail import WorkCostDetail
    from cim_python_sdk.model.iec61968.work.work import Work


class Design(WorkDocument):
    """A design for consideration by customers, potential customers, or internal work.

    Note that the Version of design is the revision attribute that is inherited from
    Document."""

    __slots__ = (
        "_condition_factors",
        "_design_locations",
        "_design_locations_cus",
        "_erp_boms",
        "_erp_quote_line_item",
        "_work",
        "_work_cost_details",
        "_work_tasks",
        "cost_estimate",
        "kind",
        "price",
    )

    kind: DesignKind | None
    price: _decimal.Decimal | None  # Money
    cost_estimate: _decimal.Decimal | None  # Money

    erp_boms: Many[ErpBOM] = Many(
        EndMeta(
            name="erp_boms",
            cim_role="ErpBOMs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_bom:ErpBOM",
            many=True,
            lower=0,
            upper=None,
            inverse="design",
            aggregation="none",
        )
    )
    design_locations_cus: Many[DesignLocationCU] = Many(
        EndMeta(
            name="design_locations_cus",
            cim_role="DesignLocationsCUs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location_cu:DesignLocationCU",
            many=True,
            lower=0,
            upper=None,
            inverse="designs",
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
            inverse="design",
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
            inverse="design",
            aggregation="none",
        )
    )
    design_locations: Many[DesignLocation] = Many(
        EndMeta(
            name="design_locations",
            cim_role="DesignLocations",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location:DesignLocation",
            many=True,
            lower=0,
            upper=None,
            inverse="designs",
            aggregation="none",
        )
    )
    work: One[Work] = One(
        EndMeta(
            name="work",
            cim_role="Work",
            target="cim_python_sdk.model.iec61968.work.work:Work",
            many=False,
            lower=0,
            upper=1,
            inverse="designs",
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
            inverse="designs",
            aggregation="none",
        )
    )
    erp_quote_line_item: One[ErpQuoteLineItem] = One(
        EndMeta(
            name="erp_quote_line_item",
            cim_role="ErpQuoteLineItem",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_quote_line_item:ErpQuoteLineItem",
            many=False,
            lower=0,
            upper=1,
            inverse="design",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Design",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{1D7DF3D9-EF02-4551-8494-AE5B859270CE}",
        attributes=(
            AttrMeta("kind", "kind", "DesignKind", 0, 1, "enumeration"),
            AttrMeta("price", "price", "Money", 0, 1, "cimdatatype"),
            AttrMeta("cost_estimate", "costEstimate", "Money", 0, 1, "cimdatatype"),
        ),
        ends=(
            erp_boms.meta,
            design_locations_cus.meta,
            work_cost_details.meta,
            work_tasks.meta,
            design_locations.meta,
            work.meta,
            condition_factors.meta,
            erp_quote_line_item.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: DesignKind | None = None,
        price: _decimal.Decimal | None = None,
        cost_estimate: _decimal.Decimal | None = None,
        erp_boms: Iterable[ErpBOM] | None = None,
        design_locations_cus: Iterable[DesignLocationCU] | None = None,
        work_cost_details: Iterable[WorkCostDetail] | None = None,
        work_tasks: Iterable[OldWorkTask] | None = None,
        design_locations: Iterable[DesignLocation] | None = None,
        work: Work | None = None,
        condition_factors: Iterable[ConditionFactor] | None = None,
        erp_quote_line_item: ErpQuoteLineItem | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.price = price
        self.cost_estimate = cost_estimate
        if erp_boms is not None:
            Design.erp_boms.extend(self, erp_boms)
        if design_locations_cus is not None:
            Design.design_locations_cus.extend(self, design_locations_cus)
        if work_cost_details is not None:
            Design.work_cost_details.extend(self, work_cost_details)
        if work_tasks is not None:
            Design.work_tasks.extend(self, work_tasks)
        if design_locations is not None:
            Design.design_locations.extend(self, design_locations)
        if work is not None:
            self.work = work
        if condition_factors is not None:
            Design.condition_factors.extend(self, condition_factors)
        if erp_quote_line_item is not None:
            self.erp_quote_line_item = erp_quote_line_item

    def add_erp_bom(self, erp_bom: ErpBOM) -> Self:
        return Design.erp_boms.add(self, erp_bom)

    def remove_erp_bom(self, erp_bom: ErpBOM) -> Self:
        return Design.erp_boms.remove(self, erp_bom)

    def clear_erp_boms(self) -> Self:
        return Design.erp_boms.clear(self)

    def num_erp_bom(self) -> int:
        return Design.erp_boms.count(self)

    def get_erp_bom_by_mrid(self, mrid: str) -> ErpBOM | None:
        return Design.erp_boms.get_by_mrid(self, mrid)

    def add_design_locations_cu(self, design_locations_cu: DesignLocationCU) -> Self:
        return Design.design_locations_cus.add(self, design_locations_cu)

    def remove_design_locations_cu(self, design_locations_cu: DesignLocationCU) -> Self:
        return Design.design_locations_cus.remove(self, design_locations_cu)

    def clear_design_locations_cus(self) -> Self:
        return Design.design_locations_cus.clear(self)

    def num_design_locations_cu(self) -> int:
        return Design.design_locations_cus.count(self)

    def get_design_locations_cu_by_mrid(self, mrid: str) -> DesignLocationCU | None:
        return Design.design_locations_cus.get_by_mrid(self, mrid)

    def add_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return Design.work_cost_details.add(self, work_cost_detail)

    def remove_work_cost_detail(self, work_cost_detail: WorkCostDetail) -> Self:
        return Design.work_cost_details.remove(self, work_cost_detail)

    def clear_work_cost_details(self) -> Self:
        return Design.work_cost_details.clear(self)

    def num_work_cost_detail(self) -> int:
        return Design.work_cost_details.count(self)

    def get_work_cost_detail_by_mrid(self, mrid: str) -> WorkCostDetail | None:
        return Design.work_cost_details.get_by_mrid(self, mrid)

    def add_work_task(self, work_task: OldWorkTask) -> Self:
        return Design.work_tasks.add(self, work_task)

    def remove_work_task(self, work_task: OldWorkTask) -> Self:
        return Design.work_tasks.remove(self, work_task)

    def clear_work_tasks(self) -> Self:
        return Design.work_tasks.clear(self)

    def num_work_task(self) -> int:
        return Design.work_tasks.count(self)

    def get_work_task_by_mrid(self, mrid: str) -> OldWorkTask | None:
        return Design.work_tasks.get_by_mrid(self, mrid)

    def add_design_location(self, design_location: DesignLocation) -> Self:
        return Design.design_locations.add(self, design_location)

    def remove_design_location(self, design_location: DesignLocation) -> Self:
        return Design.design_locations.remove(self, design_location)

    def clear_design_locations(self) -> Self:
        return Design.design_locations.clear(self)

    def num_design_location(self) -> int:
        return Design.design_locations.count(self)

    def get_design_location_by_mrid(self, mrid: str) -> DesignLocation | None:
        return Design.design_locations.get_by_mrid(self, mrid)

    def add_condition_factor(self, condition_factor: ConditionFactor) -> Self:
        return Design.condition_factors.add(self, condition_factor)

    def remove_condition_factor(self, condition_factor: ConditionFactor) -> Self:
        return Design.condition_factors.remove(self, condition_factor)

    def clear_condition_factors(self) -> Self:
        return Design.condition_factors.clear(self)

    def num_condition_factor(self) -> int:
        return Design.condition_factors.count(self)

    def get_condition_factor_by_mrid(self, mrid: str) -> ConditionFactor | None:
        return Design.condition_factors.get_by_mrid(self, mrid)

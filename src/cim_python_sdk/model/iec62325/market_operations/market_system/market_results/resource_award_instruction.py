"""CIM class ResourceAwardInstruction (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_plan.market_product import (
        MarketProduct,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_clearing import (
        ResourceAwardClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.self_schedule_breakdown import (
        SelfScheduleBreakdown,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqschg_type import MQSCHGType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class ResourceAwardInstruction(CimObject):
    """Model of market results, instruction for resource. Contains details of award as
    attributes."""

    __slots__ = (
        "_clearing_resource_award",
        "_market_product",
        "_registered_resource",
        "_self_schedule_breakdown",
        "award_mw",
        "cleared_mw",
        "cleared_price",
        "congest_lmp",
        "cost_lmp",
        "dispatcher_added_mw",
        "economic_max",
        "economic_min",
        "eff_regulation_down_limit",
        "eff_regulation_up_limit",
        "lmp",
        "loss_lmp",
        "manually_blocked",
        "marginal_resource_indicator",
        "must_run_ind",
        "no_load_cost",
        "optimal_bid_cost",
        "optimal_bid_pay",
        "optimal_margin",
        "override_time_stamp",
        "override_value",
        "self_sched_mw",
        "start_up_cost",
        "status",
        "total_revenue",
        "update_time_stamp",
        "update_type",
        "update_user",
    )

    award_mw: float | None
    cleared_mw: float | None
    cleared_price: float | None
    congest_lmp: float | None
    cost_lmp: float | None
    dispatcher_added_mw: float | None
    economic_max: float | None
    economic_min: float | None
    eff_regulation_down_limit: float | None
    eff_regulation_up_limit: float | None
    lmp: float | None
    loss_lmp: float | None
    manually_blocked: YesNo | None
    marginal_resource_indicator: YesNo | None
    must_run_ind: bool | None
    no_load_cost: float | None
    optimal_bid_cost: float | None
    optimal_bid_pay: float | None
    optimal_margin: float | None
    override_time_stamp: _dt.datetime | None
    override_value: float | None
    self_sched_mw: float | None
    start_up_cost: float | None
    status: str | None
    total_revenue: float | None
    update_time_stamp: _dt.datetime | None
    update_type: MQSCHGType | None
    update_user: str | None

    self_schedule_breakdown: Many[SelfScheduleBreakdown] = Many(
        EndMeta(
            name="self_schedule_breakdown",
            cim_role="SelfScheduleBreakdown",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.self_schedule_breakdown:SelfScheduleBreakdown",
            many=True,
            lower=0,
            upper=None,
            inverse="resource_award_instruction",
            aggregation="none",
        )
    )
    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="resource_award_instruction",
            aggregation="none",
        )
    )
    clearing_resource_award: Many[ResourceAwardClearing] = Many(
        EndMeta(
            name="clearing_resource_award",
            cim_role="ClearingResourceAward",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_award_clearing:ResourceAwardClearing",
            many=True,
            lower=1,
            upper=None,
            inverse="resource_award_instruction",
            aggregation="none",
        )
    )
    market_product: One[MarketProduct] = One(
        EndMeta(
            name="market_product",
            cim_role="MarketProduct",
            target="cim_python_sdk.model.iec62325.market_operations.market_plan.market_product:MarketProduct",
            many=False,
            lower=1,
            upper=1,
            inverse="resource_award_instruction",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceAwardInstruction",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{A4F2E108-DA91-4903-8D23-6C657C7E014E}",
        attributes=(
            AttrMeta("award_mw", "awardMW", "float", 0, 1, "primitive"),
            AttrMeta("cleared_mw", "clearedMW", "float", 0, 1, "primitive"),
            AttrMeta("cleared_price", "clearedPrice", "float", 0, 1, "primitive"),
            AttrMeta("congest_lmp", "congestLMP", "float", 0, 1, "primitive"),
            AttrMeta("cost_lmp", "costLMP", "float", 0, 1, "primitive"),
            AttrMeta("dispatcher_added_mw", "dispatcherAddedMW", "float", 0, 1, "primitive"),
            AttrMeta("economic_max", "economicMax", "float", 0, 1, "primitive"),
            AttrMeta("economic_min", "economicMin", "float", 0, 1, "primitive"),
            AttrMeta(
                "eff_regulation_down_limit", "effRegulationDownLimit", "float", 0, 1, "primitive"
            ),
            AttrMeta("eff_regulation_up_limit", "effRegulationUpLimit", "float", 0, 1, "primitive"),
            AttrMeta("lmp", "lmp", "float", 0, 1, "primitive"),
            AttrMeta("loss_lmp", "lossLMP", "float", 0, 1, "primitive"),
            AttrMeta("manually_blocked", "manuallyBlocked", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "marginal_resource_indicator",
                "marginalResourceIndicator",
                "YesNo",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("must_run_ind", "mustRunInd", "bool", 0, 1, "primitive"),
            AttrMeta("no_load_cost", "noLoadCost", "float", 0, 1, "primitive"),
            AttrMeta("optimal_bid_cost", "optimalBidCost", "float", 0, 1, "primitive"),
            AttrMeta("optimal_bid_pay", "optimalBidPay", "float", 0, 1, "primitive"),
            AttrMeta("optimal_margin", "optimalMargin", "float", 0, 1, "primitive"),
            AttrMeta("override_time_stamp", "overrideTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("override_value", "overrideValue", "float", 0, 1, "primitive"),
            AttrMeta("self_sched_mw", "selfSchedMW", "float", 0, 1, "primitive"),
            AttrMeta("start_up_cost", "startUpCost", "float", 0, 1, "primitive"),
            AttrMeta("status", "status", "str", 0, 1, "primitive"),
            AttrMeta("total_revenue", "totalRevenue", "float", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_type", "updateType", "MQSCHGType", 0, 1, "enumeration"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
        ),
        ends=(
            self_schedule_breakdown.meta,
            registered_resource.meta,
            clearing_resource_award.meta,
            market_product.meta,
        ),
    )

    def __init__(
        self,
        *,
        award_mw: float | None = None,
        cleared_mw: float | None = None,
        cleared_price: float | None = None,
        congest_lmp: float | None = None,
        cost_lmp: float | None = None,
        dispatcher_added_mw: float | None = None,
        economic_max: float | None = None,
        economic_min: float | None = None,
        eff_regulation_down_limit: float | None = None,
        eff_regulation_up_limit: float | None = None,
        lmp: float | None = None,
        loss_lmp: float | None = None,
        manually_blocked: YesNo | None = None,
        marginal_resource_indicator: YesNo | None = None,
        must_run_ind: bool | None = None,
        no_load_cost: float | None = None,
        optimal_bid_cost: float | None = None,
        optimal_bid_pay: float | None = None,
        optimal_margin: float | None = None,
        override_time_stamp: _dt.datetime | None = None,
        override_value: float | None = None,
        self_sched_mw: float | None = None,
        start_up_cost: float | None = None,
        status: str | None = None,
        total_revenue: float | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_type: MQSCHGType | None = None,
        update_user: str | None = None,
        self_schedule_breakdown: Iterable[SelfScheduleBreakdown] | None = None,
        registered_resource: RegisteredResource | None = None,
        clearing_resource_award: Iterable[ResourceAwardClearing] | None = None,
        market_product: MarketProduct | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.award_mw = award_mw
        self.cleared_mw = cleared_mw
        self.cleared_price = cleared_price
        self.congest_lmp = congest_lmp
        self.cost_lmp = cost_lmp
        self.dispatcher_added_mw = dispatcher_added_mw
        self.economic_max = economic_max
        self.economic_min = economic_min
        self.eff_regulation_down_limit = eff_regulation_down_limit
        self.eff_regulation_up_limit = eff_regulation_up_limit
        self.lmp = lmp
        self.loss_lmp = loss_lmp
        self.manually_blocked = manually_blocked
        self.marginal_resource_indicator = marginal_resource_indicator
        self.must_run_ind = must_run_ind
        self.no_load_cost = no_load_cost
        self.optimal_bid_cost = optimal_bid_cost
        self.optimal_bid_pay = optimal_bid_pay
        self.optimal_margin = optimal_margin
        self.override_time_stamp = override_time_stamp
        self.override_value = override_value
        self.self_sched_mw = self_sched_mw
        self.start_up_cost = start_up_cost
        self.status = status
        self.total_revenue = total_revenue
        self.update_time_stamp = update_time_stamp
        self.update_type = update_type
        self.update_user = update_user
        if self_schedule_breakdown is not None:
            ResourceAwardInstruction.self_schedule_breakdown.extend(self, self_schedule_breakdown)
        if registered_resource is not None:
            self.registered_resource = registered_resource
        if clearing_resource_award is not None:
            ResourceAwardInstruction.clearing_resource_award.extend(self, clearing_resource_award)
        if market_product is not None:
            self.market_product = market_product

    def add_self_schedule_breakdown(self, self_schedule_breakdown: SelfScheduleBreakdown) -> Self:
        return ResourceAwardInstruction.self_schedule_breakdown.add(self, self_schedule_breakdown)

    def remove_self_schedule_breakdown(
        self, self_schedule_breakdown: SelfScheduleBreakdown
    ) -> Self:
        return ResourceAwardInstruction.self_schedule_breakdown.remove(
            self, self_schedule_breakdown
        )

    def clear_self_schedule_breakdown(self) -> Self:
        return ResourceAwardInstruction.self_schedule_breakdown.clear(self)

    def num_self_schedule_breakdown(self) -> int:
        return ResourceAwardInstruction.self_schedule_breakdown.count(self)

    def add_clearing_resource_award(self, clearing_resource_award: ResourceAwardClearing) -> Self:
        return ResourceAwardInstruction.clearing_resource_award.add(self, clearing_resource_award)

    def remove_clearing_resource_award(
        self, clearing_resource_award: ResourceAwardClearing
    ) -> Self:
        return ResourceAwardInstruction.clearing_resource_award.remove(
            self, clearing_resource_award
        )

    def clear_clearing_resource_award(self) -> Self:
        return ResourceAwardInstruction.clearing_resource_award.clear(self)

    def num_clearing_resource_award(self) -> int:
        return ResourceAwardInstruction.clearing_resource_award.count(self)

    def get_clearing_resource_award_by_mrid(self, mrid: str) -> ResourceAwardClearing | None:
        return ResourceAwardInstruction.clearing_resource_award.get_by_mrid(self, mrid)

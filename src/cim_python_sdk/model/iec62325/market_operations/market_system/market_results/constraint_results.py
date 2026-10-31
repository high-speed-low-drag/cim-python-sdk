"""CIM class ConstraintResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.constraint_clearing import (
        ConstraintClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.constraint_limit_type import (
        ConstraintLimitType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqschg_type import MQSCHGType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.results_constraint_type import (
        ResultsConstraintType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_contingency import (
        MktContingency,
    )


class ConstraintResults(IdentifiedObject):
    """Provides the Market results for the constraint processing for either the DAM or RTM. The
    data includes the constraint type (binding or violated), the solved value for the
    constraint, and the associated shadow price."""

    __slots__ = (
        "_constraint_clearing",
        "_flowgate",
        "_mkt_contingency",
        "base_flow",
        "bg_limit",
        "bgtr_res_cap",
        "binding_limit",
        "cleared_value",
        "competitive_path_constraint",
        "constraint_type",
        "limit_flag",
        "optimization_flag",
        "overload_mw",
        "percent_mw",
        "shadow_price",
        "update_time_stamp",
        "update_type",
        "update_user",
    )

    base_flow: float | None
    bg_limit: float | None
    bgtr_res_cap: float | None
    binding_limit: float | None
    cleared_value: float | None
    competitive_path_constraint: YesNo | None
    constraint_type: ResultsConstraintType | None
    limit_flag: ConstraintLimitType | None
    optimization_flag: YesNo | None
    overload_mw: float | None
    percent_mw: float | None
    shadow_price: float | None
    update_time_stamp: _dt.datetime | None
    update_type: MQSCHGType | None
    update_user: str | None

    mkt_contingency: One[MktContingency] = One(
        EndMeta(
            name="mkt_contingency",
            cim_role="MktContingency",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_contingency:MktContingency",
            many=False,
            lower=1,
            upper=1,
            inverse="constraint_results",
            aggregation="none",
        )
    )
    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=1,
            upper=1,
            inverse="constraint_results",
            aggregation="none",
        )
    )
    constraint_clearing: One[ConstraintClearing] = One(
        EndMeta(
            name="constraint_clearing",
            cim_role="ConstraintClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.constraint_clearing:ConstraintClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="constraint_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConstraintResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{0B55B70E-F2A8-44b3-B9AE-18BCCB922A17}",
        attributes=(
            AttrMeta("base_flow", "baseFlow", "float", 0, 1, "primitive"),
            AttrMeta("bg_limit", "BGLimit", "float", 0, 1, "primitive"),
            AttrMeta("bgtr_res_cap", "BGTRResCap", "float", 0, 1, "primitive"),
            AttrMeta("binding_limit", "bindingLimit", "float", 0, 1, "primitive"),
            AttrMeta("cleared_value", "clearedValue", "float", 0, 1, "primitive"),
            AttrMeta(
                "competitive_path_constraint",
                "competitivePathConstraint",
                "YesNo",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "constraint_type", "constraintType", "ResultsConstraintType", 0, 1, "enumeration"
            ),
            AttrMeta("limit_flag", "limitFlag", "ConstraintLimitType", 0, 1, "enumeration"),
            AttrMeta("optimization_flag", "optimizationFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("overload_mw", "overloadMW", "float", 0, 1, "primitive"),
            AttrMeta("percent_mw", "percentMW", "float", 0, 1, "primitive"),
            AttrMeta("shadow_price", "shadowPrice", "float", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_type", "updateType", "MQSCHGType", 0, 1, "enumeration"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
        ),
        ends=(
            mkt_contingency.meta,
            flowgate.meta,
            constraint_clearing.meta,
        ),
    )

    def __init__(
        self,
        *,
        base_flow: float | None = None,
        bg_limit: float | None = None,
        bgtr_res_cap: float | None = None,
        binding_limit: float | None = None,
        cleared_value: float | None = None,
        competitive_path_constraint: YesNo | None = None,
        constraint_type: ResultsConstraintType | None = None,
        limit_flag: ConstraintLimitType | None = None,
        optimization_flag: YesNo | None = None,
        overload_mw: float | None = None,
        percent_mw: float | None = None,
        shadow_price: float | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_type: MQSCHGType | None = None,
        update_user: str | None = None,
        mkt_contingency: MktContingency | None = None,
        flowgate: Flowgate | None = None,
        constraint_clearing: ConstraintClearing | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.base_flow = base_flow
        self.bg_limit = bg_limit
        self.bgtr_res_cap = bgtr_res_cap
        self.binding_limit = binding_limit
        self.cleared_value = cleared_value
        self.competitive_path_constraint = competitive_path_constraint
        self.constraint_type = constraint_type
        self.limit_flag = limit_flag
        self.optimization_flag = optimization_flag
        self.overload_mw = overload_mw
        self.percent_mw = percent_mw
        self.shadow_price = shadow_price
        self.update_time_stamp = update_time_stamp
        self.update_type = update_type
        self.update_user = update_user
        if mkt_contingency is not None:
            self.mkt_contingency = mkt_contingency
        if flowgate is not None:
            self.flowgate = flowgate
        if constraint_clearing is not None:
            self.constraint_clearing = constraint_clearing

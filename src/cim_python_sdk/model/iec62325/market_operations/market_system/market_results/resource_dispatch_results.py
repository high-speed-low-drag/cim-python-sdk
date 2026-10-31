"""CIM class ResourceDispatchResults (TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_clearing import (
        ResourceClearing,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.mqschg_type import MQSCHGType
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo


class ResourceDispatchResults(CimObject):
    """The ResourceDispatchResults class provides market results that can be provided to a SC.
    The specific data provided consists of several indicators such as contingency flags,
    blocked start up, and RMR dispatch. It also provides the projected overall and the
    regulating status of the resource."""

    __slots__ = (
        "_registered_resource",
        "_resource_clearing",
        "blocked_dispatch",
        "blocked_publish_dop",
        "contingency_flag",
        "limit_indicator",
        "lower_limit",
        "max_ramp_rate",
        "operating_limit_high",
        "operating_limit_low",
        "penalty_dispatch_indicator",
        "regulating_limit_high",
        "regulating_limit_low",
        "resource_status",
        "total_schedule",
        "update_time_stamp",
        "update_type",
        "update_user",
        "upper_limit",
    )

    blocked_dispatch: str | None
    blocked_publish_dop: str | None
    contingency_flag: YesNo | None
    limit_indicator: str | None
    lower_limit: float | None
    max_ramp_rate: float | None
    operating_limit_high: float | None
    operating_limit_low: float | None
    penalty_dispatch_indicator: YesNo | None
    regulating_limit_high: float | None
    regulating_limit_low: float | None
    resource_status: str | None
    total_schedule: float | None
    update_time_stamp: _dt.datetime | None
    update_type: MQSCHGType | None
    update_user: str | None
    upper_limit: float | None

    resource_clearing: One[ResourceClearing] = One(
        EndMeta(
            name="resource_clearing",
            cim_role="ResourceClearing",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.resource_clearing:ResourceClearing",
            many=False,
            lower=0,
            upper=1,
            inverse="resource_dispatch_results",
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
            inverse="resource_dispatch_results",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceDispatchResults",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/MarketResults",
        guid="{376A011D-B48B-4989-BAC1-510269091E2B}",
        attributes=(
            AttrMeta("blocked_dispatch", "blockedDispatch", "str", 0, 1, "primitive"),
            AttrMeta("blocked_publish_dop", "blockedPublishDOP", "str", 0, 1, "primitive"),
            AttrMeta("contingency_flag", "contingencyFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("limit_indicator", "limitIndicator", "str", 0, 1, "primitive"),
            AttrMeta("lower_limit", "lowerLimit", "float", 0, 1, "primitive"),
            AttrMeta("max_ramp_rate", "maxRampRate", "float", 0, 1, "primitive"),
            AttrMeta("operating_limit_high", "operatingLimitHigh", "float", 0, 1, "primitive"),
            AttrMeta("operating_limit_low", "operatingLimitLow", "float", 0, 1, "primitive"),
            AttrMeta(
                "penalty_dispatch_indicator",
                "penaltyDispatchIndicator",
                "YesNo",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("regulating_limit_high", "regulatingLimitHigh", "float", 0, 1, "primitive"),
            AttrMeta("regulating_limit_low", "regulatingLimitLow", "float", 0, 1, "primitive"),
            AttrMeta("resource_status", "resourceStatus", "str", 0, 1, "primitive"),
            AttrMeta("total_schedule", "totalSchedule", "float", 0, 1, "primitive"),
            AttrMeta("update_time_stamp", "updateTimeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("update_type", "updateType", "MQSCHGType", 0, 1, "enumeration"),
            AttrMeta("update_user", "updateUser", "str", 0, 1, "primitive"),
            AttrMeta("upper_limit", "upperLimit", "float", 0, 1, "primitive"),
        ),
        ends=(
            resource_clearing.meta,
            registered_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        blocked_dispatch: str | None = None,
        blocked_publish_dop: str | None = None,
        contingency_flag: YesNo | None = None,
        limit_indicator: str | None = None,
        lower_limit: float | None = None,
        max_ramp_rate: float | None = None,
        operating_limit_high: float | None = None,
        operating_limit_low: float | None = None,
        penalty_dispatch_indicator: YesNo | None = None,
        regulating_limit_high: float | None = None,
        regulating_limit_low: float | None = None,
        resource_status: str | None = None,
        total_schedule: float | None = None,
        update_time_stamp: _dt.datetime | None = None,
        update_type: MQSCHGType | None = None,
        update_user: str | None = None,
        upper_limit: float | None = None,
        resource_clearing: ResourceClearing | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.blocked_dispatch = blocked_dispatch
        self.blocked_publish_dop = blocked_publish_dop
        self.contingency_flag = contingency_flag
        self.limit_indicator = limit_indicator
        self.lower_limit = lower_limit
        self.max_ramp_rate = max_ramp_rate
        self.operating_limit_high = operating_limit_high
        self.operating_limit_low = operating_limit_low
        self.penalty_dispatch_indicator = penalty_dispatch_indicator
        self.regulating_limit_high = regulating_limit_high
        self.regulating_limit_low = regulating_limit_low
        self.resource_status = resource_status
        self.total_schedule = total_schedule
        self.update_time_stamp = update_time_stamp
        self.update_type = update_type
        self.update_user = update_user
        self.upper_limit = upper_limit
        if resource_clearing is not None:
            self.resource_clearing = resource_clearing
        if registered_resource is not None:
            self.registered_resource = registered_resource

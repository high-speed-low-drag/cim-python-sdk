"""CIM class RegisteredControllableLoad (TC57CIM/IEC62325/InfIEC62325/InfReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class RegisteredControllableLoad(CimObject):
    """Temporary holding for load reduction attributes removed from RegisteredLoad. Use for
    future use case when developing the RegisteredDistributedResource specialized classes."""

    __slots__ = (
        "max_base_load",
        "max_deployment_time",
        "max_load_red_times_per_day",
        "max_load_reduction",
        "max_reduction_time",
        "max_weekly_deployment",
        "min_load_reduction",
        "min_load_reduction_cost",
        "min_load_reduction_interval",
        "min_reduction_time",
        "min_time_bet_load_red",
        "req_notice_time",
    )

    max_base_load: float | None  # ActivePower
    max_deployment_time: float | None
    max_load_red_times_per_day: int | None
    max_load_reduction: float | None  # ActivePower
    max_reduction_time: float | None
    max_weekly_deployment: int | None
    min_load_reduction: float | None  # ActivePower
    min_load_reduction_cost: float | None  # CostPerEnergyUnit
    min_load_reduction_interval: float | None
    min_reduction_time: float | None
    min_time_bet_load_red: float | None
    req_notice_time: float | None

    _cim_meta = ClassMeta(
        cim_name="RegisteredControllableLoad",
        package="TC57CIM/IEC62325/InfIEC62325/InfReferenceData",
        guid="{7455916E-A376-4f1e-B9CC-E5FD90AB37CB}",
        attributes=(
            AttrMeta("max_base_load", "maxBaseLoad", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_deployment_time", "maxDeploymentTime", "float", 0, 1, "primitive"),
            AttrMeta(
                "max_load_red_times_per_day", "maxLoadRedTimesPerDay", "int", 0, 1, "primitive"
            ),
            AttrMeta("max_load_reduction", "maxLoadReduction", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_reduction_time", "maxReductionTime", "float", 0, 1, "primitive"),
            AttrMeta("max_weekly_deployment", "maxWeeklyDeployment", "int", 0, 1, "primitive"),
            AttrMeta("min_load_reduction", "minLoadReduction", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta(
                "min_load_reduction_cost",
                "minLoadReductionCost",
                "CostPerEnergyUnit",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta(
                "min_load_reduction_interval",
                "minLoadReductionInterval",
                "float",
                0,
                1,
                "primitive",
            ),
            AttrMeta("min_reduction_time", "minReductionTime", "float", 0, 1, "primitive"),
            AttrMeta("min_time_bet_load_red", "minTimeBetLoadRed", "float", 0, 1, "primitive"),
            AttrMeta("req_notice_time", "reqNoticeTime", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        max_base_load: float | None = None,
        max_deployment_time: float | None = None,
        max_load_red_times_per_day: int | None = None,
        max_load_reduction: float | None = None,
        max_reduction_time: float | None = None,
        max_weekly_deployment: int | None = None,
        min_load_reduction: float | None = None,
        min_load_reduction_cost: float | None = None,
        min_load_reduction_interval: float | None = None,
        min_reduction_time: float | None = None,
        min_time_bet_load_red: float | None = None,
        req_notice_time: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.max_base_load = max_base_load
        self.max_deployment_time = max_deployment_time
        self.max_load_red_times_per_day = max_load_red_times_per_day
        self.max_load_reduction = max_load_reduction
        self.max_reduction_time = max_reduction_time
        self.max_weekly_deployment = max_weekly_deployment
        self.min_load_reduction = min_load_reduction
        self.min_load_reduction_cost = min_load_reduction_cost
        self.min_load_reduction_interval = min_load_reduction_interval
        self.min_reduction_time = min_reduction_time
        self.min_time_bet_load_red = min_time_bet_load_red
        self.req_notice_time = req_notice_time

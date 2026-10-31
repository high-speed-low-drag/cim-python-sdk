"""CIM class GeneratingBid (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.resource_bid import (
    ResourceBid,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraints import (
        SecurityConstraints,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_set import (
        BidSet,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.notification_time_curve import (
        NotificationTimeCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.ramp_rate_curve import (
        RampRateCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.start_up_cost_curve import (
        StartUpCostCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.start_up_time_curve import (
        StartUpTimeCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator import (
        RegisteredGenerator,
    )


class GeneratingBid(ResourceBid):
    """Offer to supply energy/ancillary services from a generating unit or resource."""

    __slots__ = (
        "_bid_set",
        "_notification_time_curve",
        "_ramp_rate_curve",
        "_registered_generator",
        "_security_constraints",
        "_start_up_cost_curve",
        "_start_up_time_curve",
        "combined_cycle_unit_offer",
        "down_time_max",
        "installed_capacity",
        "lower_ramp_rate",
        "max_emergency_mw",
        "maximum_economic_mw",
        "min_emergency_mw",
        "minimum_economic_mw",
        "no_load_cost",
        "notification_time",
        "operating_mode",
        "raise_ramp_rate",
        "ramp_curve_type",
        "start_up_ramp_rate",
        "start_up_type",
        "startup_cost",
        "up_time_max",
    )

    combined_cycle_unit_offer: str | None
    down_time_max: float | None
    installed_capacity: float | None
    lower_ramp_rate: float | None  # ActivePowerChangeRate
    max_emergency_mw: float | None  # ActivePower
    maximum_economic_mw: float | None
    min_emergency_mw: float | None  # ActivePower
    minimum_economic_mw: float | None
    no_load_cost: float | None
    notification_time: float | None
    operating_mode: str | None
    raise_ramp_rate: float | None  # ActivePowerChangeRate
    ramp_curve_type: int | None
    startup_cost: float | None
    start_up_ramp_rate: float | None  # ActivePowerChangeRate
    start_up_type: int | None
    up_time_max: float | None

    start_up_cost_curve: One[StartUpCostCurve] = One(
        EndMeta(
            name="start_up_cost_curve",
            cim_role="StartUpCostCurve",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.start_up_cost_curve:StartUpCostCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="generating_bid",
            aggregation="none",
        )
    )
    start_up_time_curve: One[StartUpTimeCurve] = One(
        EndMeta(
            name="start_up_time_curve",
            cim_role="StartUpTimeCurve",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.start_up_time_curve:StartUpTimeCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="generating_bid",
            aggregation="none",
        )
    )
    notification_time_curve: One[NotificationTimeCurve] = One(
        EndMeta(
            name="notification_time_curve",
            cim_role="NotificationTimeCurve",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.notification_time_curve:NotificationTimeCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="generating_bids",
            aggregation="none",
        )
    )
    ramp_rate_curve: Many[RampRateCurve] = Many(
        EndMeta(
            name="ramp_rate_curve",
            cim_role="RampRateCurve",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.ramp_rate_curve:RampRateCurve",
            many=True,
            lower=0,
            upper=None,
            inverse="generating_bid",
            aggregation="none",
        )
    )
    registered_generator: One[RegisteredGenerator] = One(
        EndMeta(
            name="registered_generator",
            cim_role="RegisteredGenerator",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.registered_generator:RegisteredGenerator",
            many=False,
            lower=0,
            upper=1,
            inverse="generating_bids",
            aggregation="none",
        )
    )
    bid_set: One[BidSet] = One(
        EndMeta(
            name="bid_set",
            cim_role="BidSet",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid_set:BidSet",
            many=False,
            lower=0,
            upper=1,
            inverse="generating_bids",
            aggregation="none",
        )
    )
    security_constraints: Many[SecurityConstraints] = Many(
        EndMeta(
            name="security_constraints",
            cim_role="SecurityConstraints",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.security_constraints:SecurityConstraints",
            many=True,
            lower=0,
            upper=None,
            inverse="generating_bid",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="GeneratingBid",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{EE38CBD0-D27E-4b93-9ECC-C43233E58F2B}",
        attributes=(
            AttrMeta(
                "combined_cycle_unit_offer", "combinedCycleUnitOffer", "str", 0, 1, "primitive"
            ),
            AttrMeta("down_time_max", "downTimeMax", "float", 0, 1, "primitive"),
            AttrMeta("installed_capacity", "installedCapacity", "float", 0, 1, "primitive"),
            AttrMeta(
                "lower_ramp_rate", "lowerRampRate", "ActivePowerChangeRate", 0, 1, "cimdatatype"
            ),
            AttrMeta("max_emergency_mw", "maxEmergencyMW", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("maximum_economic_mw", "maximumEconomicMW", "float", 0, 1, "primitive"),
            AttrMeta("min_emergency_mw", "minEmergencyMW", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("minimum_economic_mw", "minimumEconomicMW", "float", 0, 1, "primitive"),
            AttrMeta("no_load_cost", "noLoadCost", "float", 0, 1, "primitive"),
            AttrMeta("notification_time", "notificationTime", "float", 0, 1, "primitive"),
            AttrMeta("operating_mode", "operatingMode", "str", 0, 1, "primitive"),
            AttrMeta(
                "raise_ramp_rate", "raiseRampRate", "ActivePowerChangeRate", 0, 1, "cimdatatype"
            ),
            AttrMeta("ramp_curve_type", "rampCurveType", "int", 0, 1, "primitive"),
            AttrMeta("startup_cost", "startupCost", "float", 0, 1, "primitive"),
            AttrMeta(
                "start_up_ramp_rate",
                "startUpRampRate",
                "ActivePowerChangeRate",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("start_up_type", "startUpType", "int", 0, 1, "primitive"),
            AttrMeta("up_time_max", "upTimeMax", "float", 0, 1, "primitive"),
        ),
        ends=(
            start_up_cost_curve.meta,
            start_up_time_curve.meta,
            notification_time_curve.meta,
            ramp_rate_curve.meta,
            registered_generator.meta,
            bid_set.meta,
            security_constraints.meta,
        ),
    )

    def __init__(
        self,
        *,
        combined_cycle_unit_offer: str | None = None,
        down_time_max: float | None = None,
        installed_capacity: float | None = None,
        lower_ramp_rate: float | None = None,
        max_emergency_mw: float | None = None,
        maximum_economic_mw: float | None = None,
        min_emergency_mw: float | None = None,
        minimum_economic_mw: float | None = None,
        no_load_cost: float | None = None,
        notification_time: float | None = None,
        operating_mode: str | None = None,
        raise_ramp_rate: float | None = None,
        ramp_curve_type: int | None = None,
        startup_cost: float | None = None,
        start_up_ramp_rate: float | None = None,
        start_up_type: int | None = None,
        up_time_max: float | None = None,
        start_up_cost_curve: StartUpCostCurve | None = None,
        start_up_time_curve: StartUpTimeCurve | None = None,
        notification_time_curve: NotificationTimeCurve | None = None,
        ramp_rate_curve: Iterable[RampRateCurve] | None = None,
        registered_generator: RegisteredGenerator | None = None,
        bid_set: BidSet | None = None,
        security_constraints: Iterable[SecurityConstraints] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.combined_cycle_unit_offer = combined_cycle_unit_offer
        self.down_time_max = down_time_max
        self.installed_capacity = installed_capacity
        self.lower_ramp_rate = lower_ramp_rate
        self.max_emergency_mw = max_emergency_mw
        self.maximum_economic_mw = maximum_economic_mw
        self.min_emergency_mw = min_emergency_mw
        self.minimum_economic_mw = minimum_economic_mw
        self.no_load_cost = no_load_cost
        self.notification_time = notification_time
        self.operating_mode = operating_mode
        self.raise_ramp_rate = raise_ramp_rate
        self.ramp_curve_type = ramp_curve_type
        self.startup_cost = startup_cost
        self.start_up_ramp_rate = start_up_ramp_rate
        self.start_up_type = start_up_type
        self.up_time_max = up_time_max
        if start_up_cost_curve is not None:
            self.start_up_cost_curve = start_up_cost_curve
        if start_up_time_curve is not None:
            self.start_up_time_curve = start_up_time_curve
        if notification_time_curve is not None:
            self.notification_time_curve = notification_time_curve
        if ramp_rate_curve is not None:
            GeneratingBid.ramp_rate_curve.extend(self, ramp_rate_curve)
        if registered_generator is not None:
            self.registered_generator = registered_generator
        if bid_set is not None:
            self.bid_set = bid_set
        if security_constraints is not None:
            GeneratingBid.security_constraints.extend(self, security_constraints)

    def add_ramp_rate_curve(self, ramp_rate_curve: RampRateCurve) -> Self:
        return GeneratingBid.ramp_rate_curve.add(self, ramp_rate_curve)

    def remove_ramp_rate_curve(self, ramp_rate_curve: RampRateCurve) -> Self:
        return GeneratingBid.ramp_rate_curve.remove(self, ramp_rate_curve)

    def clear_ramp_rate_curve(self) -> Self:
        return GeneratingBid.ramp_rate_curve.clear(self)

    def num_ramp_rate_curve(self) -> int:
        return GeneratingBid.ramp_rate_curve.count(self)

    def get_ramp_rate_curve_by_mrid(self, mrid: str) -> RampRateCurve | None:
        return GeneratingBid.ramp_rate_curve.get_by_mrid(self, mrid)

    def add_security_constraint(self, security_constraint: SecurityConstraints) -> Self:
        return GeneratingBid.security_constraints.add(self, security_constraint)

    def remove_security_constraint(self, security_constraint: SecurityConstraints) -> Self:
        return GeneratingBid.security_constraints.remove(self, security_constraint)

    def clear_security_constraints(self) -> Self:
        return GeneratingBid.security_constraints.clear(self)

    def num_security_constraint(self) -> int:
        return GeneratingBid.security_constraints.count(self)

    def get_security_constraint_by_mrid(self, mrid: str) -> SecurityConstraints | None:
        return GeneratingBid.security_constraints.get_by_mrid(self, mrid)

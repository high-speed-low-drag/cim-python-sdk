"""CIM class RegisteredInterTie (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.interchange_schedule import (
        InterchangeSchedule,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.energy_product_type import (
        EnergyProductType,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.inter_tie_direction import (
        InterTieDirection,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.inter_tie_bid import (
        InterTieBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.inter_tie_dispatch_response import (
        InterTieDispatchResponse,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate
    from cim_python_sdk.model.iec62325.market_operations.reference_data.wheeling_counter_party import (
        WheelingCounterParty,
    )


class RegisteredInterTie(RegisteredResource):
    """This class represents the inter tie resource."""

    __slots__ = (
        "_flowgate",
        "_inter_tie_bid",
        "_inter_tie_dispatch_response",
        "_interchange_schedule",
        "_wheeling_counter_party",
        "direction",
        "energy_product_type",
        "is_dc_tie",
        "is_dynamic_interchange",
        "min_hourly_block_limit",
    )

    direction: InterTieDirection | None
    energy_product_type: EnergyProductType | None
    is_dc_tie: YesNo | None
    is_dynamic_interchange: YesNo | None
    min_hourly_block_limit: int | None

    wheeling_counter_party: Many[WheelingCounterParty] = Many(
        EndMeta(
            name="wheeling_counter_party",
            cim_role="WheelingCounterParty",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.wheeling_counter_party:WheelingCounterParty",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_inter_tie",
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
            inverse="registered_inter_tie",
            aggregation="none",
        )
    )
    inter_tie_dispatch_response: Many[InterTieDispatchResponse] = Many(
        EndMeta(
            name="inter_tie_dispatch_response",
            cim_role="InterTieDispatchResponse",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.inter_tie_dispatch_response:InterTieDispatchResponse",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_inter_tie",
            aggregation="none",
        )
    )
    inter_tie_bid: One[InterTieBid] = One(
        EndMeta(
            name="inter_tie_bid",
            cim_role="InterTieBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.inter_tie_bid:InterTieBid",
            many=False,
            lower=0,
            upper=1,
            inverse="registered_inter_tie",
            aggregation="none",
        )
    )
    interchange_schedule: Many[InterchangeSchedule] = Many(
        EndMeta(
            name="interchange_schedule",
            cim_role="InterchangeSchedule",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.interchange_schedule:InterchangeSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="registered_inter_tie",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RegisteredInterTie",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{3A575D6B-3C0D-46ab-92F5-A7FEB25D9633}",
        attributes=(
            AttrMeta("direction", "direction", "InterTieDirection", 0, 1, "enumeration"),
            AttrMeta(
                "energy_product_type", "energyProductType", "EnergyProductType", 0, 1, "enumeration"
            ),
            AttrMeta("is_dc_tie", "isDCTie", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "is_dynamic_interchange", "isDynamicInterchange", "YesNo", 0, 1, "enumeration"
            ),
            AttrMeta("min_hourly_block_limit", "minHourlyBlockLimit", "int", 0, 1, "primitive"),
        ),
        ends=(
            wheeling_counter_party.meta,
            flowgate.meta,
            inter_tie_dispatch_response.meta,
            inter_tie_bid.meta,
            interchange_schedule.meta,
        ),
    )

    def __init__(
        self,
        *,
        direction: InterTieDirection | None = None,
        energy_product_type: EnergyProductType | None = None,
        is_dc_tie: YesNo | None = None,
        is_dynamic_interchange: YesNo | None = None,
        min_hourly_block_limit: int | None = None,
        wheeling_counter_party: Iterable[WheelingCounterParty] | None = None,
        flowgate: Flowgate | None = None,
        inter_tie_dispatch_response: Iterable[InterTieDispatchResponse] | None = None,
        inter_tie_bid: InterTieBid | None = None,
        interchange_schedule: Iterable[InterchangeSchedule] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.direction = direction
        self.energy_product_type = energy_product_type
        self.is_dc_tie = is_dc_tie
        self.is_dynamic_interchange = is_dynamic_interchange
        self.min_hourly_block_limit = min_hourly_block_limit
        if wheeling_counter_party is not None:
            RegisteredInterTie.wheeling_counter_party.extend(self, wheeling_counter_party)
        if flowgate is not None:
            self.flowgate = flowgate
        if inter_tie_dispatch_response is not None:
            RegisteredInterTie.inter_tie_dispatch_response.extend(self, inter_tie_dispatch_response)
        if inter_tie_bid is not None:
            self.inter_tie_bid = inter_tie_bid
        if interchange_schedule is not None:
            RegisteredInterTie.interchange_schedule.extend(self, interchange_schedule)

    def add_wheeling_counter_party(self, wheeling_counter_party: WheelingCounterParty) -> Self:
        return RegisteredInterTie.wheeling_counter_party.add(self, wheeling_counter_party)

    def remove_wheeling_counter_party(self, wheeling_counter_party: WheelingCounterParty) -> Self:
        return RegisteredInterTie.wheeling_counter_party.remove(self, wheeling_counter_party)

    def clear_wheeling_counter_party(self) -> Self:
        return RegisteredInterTie.wheeling_counter_party.clear(self)

    def num_wheeling_counter_party(self) -> int:
        return RegisteredInterTie.wheeling_counter_party.count(self)

    def get_wheeling_counter_party_by_mrid(self, mrid: str) -> WheelingCounterParty | None:
        return RegisteredInterTie.wheeling_counter_party.get_by_mrid(self, mrid)

    def add_inter_tie_dispatch_response(
        self, inter_tie_dispatch_response: InterTieDispatchResponse
    ) -> Self:
        return RegisteredInterTie.inter_tie_dispatch_response.add(self, inter_tie_dispatch_response)

    def remove_inter_tie_dispatch_response(
        self, inter_tie_dispatch_response: InterTieDispatchResponse
    ) -> Self:
        return RegisteredInterTie.inter_tie_dispatch_response.remove(
            self, inter_tie_dispatch_response
        )

    def clear_inter_tie_dispatch_response(self) -> Self:
        return RegisteredInterTie.inter_tie_dispatch_response.clear(self)

    def num_inter_tie_dispatch_response(self) -> int:
        return RegisteredInterTie.inter_tie_dispatch_response.count(self)

    def add_interchange_schedule(self, interchange_schedule: InterchangeSchedule) -> Self:
        return RegisteredInterTie.interchange_schedule.add(self, interchange_schedule)

    def remove_interchange_schedule(self, interchange_schedule: InterchangeSchedule) -> Self:
        return RegisteredInterTie.interchange_schedule.remove(self, interchange_schedule)

    def clear_interchange_schedule(self) -> Self:
        return RegisteredInterTie.interchange_schedule.clear(self)

    def num_interchange_schedule(self) -> int:
        return RegisteredInterTie.interchange_schedule.count(self)

    def get_interchange_schedule_by_mrid(self, mrid: str) -> InterchangeSchedule | None:
        return RegisteredInterTie.interchange_schedule.get_by_mrid(self, mrid)

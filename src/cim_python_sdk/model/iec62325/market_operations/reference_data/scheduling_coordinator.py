"""CIM class SchedulingCoordinator (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_common.market_participant import MarketParticipant

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade import Trade
    from cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right import (
        ContractRight,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.load_ratio import LoadRatio
    from cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator_user import (
        SchedulingCoordinatorUser,
    )


class SchedulingCoordinator(MarketParticipant):
    """Market participants could be represented by Scheduling Coordinators (SCs) that are
    registered with the RTO/ISO. One participant could register multiple SCs with the
    RTO/ISO. Many market participants can do business with the RTO/ISO using a single SC.
    One SC could schedule multiple generators. A load scheduling point could be used by
    multiple SCs. Each SC could schedule load at multiple scheduling points. An inter-tie
    scheduling point can be used by multiple SCs. Each SC can schedule interchange at
    multiple inter-tie scheduling points."""

    __slots__ = (
        "_from_sc_trade",
        "_load_ratio",
        "_market_participant",
        "_scheduling_coordinator_users",
        "_submit_from_sc_trade",
        "_submit_to_sc_trade",
        "_to_sc_trade",
        "_transmission_contract_right",
        "credit_flag",
        "credit_start_effective_date",
        "last_modified",
        "qualification_status",
        "scid",
    )

    credit_flag: YesNo | None
    credit_start_effective_date: _dt.datetime | None
    last_modified: _dt.datetime | None
    qualification_status: str | None
    scid: str | None

    load_ratio: One[LoadRatio] = One(
        EndMeta(
            name="load_ratio",
            cim_role="LoadRatio",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.load_ratio:LoadRatio",
            many=False,
            lower=1,
            upper=1,
            inverse="scheduling_coordinator",
            aggregation="none",
        )
    )
    scheduling_coordinator_users: Many[SchedulingCoordinatorUser] = Many(
        EndMeta(
            name="scheduling_coordinator_users",
            cim_role=None,
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.scheduling_coordinator_user:SchedulingCoordinatorUser",
            many=True,
            lower=0,
            upper=None,
            inverse="scheduling_coordinator",
            aggregation="shared",
        )
    )
    submit_from_sc_trade: Many[Trade] = Many(
        EndMeta(
            name="submit_from_sc_trade",
            cim_role="SubmitFromSCTrade",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade:Trade",
            many=True,
            lower=0,
            upper=None,
            inverse="submit_from_scheduling_coordinator",
            aggregation="none",
        )
    )
    from_sc_trade: Many[Trade] = Many(
        EndMeta(
            name="from_sc_trade",
            cim_role="FromSCTrade",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade:Trade",
            many=True,
            lower=0,
            upper=None,
            inverse="from_sc",
            aggregation="none",
        )
    )
    to_sc_trade: Many[Trade] = Many(
        EndMeta(
            name="to_sc_trade",
            cim_role="ToSCTrade",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade:Trade",
            many=True,
            lower=0,
            upper=None,
            inverse="to_sc",
            aggregation="none",
        )
    )
    transmission_contract_right: Many[ContractRight] = Many(
        EndMeta(
            name="transmission_contract_right",
            cim_role="TransmissionContractRight",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right:ContractRight",
            many=True,
            lower=0,
            upper=None,
            inverse="scheduling_coordinator",
            aggregation="none",
        )
    )
    submit_to_sc_trade: Many[Trade] = Many(
        EndMeta(
            name="submit_to_sc_trade",
            cim_role="SubmitToSCTrade",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.trade:Trade",
            many=True,
            lower=0,
            upper=None,
            inverse="submit_to_scheduling_coordinator",
            aggregation="none",
        )
    )
    market_participant: One[MarketParticipant] = One(
        EndMeta(
            name="market_participant",
            cim_role="MarketParticipant",
            target="cim_python_sdk.model.iec62325.market_common.market_participant:MarketParticipant",
            many=False,
            lower=0,
            upper=1,
            inverse="scheduling_coordinator",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SchedulingCoordinator",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{29DD7B48-807D-4f7a-8570-3C7EFF51D865}",
        attributes=(
            AttrMeta("credit_flag", "creditFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "credit_start_effective_date",
                "creditStartEffectiveDate",
                "datetime",
                0,
                1,
                "primitive",
            ),
            AttrMeta("last_modified", "lastModified", "datetime", 0, 1, "primitive"),
            AttrMeta("qualification_status", "qualificationStatus", "str", 0, 1, "primitive"),
            AttrMeta("scid", "scid", "str", 0, 1, "primitive"),
        ),
        ends=(
            load_ratio.meta,
            scheduling_coordinator_users.meta,
            submit_from_sc_trade.meta,
            from_sc_trade.meta,
            to_sc_trade.meta,
            transmission_contract_right.meta,
            submit_to_sc_trade.meta,
            market_participant.meta,
        ),
    )

    def __init__(
        self,
        *,
        credit_flag: YesNo | None = None,
        credit_start_effective_date: _dt.datetime | None = None,
        last_modified: _dt.datetime | None = None,
        qualification_status: str | None = None,
        scid: str | None = None,
        load_ratio: LoadRatio | None = None,
        scheduling_coordinator_users: Iterable[SchedulingCoordinatorUser] | None = None,
        submit_from_sc_trade: Iterable[Trade] | None = None,
        from_sc_trade: Iterable[Trade] | None = None,
        to_sc_trade: Iterable[Trade] | None = None,
        transmission_contract_right: Iterable[ContractRight] | None = None,
        submit_to_sc_trade: Iterable[Trade] | None = None,
        market_participant: MarketParticipant | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.credit_flag = credit_flag
        self.credit_start_effective_date = credit_start_effective_date
        self.last_modified = last_modified
        self.qualification_status = qualification_status
        self.scid = scid
        if load_ratio is not None:
            self.load_ratio = load_ratio
        if scheduling_coordinator_users is not None:
            SchedulingCoordinator.scheduling_coordinator_users.extend(
                self, scheduling_coordinator_users
            )
        if submit_from_sc_trade is not None:
            SchedulingCoordinator.submit_from_sc_trade.extend(self, submit_from_sc_trade)
        if from_sc_trade is not None:
            SchedulingCoordinator.from_sc_trade.extend(self, from_sc_trade)
        if to_sc_trade is not None:
            SchedulingCoordinator.to_sc_trade.extend(self, to_sc_trade)
        if transmission_contract_right is not None:
            SchedulingCoordinator.transmission_contract_right.extend(
                self, transmission_contract_right
            )
        if submit_to_sc_trade is not None:
            SchedulingCoordinator.submit_to_sc_trade.extend(self, submit_to_sc_trade)
        if market_participant is not None:
            self.market_participant = market_participant

    def add_scheduling_coordinator_user(
        self, scheduling_coordinator_user: SchedulingCoordinatorUser
    ) -> Self:
        return SchedulingCoordinator.scheduling_coordinator_users.add(
            self, scheduling_coordinator_user
        )

    def remove_scheduling_coordinator_user(
        self, scheduling_coordinator_user: SchedulingCoordinatorUser
    ) -> Self:
        return SchedulingCoordinator.scheduling_coordinator_users.remove(
            self, scheduling_coordinator_user
        )

    def clear_scheduling_coordinator_users(self) -> Self:
        return SchedulingCoordinator.scheduling_coordinator_users.clear(self)

    def num_scheduling_coordinator_user(self) -> int:
        return SchedulingCoordinator.scheduling_coordinator_users.count(self)

    def add_submit_from_sc_trade(self, submit_from_sc_trade: Trade) -> Self:
        return SchedulingCoordinator.submit_from_sc_trade.add(self, submit_from_sc_trade)

    def remove_submit_from_sc_trade(self, submit_from_sc_trade: Trade) -> Self:
        return SchedulingCoordinator.submit_from_sc_trade.remove(self, submit_from_sc_trade)

    def clear_submit_from_sc_trade(self) -> Self:
        return SchedulingCoordinator.submit_from_sc_trade.clear(self)

    def num_submit_from_sc_trade(self) -> int:
        return SchedulingCoordinator.submit_from_sc_trade.count(self)

    def get_submit_from_sc_trade_by_mrid(self, mrid: str) -> Trade | None:
        return SchedulingCoordinator.submit_from_sc_trade.get_by_mrid(self, mrid)

    def add_from_sc_trade(self, from_sc_trade: Trade) -> Self:
        return SchedulingCoordinator.from_sc_trade.add(self, from_sc_trade)

    def remove_from_sc_trade(self, from_sc_trade: Trade) -> Self:
        return SchedulingCoordinator.from_sc_trade.remove(self, from_sc_trade)

    def clear_from_sc_trade(self) -> Self:
        return SchedulingCoordinator.from_sc_trade.clear(self)

    def num_from_sc_trade(self) -> int:
        return SchedulingCoordinator.from_sc_trade.count(self)

    def get_from_sc_trade_by_mrid(self, mrid: str) -> Trade | None:
        return SchedulingCoordinator.from_sc_trade.get_by_mrid(self, mrid)

    def add_to_sc_trade(self, to_sc_trade: Trade) -> Self:
        return SchedulingCoordinator.to_sc_trade.add(self, to_sc_trade)

    def remove_to_sc_trade(self, to_sc_trade: Trade) -> Self:
        return SchedulingCoordinator.to_sc_trade.remove(self, to_sc_trade)

    def clear_to_sc_trade(self) -> Self:
        return SchedulingCoordinator.to_sc_trade.clear(self)

    def num_to_sc_trade(self) -> int:
        return SchedulingCoordinator.to_sc_trade.count(self)

    def get_to_sc_trade_by_mrid(self, mrid: str) -> Trade | None:
        return SchedulingCoordinator.to_sc_trade.get_by_mrid(self, mrid)

    def add_transmission_contract_right(self, transmission_contract_right: ContractRight) -> Self:
        return SchedulingCoordinator.transmission_contract_right.add(
            self, transmission_contract_right
        )

    def remove_transmission_contract_right(
        self, transmission_contract_right: ContractRight
    ) -> Self:
        return SchedulingCoordinator.transmission_contract_right.remove(
            self, transmission_contract_right
        )

    def clear_transmission_contract_right(self) -> Self:
        return SchedulingCoordinator.transmission_contract_right.clear(self)

    def num_transmission_contract_right(self) -> int:
        return SchedulingCoordinator.transmission_contract_right.count(self)

    def get_transmission_contract_right_by_mrid(self, mrid: str) -> ContractRight | None:
        return SchedulingCoordinator.transmission_contract_right.get_by_mrid(self, mrid)

    def add_submit_to_sc_trade(self, submit_to_sc_trade: Trade) -> Self:
        return SchedulingCoordinator.submit_to_sc_trade.add(self, submit_to_sc_trade)

    def remove_submit_to_sc_trade(self, submit_to_sc_trade: Trade) -> Self:
        return SchedulingCoordinator.submit_to_sc_trade.remove(self, submit_to_sc_trade)

    def clear_submit_to_sc_trade(self) -> Self:
        return SchedulingCoordinator.submit_to_sc_trade.clear(self)

    def num_submit_to_sc_trade(self) -> int:
        return SchedulingCoordinator.submit_to_sc_trade.count(self)

    def get_submit_to_sc_trade_by_mrid(self, mrid: str) -> Trade | None:
        return SchedulingCoordinator.submit_to_sc_trade.get_by_mrid(self, mrid)

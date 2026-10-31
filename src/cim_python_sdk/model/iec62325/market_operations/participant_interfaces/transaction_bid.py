"""CIM class TransactionBid (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.bid import Bid

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_profile import (
        EnergyProfile,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_reservation import (
        TransmissionReservation,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.market_results.transaction_bid_results import (
        TransactionBidResults,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode


class TransactionBid(Bid):
    """Bilateral or scheduled transactions for energy and ancillary services considered by
    market clearing process."""

    __slots__ = (
        "_delivery_pnode",
        "_energy_profiles",
        "_receipt_pnode",
        "_transaction_bid_results",
        "_transmission_reservation",
        "demand_transaction",
        "dispatchable",
        "pay_congestion",
    )

    demand_transaction: bool | None
    dispatchable: bool | None
    pay_congestion: bool | None

    transaction_bid_results: Many[TransactionBidResults] = Many(
        EndMeta(
            name="transaction_bid_results",
            cim_role="TransactionBidResults",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.market_results.transaction_bid_results:TransactionBidResults",
            many=True,
            lower=0,
            upper=None,
            inverse="transaction_bid",
            aggregation="none",
        )
    )
    delivery_pnode: One[Pnode] = One(
        EndMeta(
            name="delivery_pnode",
            cim_role="Delivery_Pnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=False,
            lower=0,
            upper=1,
            inverse="delivery_transaction_bids",
            aggregation="none",
        )
    )
    receipt_pnode: One[Pnode] = One(
        EndMeta(
            name="receipt_pnode",
            cim_role="Receipt_Pnode",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=False,
            lower=0,
            upper=1,
            inverse="receipt_transaction_bids",
            aggregation="none",
        )
    )
    transmission_reservation: One[TransmissionReservation] = One(
        EndMeta(
            name="transmission_reservation",
            cim_role="TransmissionReservation",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_reservation:TransmissionReservation",
            many=False,
            lower=0,
            upper=1,
            inverse="transaction_bid",
            aggregation="none",
        )
    )
    energy_profiles: Many[EnergyProfile] = Many(
        EndMeta(
            name="energy_profiles",
            cim_role="EnergyProfiles",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_profile:EnergyProfile",
            many=True,
            lower=1,
            upper=None,
            inverse="transaction_bid",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransactionBid",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{CCB96D43-271B-46b2-AC67-CBBBADB5904F}",
        attributes=(
            AttrMeta("demand_transaction", "demandTransaction", "bool", 0, 1, "primitive"),
            AttrMeta("dispatchable", "dispatchable", "bool", 0, 1, "primitive"),
            AttrMeta("pay_congestion", "payCongestion", "bool", 0, 1, "primitive"),
        ),
        ends=(
            transaction_bid_results.meta,
            delivery_pnode.meta,
            receipt_pnode.meta,
            transmission_reservation.meta,
            energy_profiles.meta,
        ),
    )

    def __init__(
        self,
        *,
        demand_transaction: bool | None = None,
        dispatchable: bool | None = None,
        pay_congestion: bool | None = None,
        transaction_bid_results: Iterable[TransactionBidResults] | None = None,
        delivery_pnode: Pnode | None = None,
        receipt_pnode: Pnode | None = None,
        transmission_reservation: TransmissionReservation | None = None,
        energy_profiles: Iterable[EnergyProfile] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.demand_transaction = demand_transaction
        self.dispatchable = dispatchable
        self.pay_congestion = pay_congestion
        if transaction_bid_results is not None:
            TransactionBid.transaction_bid_results.extend(self, transaction_bid_results)
        if delivery_pnode is not None:
            self.delivery_pnode = delivery_pnode
        if receipt_pnode is not None:
            self.receipt_pnode = receipt_pnode
        if transmission_reservation is not None:
            self.transmission_reservation = transmission_reservation
        if energy_profiles is not None:
            TransactionBid.energy_profiles.extend(self, energy_profiles)

    def add_transaction_bid_result(self, transaction_bid_result: TransactionBidResults) -> Self:
        return TransactionBid.transaction_bid_results.add(self, transaction_bid_result)

    def remove_transaction_bid_result(self, transaction_bid_result: TransactionBidResults) -> Self:
        return TransactionBid.transaction_bid_results.remove(self, transaction_bid_result)

    def clear_transaction_bid_results(self) -> Self:
        return TransactionBid.transaction_bid_results.clear(self)

    def num_transaction_bid_result(self) -> int:
        return TransactionBid.transaction_bid_results.count(self)

    def get_transaction_bid_result_by_mrid(self, mrid: str) -> TransactionBidResults | None:
        return TransactionBid.transaction_bid_results.get_by_mrid(self, mrid)

    def add_energy_profile(self, energy_profile: EnergyProfile) -> Self:
        return TransactionBid.energy_profiles.add(self, energy_profile)

    def remove_energy_profile(self, energy_profile: EnergyProfile) -> Self:
        return TransactionBid.energy_profiles.remove(self, energy_profile)

    def clear_energy_profiles(self) -> Self:
        return TransactionBid.energy_profiles.clear(self)

    def num_energy_profile(self) -> int:
        return TransactionBid.energy_profiles.count(self)

    def get_energy_profile_by_mrid(self, mrid: str) -> EnergyProfile | None:
        return TransactionBid.energy_profiles.get_by_mrid(self, mrid)

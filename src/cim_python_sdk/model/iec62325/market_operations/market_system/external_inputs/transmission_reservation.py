"""CIM class TransmissionReservation (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction import (
        EnergyTransaction,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.service_point import (
        ServicePoint,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_path import (
        TransmissionPath,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.transaction_bid import (
        TransactionBid,
    )


class TransmissionReservation(CimObject):
    """A transmission reservation is obtained from the OASIS system to reserve transmission for
    a specified time period, transmission path and transmission product."""

    __slots__ = (
        "_energy_transaction",
        "_sink",
        "_source",
        "_transaction_bid",
        "_transmission_path",
    )

    sink: One[ServicePoint] = One(
        EndMeta(
            name="sink",
            cim_role="Sink",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.service_point:ServicePoint",
            many=False,
            lower=0,
            upper=1,
            inverse="sink_reservation",
            aggregation="none",
        )
    )
    energy_transaction: One[EnergyTransaction] = One(
        EndMeta(
            name="energy_transaction",
            cim_role="EnergyTransaction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction:EnergyTransaction",
            many=False,
            lower=0,
            upper=1,
            inverse="transmission_reservation",
            aggregation="none",
        )
    )
    transaction_bid: One[TransactionBid] = One(
        EndMeta(
            name="transaction_bid",
            cim_role="TransactionBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.transaction_bid:TransactionBid",
            many=False,
            lower=0,
            upper=1,
            inverse="transmission_reservation",
            aggregation="none",
        )
    )
    source: One[ServicePoint] = One(
        EndMeta(
            name="source",
            cim_role="Source",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.service_point:ServicePoint",
            many=False,
            lower=0,
            upper=1,
            inverse="source_reservation",
            aggregation="none",
        )
    )
    transmission_path: One[TransmissionPath] = One(
        EndMeta(
            name="transmission_path",
            cim_role="TransmissionPath",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_path:TransmissionPath",
            many=False,
            lower=1,
            upper=1,
            inverse="transmission_reservation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransmissionReservation",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{1E49E136-2EDC-45a3-AEB8-345AF93E5F5E}",
        ends=(
            sink.meta,
            energy_transaction.meta,
            transaction_bid.meta,
            source.meta,
            transmission_path.meta,
        ),
    )

    def __init__(
        self,
        *,
        sink: ServicePoint | None = None,
        energy_transaction: EnergyTransaction | None = None,
        transaction_bid: TransactionBid | None = None,
        source: ServicePoint | None = None,
        transmission_path: TransmissionPath | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if sink is not None:
            self.sink = sink
        if energy_transaction is not None:
            self.energy_transaction = energy_transaction
        if transaction_bid is not None:
            self.transaction_bid = transaction_bid
        if source is not None:
            self.source = source
        if transmission_path is not None:
            self.transmission_path = transmission_path

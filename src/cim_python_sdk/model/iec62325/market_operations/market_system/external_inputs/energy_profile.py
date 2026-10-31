"""CIM class EnergyProfile (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.profile import (
    Profile,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction import (
        EnergyTransaction,
    )
    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.transaction_bid import (
        TransactionBid,
    )


class EnergyProfile(Profile):
    """Specifies the start time, stop time, level for an EnergyTransaction."""

    __slots__ = ("_energy_transaction", "_transaction_bid")

    energy_transaction: One[EnergyTransaction] = One(
        EndMeta(
            name="energy_transaction",
            cim_role="EnergyTransaction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction:EnergyTransaction",
            many=False,
            lower=1,
            upper=1,
            inverse="energy_profiles",
            aggregation="none",
        )
    )
    transaction_bid: One[TransactionBid] = One(
        EndMeta(
            name="transaction_bid",
            cim_role="TransactionBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.transaction_bid:TransactionBid",
            many=False,
            lower=1,
            upper=1,
            inverse="energy_profiles",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyProfile",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{46A60F35-459E-4dec-BD8D-FE46FB498CD6}",
        ends=(
            energy_transaction.meta,
            transaction_bid.meta,
        ),
    )

    def __init__(
        self,
        *,
        energy_transaction: EnergyTransaction | None = None,
        transaction_bid: TransactionBid | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if energy_transaction is not None:
            self.energy_transaction = energy_transaction
        if transaction_bid is not None:
            self.transaction_bid = transaction_bid

"""CIM class EnergyPriceCurve (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_congestion_revenue_rights.ftr import FTR
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction import (
        EnergyTransaction,
    )


class EnergyPriceCurve(CimObject):
    """Relationship between a price in $(or other monetary unit) /hour (Y-axis) and a MW value
    (X-axis)."""

    __slots__ = ("_energy_transactions", "_ftrs")

    ftrs: Many[FTR] = Many(
        EndMeta(
            name="ftrs",
            cim_role="FTRs",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_congestion_revenue_rights.ftr:FTR",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_price_curve",
            aggregation="none",
        )
    )
    energy_transactions: Many[EnergyTransaction] = Many(
        EndMeta(
            name="energy_transactions",
            cim_role="EnergyTransactions",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction:EnergyTransaction",
            many=True,
            lower=0,
            upper=None,
            inverse="energy_price_curves",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyPriceCurve",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{4DE57A72-7481-4ba0-AFEE-5B5A86F4F166}",
        ends=(
            ftrs.meta,
            energy_transactions.meta,
        ),
    )

    def __init__(
        self,
        *,
        ftrs: Iterable[FTR] | None = None,
        energy_transactions: Iterable[EnergyTransaction] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if ftrs is not None:
            EnergyPriceCurve.ftrs.extend(self, ftrs)
        if energy_transactions is not None:
            EnergyPriceCurve.energy_transactions.extend(self, energy_transactions)

    def add_ftr(self, ftr: FTR) -> Self:
        return EnergyPriceCurve.ftrs.add(self, ftr)

    def remove_ftr(self, ftr: FTR) -> Self:
        return EnergyPriceCurve.ftrs.remove(self, ftr)

    def clear_ftrs(self) -> Self:
        return EnergyPriceCurve.ftrs.clear(self)

    def num_ftr(self) -> int:
        return EnergyPriceCurve.ftrs.count(self)

    def get_ftr_by_mrid(self, mrid: str) -> FTR | None:
        return EnergyPriceCurve.ftrs.get_by_mrid(self, mrid)

    def add_energy_transaction(self, energy_transaction: EnergyTransaction) -> Self:
        return EnergyPriceCurve.energy_transactions.add(self, energy_transaction)

    def remove_energy_transaction(self, energy_transaction: EnergyTransaction) -> Self:
        return EnergyPriceCurve.energy_transactions.remove(self, energy_transaction)

    def clear_energy_transactions(self) -> Self:
        return EnergyPriceCurve.energy_transactions.clear(self)

    def num_energy_transaction(self) -> int:
        return EnergyPriceCurve.energy_transactions.count(self)

    def get_energy_transaction_by_mrid(self, mrid: str) -> EnergyTransaction | None:
        return EnergyPriceCurve.energy_transactions.get_by_mrid(self, mrid)

"""CIM class EnergyProduct (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.agreement import Agreement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.generation_provider import (
        GenerationProvider,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.marketer import Marketer
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction import (
        EnergyTransaction,
    )


class EnergyProduct(Agreement):
    """An EnergyProduct is offered commercially as a ContractOrTariff."""

    __slots__ = (
        "_energy_transactions",
        "_generation_provider",
        "_resold_by_marketer",
        "_title_held_by_marketer",
    )

    title_held_by_marketer: One[Marketer] = One(
        EndMeta(
            name="title_held_by_marketer",
            cim_role="TitleHeldBy_Marketer",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.marketer:Marketer",
            many=False,
            lower=0,
            upper=1,
            inverse="holds_title_to_energy_products",
            aggregation="none",
        )
    )
    energy_transactions: Many[EnergyTransaction] = Many(
        EndMeta(
            name="energy_transactions",
            cim_role="EnergyTransactions",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction:EnergyTransaction",
            many=True,
            lower=1,
            upper=None,
            inverse="energy_product",
            aggregation="none",
        )
    )
    generation_provider: One[GenerationProvider] = One(
        EndMeta(
            name="generation_provider",
            cim_role="GenerationProvider",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.generation_provider:GenerationProvider",
            many=False,
            lower=1,
            upper=1,
            inverse="provided_by",
            aggregation="none",
        )
    )
    resold_by_marketer: Many[Marketer] = Many(
        EndMeta(
            name="resold_by_marketer",
            cim_role="ResoldBy_Marketer",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.marketer:Marketer",
            many=True,
            lower=0,
            upper=None,
            inverse="resells_energy_product",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyProduct",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{19926DEE-044E-4b26-84C3-E43379FDDD84}",
        ends=(
            title_held_by_marketer.meta,
            energy_transactions.meta,
            generation_provider.meta,
            resold_by_marketer.meta,
        ),
    )

    def __init__(
        self,
        *,
        title_held_by_marketer: Marketer | None = None,
        energy_transactions: Iterable[EnergyTransaction] | None = None,
        generation_provider: GenerationProvider | None = None,
        resold_by_marketer: Iterable[Marketer] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if title_held_by_marketer is not None:
            self.title_held_by_marketer = title_held_by_marketer
        if energy_transactions is not None:
            EnergyProduct.energy_transactions.extend(self, energy_transactions)
        if generation_provider is not None:
            self.generation_provider = generation_provider
        if resold_by_marketer is not None:
            EnergyProduct.resold_by_marketer.extend(self, resold_by_marketer)

    def add_energy_transaction(self, energy_transaction: EnergyTransaction) -> Self:
        return EnergyProduct.energy_transactions.add(self, energy_transaction)

    def remove_energy_transaction(self, energy_transaction: EnergyTransaction) -> Self:
        return EnergyProduct.energy_transactions.remove(self, energy_transaction)

    def clear_energy_transactions(self) -> Self:
        return EnergyProduct.energy_transactions.clear(self)

    def num_energy_transaction(self) -> int:
        return EnergyProduct.energy_transactions.count(self)

    def get_energy_transaction_by_mrid(self, mrid: str) -> EnergyTransaction | None:
        return EnergyProduct.energy_transactions.get_by_mrid(self, mrid)

    def add_resold_by_marketer(self, resold_by_marketer: Marketer) -> Self:
        return EnergyProduct.resold_by_marketer.add(self, resold_by_marketer)

    def remove_resold_by_marketer(self, resold_by_marketer: Marketer) -> Self:
        return EnergyProduct.resold_by_marketer.remove(self, resold_by_marketer)

    def clear_resold_by_marketer(self) -> Self:
        return EnergyProduct.resold_by_marketer.clear(self)

    def num_resold_by_marketer(self) -> int:
        return EnergyProduct.resold_by_marketer.count(self)

    def get_resold_by_marketer_by_mrid(self, mrid: str) -> Marketer | None:
        return EnergyProduct.resold_by_marketer.get_by_mrid(self, mrid)

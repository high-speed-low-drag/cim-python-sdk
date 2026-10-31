"""CIM class CurtailmentProfile (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

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


class CurtailmentProfile(Profile):
    """Curtailing entity must be providing at least one service to the EnergyTransaction. The
    CurtailmentProfile must be completely contained within the EnergyProfile timeframe for
    this EnergyTransaction."""

    __slots__ = ("_energy_transaction",)

    energy_transaction: One[EnergyTransaction] = One(
        EndMeta(
            name="energy_transaction",
            cim_role="EnergyTransaction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction:EnergyTransaction",
            many=False,
            lower=1,
            upper=1,
            inverse="curtailment_profiles",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CurtailmentProfile",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{C11A5B85-693D-412c-8B62-3A1008D90158}",
        ends=(energy_transaction.meta,),
    )

    def __init__(
        self,
        *,
        energy_transaction: EnergyTransaction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if energy_transaction is not None:
            self.energy_transaction = energy_transaction

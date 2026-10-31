"""CIM class LossProfile (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.profile import (
    Profile,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.transmission_provider import (
        TransmissionProvider,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction import (
        EnergyTransaction,
    )


class LossProfile(Profile):
    """LossProfile is associated with an EnerrgyTransaction and must be completely contained
    within the time frame of the EnergyProfile associated with this EnergyTransaction."""

    __slots__ = ("_energy_transaction", "_has_loss")

    energy_transaction: One[EnergyTransaction] = One(
        EndMeta(
            name="energy_transaction",
            cim_role="EnergyTransaction",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.energy_transaction:EnergyTransaction",
            many=False,
            lower=1,
            upper=1,
            inverse="loss_profiles",
            aggregation="none",
        )
    )
    has_loss: One[TransmissionProvider] = One(
        EndMeta(
            name="has_loss",
            cim_role="HasLoss_",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.transmission_provider:TransmissionProvider",
            many=False,
            lower=0,
            upper=1,
            inverse="for_",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LossProfile",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{54BFFACA-ABB8-4351-AEF1-5377172641D9}",
        ends=(
            energy_transaction.meta,
            has_loss.meta,
        ),
    )

    def __init__(
        self,
        *,
        energy_transaction: EnergyTransaction | None = None,
        has_loss: TransmissionProvider | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if energy_transaction is not None:
            self.energy_transaction = energy_transaction
        if has_loss is not None:
            self.has_loss = has_loss

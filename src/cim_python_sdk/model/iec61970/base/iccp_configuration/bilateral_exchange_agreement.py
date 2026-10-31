"""CIM class BilateralExchangeAgreement (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_actor import (
        BilateralExchangeActor,
    )


class BilateralExchangeAgreement(IdentifiedObject):
    """This is the representation of the information exchange agreement between peers."""

    __slots__ = ("_consumer", "_provider")

    consumer: One[BilateralExchangeActor] = One(
        EndMeta(
            name="consumer",
            cim_role="Consumer",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_actor:BilateralExchangeActor",
            many=False,
            lower=0,
            upper=1,
            inverse="consumer_bilateral_exchange",
            aggregation="none",
        )
    )
    provider: One[BilateralExchangeActor] = One(
        EndMeta(
            name="provider",
            cim_role="Provider",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_actor:BilateralExchangeActor",
            many=False,
            lower=1,
            upper=1,
            inverse="provider_bilateral_exchange",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BilateralExchangeAgreement",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{CF6011D0-FCF1-4f5b-8F98-B14770BEFE86}",
        ends=(
            consumer.meta,
            provider.meta,
        ),
    )

    def __init__(
        self,
        *,
        consumer: BilateralExchangeActor | None = None,
        provider: BilateralExchangeActor | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if consumer is not None:
            self.consumer = consumer
        if provider is not None:
            self.provider = provider

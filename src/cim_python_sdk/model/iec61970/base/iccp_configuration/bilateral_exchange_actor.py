"""CIM class BilateralExchangeActor (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_agreement import (
        BilateralExchangeAgreement,
    )
    from cim_python_sdk.model.iec61970.base.iccp_configuration.provided_bilateral_point import (
        ProvidedBilateralPoint,
    )
    from cim_python_sdk.model.iec61970.base.scada.communication_link import CommunicationLink


class BilateralExchangeActor(IdentifiedObject):
    """BilateralExchangeActor describes an actor that provides ICCP data, consumes ICCP data or
    both. The ICCP data provider lists the data it makes available to an ICCP data consumer.
    This data is described by ProvidedBilateralPoints. The relation between an ICCP data
    provider and a consumer is established by a BilateralExchangeAgreement. It is up to the
    ICCP data consumer to select what ProvidedBilateralPoints to use. The selection made is
    not described in this information model."""

    __slots__ = (
        "_communication_link",
        "_consumer_bilateral_exchange",
        "_provided_bilateral_io_point",
        "_provider_bilateral_exchange",
    )

    consumer_bilateral_exchange: Many[BilateralExchangeAgreement] = Many(
        EndMeta(
            name="consumer_bilateral_exchange",
            cim_role="ConsumerBilateralExchange",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_agreement:BilateralExchangeAgreement",
            many=True,
            lower=0,
            upper=None,
            inverse="consumer",
            aggregation="none",
        )
    )
    provider_bilateral_exchange: Many[BilateralExchangeAgreement] = Many(
        EndMeta(
            name="provider_bilateral_exchange",
            cim_role="ProviderBilateralExchange",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_agreement:BilateralExchangeAgreement",
            many=True,
            lower=0,
            upper=None,
            inverse="provider",
            aggregation="none",
        )
    )
    provided_bilateral_io_point: Many[ProvidedBilateralPoint] = Many(
        EndMeta(
            name="provided_bilateral_io_point",
            cim_role="ProvidedBilateralIOPoint",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.provided_bilateral_point:ProvidedBilateralPoint",
            many=True,
            lower=0,
            upper=None,
            inverse="bilateral_exchange_actor",
            aggregation="none",
        )
    )
    communication_link: Many[CommunicationLink] = Many(
        EndMeta(
            name="communication_link",
            cim_role="CommunicationLink",
            target="cim_python_sdk.model.iec61970.base.scada.communication_link:CommunicationLink",
            many=True,
            lower=0,
            upper=None,
            inverse="bilateral_exchange_actor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BilateralExchangeActor",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{C4C36CA2-2418-4e2f-A0FD-F819DCBC8DE6}",
        ends=(
            consumer_bilateral_exchange.meta,
            provider_bilateral_exchange.meta,
            provided_bilateral_io_point.meta,
            communication_link.meta,
        ),
    )

    def __init__(
        self,
        *,
        consumer_bilateral_exchange: Iterable[BilateralExchangeAgreement] | None = None,
        provider_bilateral_exchange: Iterable[BilateralExchangeAgreement] | None = None,
        provided_bilateral_io_point: Iterable[ProvidedBilateralPoint] | None = None,
        communication_link: Iterable[CommunicationLink] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if consumer_bilateral_exchange is not None:
            BilateralExchangeActor.consumer_bilateral_exchange.extend(
                self, consumer_bilateral_exchange
            )
        if provider_bilateral_exchange is not None:
            BilateralExchangeActor.provider_bilateral_exchange.extend(
                self, provider_bilateral_exchange
            )
        if provided_bilateral_io_point is not None:
            BilateralExchangeActor.provided_bilateral_io_point.extend(
                self, provided_bilateral_io_point
            )
        if communication_link is not None:
            BilateralExchangeActor.communication_link.extend(self, communication_link)

    def add_consumer_bilateral_exchange(
        self, consumer_bilateral_exchange: BilateralExchangeAgreement
    ) -> Self:
        return BilateralExchangeActor.consumer_bilateral_exchange.add(
            self, consumer_bilateral_exchange
        )

    def remove_consumer_bilateral_exchange(
        self, consumer_bilateral_exchange: BilateralExchangeAgreement
    ) -> Self:
        return BilateralExchangeActor.consumer_bilateral_exchange.remove(
            self, consumer_bilateral_exchange
        )

    def clear_consumer_bilateral_exchange(self) -> Self:
        return BilateralExchangeActor.consumer_bilateral_exchange.clear(self)

    def num_consumer_bilateral_exchange(self) -> int:
        return BilateralExchangeActor.consumer_bilateral_exchange.count(self)

    def get_consumer_bilateral_exchange_by_mrid(
        self, mrid: str
    ) -> BilateralExchangeAgreement | None:
        return BilateralExchangeActor.consumer_bilateral_exchange.get_by_mrid(self, mrid)

    def add_provider_bilateral_exchange(
        self, provider_bilateral_exchange: BilateralExchangeAgreement
    ) -> Self:
        return BilateralExchangeActor.provider_bilateral_exchange.add(
            self, provider_bilateral_exchange
        )

    def remove_provider_bilateral_exchange(
        self, provider_bilateral_exchange: BilateralExchangeAgreement
    ) -> Self:
        return BilateralExchangeActor.provider_bilateral_exchange.remove(
            self, provider_bilateral_exchange
        )

    def clear_provider_bilateral_exchange(self) -> Self:
        return BilateralExchangeActor.provider_bilateral_exchange.clear(self)

    def num_provider_bilateral_exchange(self) -> int:
        return BilateralExchangeActor.provider_bilateral_exchange.count(self)

    def get_provider_bilateral_exchange_by_mrid(
        self, mrid: str
    ) -> BilateralExchangeAgreement | None:
        return BilateralExchangeActor.provider_bilateral_exchange.get_by_mrid(self, mrid)

    def add_provided_bilateral_io_point(
        self, provided_bilateral_io_point: ProvidedBilateralPoint
    ) -> Self:
        return BilateralExchangeActor.provided_bilateral_io_point.add(
            self, provided_bilateral_io_point
        )

    def remove_provided_bilateral_io_point(
        self, provided_bilateral_io_point: ProvidedBilateralPoint
    ) -> Self:
        return BilateralExchangeActor.provided_bilateral_io_point.remove(
            self, provided_bilateral_io_point
        )

    def clear_provided_bilateral_io_point(self) -> Self:
        return BilateralExchangeActor.provided_bilateral_io_point.clear(self)

    def num_provided_bilateral_io_point(self) -> int:
        return BilateralExchangeActor.provided_bilateral_io_point.count(self)

    def get_provided_bilateral_io_point_by_mrid(self, mrid: str) -> ProvidedBilateralPoint | None:
        return BilateralExchangeActor.provided_bilateral_io_point.get_by_mrid(self, mrid)

    def add_communication_link(self, communication_link: CommunicationLink) -> Self:
        return BilateralExchangeActor.communication_link.add(self, communication_link)

    def remove_communication_link(self, communication_link: CommunicationLink) -> Self:
        return BilateralExchangeActor.communication_link.remove(self, communication_link)

    def clear_communication_link(self) -> Self:
        return BilateralExchangeActor.communication_link.clear(self)

    def num_communication_link(self) -> int:
        return BilateralExchangeActor.communication_link.count(self)

    def get_communication_link_by_mrid(self, mrid: str) -> CommunicationLink | None:
        return BilateralExchangeActor.communication_link.get_by_mrid(self, mrid)

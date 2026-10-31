"""CIM class MarketDocument (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.market_participant import MarketParticipant
    from cim_python_sdk.model.iec62325.market_management.ace_tariff_type import AceTariffType
    from cim_python_sdk.model.iec62325.market_management.attribute_instance_component import (
        AttributeInstanceComponent,
    )
    from cim_python_sdk.model.iec62325.market_management.date_and_or_time import DateAndOrTime
    from cim_python_sdk.model.iec62325.market_management.domain import Domain
    from cim_python_sdk.model.iec62325.market_management.period import Period
    from cim_python_sdk.model.iec62325.market_management.process import Process
    from cim_python_sdk.model.iec62325.market_management.reason import Reason
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class MarketDocument(Document):
    """Electronic document containing the information necessary to satisfy a given business
    process set of requirements."""

    __slots__ = (
        "_ace_tariff_type",
        "_attribute_instance_component",
        "_date_and_or_time",
        "_domain",
        "_market_document",
        "_market_participant",
        "_period",
        "_process",
        "_reason",
        "_self_market_document",
        "_time_series",
    )

    process: Many[Process] = Many(
        EndMeta(
            name="process",
            cim_role="Process",
            target="cim_python_sdk.model.iec62325.market_management.process:Process",
            many=True,
            lower=0,
            upper=None,
            inverse="market_document",
            aggregation="none",
        )
    )
    period: Many[Period] = Many(
        EndMeta(
            name="period",
            cim_role="Period",
            target="cim_python_sdk.model.iec62325.market_management.period:Period",
            many=True,
            lower=0,
            upper=None,
            inverse="market_document",
            aggregation="none",
        )
    )
    market_participant: Many[MarketParticipant] = Many(
        EndMeta(
            name="market_participant",
            cim_role="MarketParticipant",
            target="cim_python_sdk.model.iec62325.market_common.market_participant:MarketParticipant",
            many=True,
            lower=0,
            upper=None,
            inverse="market_document",
            aggregation="none",
        )
    )
    ace_tariff_type: Many[AceTariffType] = Many(
        EndMeta(
            name="ace_tariff_type",
            cim_role="AceTariffType",
            target="cim_python_sdk.model.iec62325.market_management.ace_tariff_type:AceTariffType",
            many=True,
            lower=0,
            upper=None,
            inverse="market_document",
            aggregation="none",
        )
    )
    attribute_instance_component: Many[AttributeInstanceComponent] = Many(
        EndMeta(
            name="attribute_instance_component",
            cim_role="AttributeInstanceComponent",
            target="cim_python_sdk.model.iec62325.market_management.attribute_instance_component:AttributeInstanceComponent",
            many=True,
            lower=0,
            upper=None,
            inverse="market_document",
            aggregation="none",
        )
    )
    domain: Many[Domain] = Many(
        EndMeta(
            name="domain",
            cim_role="Domain",
            target="cim_python_sdk.model.iec62325.market_management.domain:Domain",
            many=True,
            lower=0,
            upper=None,
            inverse="market_document",
            aggregation="none",
        )
    )
    self_market_document: Many[MarketDocument] = Many(
        EndMeta(
            name="self_market_document",
            cim_role="SelfMarketDocument",
            target="cim_python_sdk.model.iec62325.market_management.market_document:MarketDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="market_document",
            aggregation="none",
        )
    )
    market_document: Many[MarketDocument] = Many(
        EndMeta(
            name="market_document",
            cim_role="MarketDocument",
            target="cim_python_sdk.model.iec62325.market_management.market_document:MarketDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="self_market_document",
            aggregation="none",
        )
    )
    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="market_document",
            aggregation="none",
        )
    )
    reason: Many[Reason] = Many(
        EndMeta(
            name="reason",
            cim_role="Reason",
            target="cim_python_sdk.model.iec62325.market_management.reason:Reason",
            many=True,
            lower=0,
            upper=None,
            inverse="market_document",
            aggregation="none",
        )
    )
    date_and_or_time: Many[DateAndOrTime] = Many(
        EndMeta(
            name="date_and_or_time",
            cim_role="DateAndOrTime",
            target="cim_python_sdk.model.iec62325.market_management.date_and_or_time:DateAndOrTime",
            many=True,
            lower=0,
            upper=None,
            inverse="market_document",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketDocument",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{C3394CCE-C232-4c44-AEFE-C7449974B30B}",
        ends=(
            process.meta,
            period.meta,
            market_participant.meta,
            ace_tariff_type.meta,
            attribute_instance_component.meta,
            domain.meta,
            self_market_document.meta,
            market_document.meta,
            time_series.meta,
            reason.meta,
            date_and_or_time.meta,
        ),
    )

    def __init__(
        self,
        *,
        process: Iterable[Process] | None = None,
        period: Iterable[Period] | None = None,
        market_participant: Iterable[MarketParticipant] | None = None,
        ace_tariff_type: Iterable[AceTariffType] | None = None,
        attribute_instance_component: Iterable[AttributeInstanceComponent] | None = None,
        domain: Iterable[Domain] | None = None,
        self_market_document: Iterable[MarketDocument] | None = None,
        market_document: Iterable[MarketDocument] | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        reason: Iterable[Reason] | None = None,
        date_and_or_time: Iterable[DateAndOrTime] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if process is not None:
            MarketDocument.process.extend(self, process)
        if period is not None:
            MarketDocument.period.extend(self, period)
        if market_participant is not None:
            MarketDocument.market_participant.extend(self, market_participant)
        if ace_tariff_type is not None:
            MarketDocument.ace_tariff_type.extend(self, ace_tariff_type)
        if attribute_instance_component is not None:
            MarketDocument.attribute_instance_component.extend(self, attribute_instance_component)
        if domain is not None:
            MarketDocument.domain.extend(self, domain)
        if self_market_document is not None:
            MarketDocument.self_market_document.extend(self, self_market_document)
        if market_document is not None:
            MarketDocument.market_document.extend(self, market_document)
        if time_series is not None:
            MarketDocument.time_series.extend(self, time_series)
        if reason is not None:
            MarketDocument.reason.extend(self, reason)
        if date_and_or_time is not None:
            MarketDocument.date_and_or_time.extend(self, date_and_or_time)

    def add_process(self, process: Process) -> Self:
        return MarketDocument.process.add(self, process)

    def remove_process(self, process: Process) -> Self:
        return MarketDocument.process.remove(self, process)

    def clear_process(self) -> Self:
        return MarketDocument.process.clear(self)

    def num_process(self) -> int:
        return MarketDocument.process.count(self)

    def get_process_by_mrid(self, mrid: str) -> Process | None:
        return MarketDocument.process.get_by_mrid(self, mrid)

    def add_period(self, period: Period) -> Self:
        return MarketDocument.period.add(self, period)

    def remove_period(self, period: Period) -> Self:
        return MarketDocument.period.remove(self, period)

    def clear_period(self) -> Self:
        return MarketDocument.period.clear(self)

    def num_period(self) -> int:
        return MarketDocument.period.count(self)

    def add_market_participant(self, market_participant: MarketParticipant) -> Self:
        return MarketDocument.market_participant.add(self, market_participant)

    def remove_market_participant(self, market_participant: MarketParticipant) -> Self:
        return MarketDocument.market_participant.remove(self, market_participant)

    def clear_market_participant(self) -> Self:
        return MarketDocument.market_participant.clear(self)

    def num_market_participant(self) -> int:
        return MarketDocument.market_participant.count(self)

    def get_market_participant_by_mrid(self, mrid: str) -> MarketParticipant | None:
        return MarketDocument.market_participant.get_by_mrid(self, mrid)

    def add_ace_tariff_type(self, ace_tariff_type: AceTariffType) -> Self:
        return MarketDocument.ace_tariff_type.add(self, ace_tariff_type)

    def remove_ace_tariff_type(self, ace_tariff_type: AceTariffType) -> Self:
        return MarketDocument.ace_tariff_type.remove(self, ace_tariff_type)

    def clear_ace_tariff_type(self) -> Self:
        return MarketDocument.ace_tariff_type.clear(self)

    def num_ace_tariff_type(self) -> int:
        return MarketDocument.ace_tariff_type.count(self)

    def add_attribute_instance_component(
        self, attribute_instance_component: AttributeInstanceComponent
    ) -> Self:
        return MarketDocument.attribute_instance_component.add(self, attribute_instance_component)

    def remove_attribute_instance_component(
        self, attribute_instance_component: AttributeInstanceComponent
    ) -> Self:
        return MarketDocument.attribute_instance_component.remove(
            self, attribute_instance_component
        )

    def clear_attribute_instance_component(self) -> Self:
        return MarketDocument.attribute_instance_component.clear(self)

    def num_attribute_instance_component(self) -> int:
        return MarketDocument.attribute_instance_component.count(self)

    def add_domain(self, domain: Domain) -> Self:
        return MarketDocument.domain.add(self, domain)

    def remove_domain(self, domain: Domain) -> Self:
        return MarketDocument.domain.remove(self, domain)

    def clear_domain(self) -> Self:
        return MarketDocument.domain.clear(self)

    def num_domain(self) -> int:
        return MarketDocument.domain.count(self)

    def get_domain_by_mrid(self, mrid: str) -> Domain | None:
        return MarketDocument.domain.get_by_mrid(self, mrid)

    def add_self_market_document(self, self_market_document: MarketDocument) -> Self:
        return MarketDocument.self_market_document.add(self, self_market_document)

    def remove_self_market_document(self, self_market_document: MarketDocument) -> Self:
        return MarketDocument.self_market_document.remove(self, self_market_document)

    def clear_self_market_document(self) -> Self:
        return MarketDocument.self_market_document.clear(self)

    def num_self_market_document(self) -> int:
        return MarketDocument.self_market_document.count(self)

    def get_self_market_document_by_mrid(self, mrid: str) -> MarketDocument | None:
        return MarketDocument.self_market_document.get_by_mrid(self, mrid)

    def add_market_document(self, market_document: MarketDocument) -> Self:
        return MarketDocument.market_document.add(self, market_document)

    def remove_market_document(self, market_document: MarketDocument) -> Self:
        return MarketDocument.market_document.remove(self, market_document)

    def clear_market_document(self) -> Self:
        return MarketDocument.market_document.clear(self)

    def num_market_document(self) -> int:
        return MarketDocument.market_document.count(self)

    def get_market_document_by_mrid(self, mrid: str) -> MarketDocument | None:
        return MarketDocument.market_document.get_by_mrid(self, mrid)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return MarketDocument.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return MarketDocument.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return MarketDocument.time_series.clear(self)

    def num_time_series(self) -> int:
        return MarketDocument.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return MarketDocument.time_series.get_by_mrid(self, mrid)

    def add_reason(self, reason: Reason) -> Self:
        return MarketDocument.reason.add(self, reason)

    def remove_reason(self, reason: Reason) -> Self:
        return MarketDocument.reason.remove(self, reason)

    def clear_reason(self) -> Self:
        return MarketDocument.reason.clear(self)

    def num_reason(self) -> int:
        return MarketDocument.reason.count(self)

    def add_date_and_or_time(self, date_and_or_time: DateAndOrTime) -> Self:
        return MarketDocument.date_and_or_time.add(self, date_and_or_time)

    def remove_date_and_or_time(self, date_and_or_time: DateAndOrTime) -> Self:
        return MarketDocument.date_and_or_time.remove(self, date_and_or_time)

    def clear_date_and_or_time(self) -> Self:
        return MarketDocument.date_and_or_time.clear(self)

    def num_date_and_or_time(self) -> int:
        return MarketDocument.date_and_or_time.count(self)

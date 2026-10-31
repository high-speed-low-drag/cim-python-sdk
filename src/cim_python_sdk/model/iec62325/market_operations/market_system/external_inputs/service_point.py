"""CIM class ServicePoint (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_path import (
        TransmissionPath,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_reservation import (
        TransmissionReservation,
    )


class ServicePoint(IdentifiedObject):
    """The defined termination points of a transmission path. Service points are defined from
    the viewpoint of the transmission service. Each service point is contained within (or on
    the boundary of) an interchange area. A service point is source or destination of a
    transaction."""

    __slots__ = (
        "_pod_transmission_path",
        "_por_transmission_path",
        "_sink_reservation",
        "_source_reservation",
    )

    pod_transmission_path: Many[TransmissionPath] = Many(
        EndMeta(
            name="pod_transmission_path",
            cim_role="PODTransmissionPath",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_path:TransmissionPath",
            many=True,
            lower=0,
            upper=None,
            inverse="delivery_point",
            aggregation="none",
        )
    )
    sink_reservation: Many[TransmissionReservation] = Many(
        EndMeta(
            name="sink_reservation",
            cim_role="SinkReservation",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_reservation:TransmissionReservation",
            many=True,
            lower=0,
            upper=None,
            inverse="sink",
            aggregation="none",
        )
    )
    por_transmission_path: Many[TransmissionPath] = Many(
        EndMeta(
            name="por_transmission_path",
            cim_role="PORTransmissionPath",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_path:TransmissionPath",
            many=True,
            lower=0,
            upper=None,
            inverse="point_of_receipt",
            aggregation="none",
        )
    )
    source_reservation: Many[TransmissionReservation] = Many(
        EndMeta(
            name="source_reservation",
            cim_role="SourceReservation",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_reservation:TransmissionReservation",
            many=True,
            lower=0,
            upper=None,
            inverse="source",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ServicePoint",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{E0569B00-C504-4bd4-BC15-97A64DA26866}",
        ends=(
            pod_transmission_path.meta,
            sink_reservation.meta,
            por_transmission_path.meta,
            source_reservation.meta,
        ),
    )

    def __init__(
        self,
        *,
        pod_transmission_path: Iterable[TransmissionPath] | None = None,
        sink_reservation: Iterable[TransmissionReservation] | None = None,
        por_transmission_path: Iterable[TransmissionPath] | None = None,
        source_reservation: Iterable[TransmissionReservation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if pod_transmission_path is not None:
            ServicePoint.pod_transmission_path.extend(self, pod_transmission_path)
        if sink_reservation is not None:
            ServicePoint.sink_reservation.extend(self, sink_reservation)
        if por_transmission_path is not None:
            ServicePoint.por_transmission_path.extend(self, por_transmission_path)
        if source_reservation is not None:
            ServicePoint.source_reservation.extend(self, source_reservation)

    def add_pod_transmission_path(self, pod_transmission_path: TransmissionPath) -> Self:
        return ServicePoint.pod_transmission_path.add(self, pod_transmission_path)

    def remove_pod_transmission_path(self, pod_transmission_path: TransmissionPath) -> Self:
        return ServicePoint.pod_transmission_path.remove(self, pod_transmission_path)

    def clear_pod_transmission_path(self) -> Self:
        return ServicePoint.pod_transmission_path.clear(self)

    def num_pod_transmission_path(self) -> int:
        return ServicePoint.pod_transmission_path.count(self)

    def get_pod_transmission_path_by_mrid(self, mrid: str) -> TransmissionPath | None:
        return ServicePoint.pod_transmission_path.get_by_mrid(self, mrid)

    def add_sink_reservation(self, sink_reservation: TransmissionReservation) -> Self:
        return ServicePoint.sink_reservation.add(self, sink_reservation)

    def remove_sink_reservation(self, sink_reservation: TransmissionReservation) -> Self:
        return ServicePoint.sink_reservation.remove(self, sink_reservation)

    def clear_sink_reservation(self) -> Self:
        return ServicePoint.sink_reservation.clear(self)

    def num_sink_reservation(self) -> int:
        return ServicePoint.sink_reservation.count(self)

    def add_por_transmission_path(self, por_transmission_path: TransmissionPath) -> Self:
        return ServicePoint.por_transmission_path.add(self, por_transmission_path)

    def remove_por_transmission_path(self, por_transmission_path: TransmissionPath) -> Self:
        return ServicePoint.por_transmission_path.remove(self, por_transmission_path)

    def clear_por_transmission_path(self) -> Self:
        return ServicePoint.por_transmission_path.clear(self)

    def num_por_transmission_path(self) -> int:
        return ServicePoint.por_transmission_path.count(self)

    def get_por_transmission_path_by_mrid(self, mrid: str) -> TransmissionPath | None:
        return ServicePoint.por_transmission_path.get_by_mrid(self, mrid)

    def add_source_reservation(self, source_reservation: TransmissionReservation) -> Self:
        return ServicePoint.source_reservation.add(self, source_reservation)

    def remove_source_reservation(self, source_reservation: TransmissionReservation) -> Self:
        return ServicePoint.source_reservation.remove(self, source_reservation)

    def clear_source_reservation(self) -> Self:
        return ServicePoint.source_reservation.clear(self)

    def num_source_reservation(self) -> int:
        return ServicePoint.source_reservation.count(self)

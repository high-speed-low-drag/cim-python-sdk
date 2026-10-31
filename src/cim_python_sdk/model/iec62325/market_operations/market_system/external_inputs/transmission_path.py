"""CIM class TransmissionPath (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.transmission_corridor import (
        TransmissionCorridor,
    )
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.transmission_product import (
        TransmissionProduct,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.service_point import (
        ServicePoint,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_reservation import (
        TransmissionReservation,
    )


class TransmissionPath(IdentifiedObject):
    """An electrical connection, link, or line consisting of one or more parallel transmission
    elements between two areas of the interconnected electric systems, or portions thereof.
    TransmissionCorridor and TransmissionRightOfWay refer to legal aspects. The
    TransmissionPath refers to the segments between a TransmissionProvider's ServicePoints."""

    __slots__ = (
        "_delivery_point",
        "_for_",
        "_located_on",
        "_point_of_receipt",
        "_transmission_reservation",
        "avail_transfer_capability",
        "parallel_path_flag",
        "total_transfer_capability",
    )

    avail_transfer_capability: float | None  # ActivePower
    parallel_path_flag: bool | None
    total_transfer_capability: float | None  # ActivePower

    delivery_point: One[ServicePoint] = One(
        EndMeta(
            name="delivery_point",
            cim_role="DeliveryPoint",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.service_point:ServicePoint",
            many=False,
            lower=1,
            upper=1,
            inverse="pod_transmission_path",
            aggregation="none",
        )
    )
    located_on: Many[TransmissionProduct] = Many(
        EndMeta(
            name="located_on",
            cim_role="LocatedOn",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_financial.transmission_product:TransmissionProduct",
            many=True,
            lower=0,
            upper=None,
            inverse="location_for",
            aggregation="none",
        )
    )
    point_of_receipt: One[ServicePoint] = One(
        EndMeta(
            name="point_of_receipt",
            cim_role="PointOfReceipt",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.service_point:ServicePoint",
            many=False,
            lower=1,
            upper=1,
            inverse="por_transmission_path",
            aggregation="none",
        )
    )
    for_: One[TransmissionCorridor] = One(
        EndMeta(
            name="for_",
            cim_role="For",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.transmission_corridor:TransmissionCorridor",
            many=False,
            lower=1,
            upper=1,
            inverse="contained_in",
            aggregation="none",
        )
    )
    transmission_reservation: Many[TransmissionReservation] = Many(
        EndMeta(
            name="transmission_reservation",
            cim_role="TransmissionReservation",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transmission_reservation:TransmissionReservation",
            many=True,
            lower=0,
            upper=None,
            inverse="transmission_path",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransmissionPath",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{44B2693F-73B9-4f42-B74F-067D411CDF55}",
        attributes=(
            AttrMeta(
                "avail_transfer_capability",
                "availTransferCapability",
                "ActivePower",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("parallel_path_flag", "parallelPathFlag", "bool", 0, 1, "primitive"),
            AttrMeta(
                "total_transfer_capability",
                "totalTransferCapability",
                "ActivePower",
                0,
                1,
                "cimdatatype",
            ),
        ),
        ends=(
            delivery_point.meta,
            located_on.meta,
            point_of_receipt.meta,
            for_.meta,
            transmission_reservation.meta,
        ),
    )

    def __init__(
        self,
        *,
        avail_transfer_capability: float | None = None,
        parallel_path_flag: bool | None = None,
        total_transfer_capability: float | None = None,
        delivery_point: ServicePoint | None = None,
        located_on: Iterable[TransmissionProduct] | None = None,
        point_of_receipt: ServicePoint | None = None,
        for_: TransmissionCorridor | None = None,
        transmission_reservation: Iterable[TransmissionReservation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.avail_transfer_capability = avail_transfer_capability
        self.parallel_path_flag = parallel_path_flag
        self.total_transfer_capability = total_transfer_capability
        if delivery_point is not None:
            self.delivery_point = delivery_point
        if located_on is not None:
            TransmissionPath.located_on.extend(self, located_on)
        if point_of_receipt is not None:
            self.point_of_receipt = point_of_receipt
        if for_ is not None:
            self.for_ = for_
        if transmission_reservation is not None:
            TransmissionPath.transmission_reservation.extend(self, transmission_reservation)

    def add_located_on(self, located_on: TransmissionProduct) -> Self:
        return TransmissionPath.located_on.add(self, located_on)

    def remove_located_on(self, located_on: TransmissionProduct) -> Self:
        return TransmissionPath.located_on.remove(self, located_on)

    def clear_located_on(self) -> Self:
        return TransmissionPath.located_on.clear(self)

    def num_located_on(self) -> int:
        return TransmissionPath.located_on.count(self)

    def get_located_on_by_mrid(self, mrid: str) -> TransmissionProduct | None:
        return TransmissionPath.located_on.get_by_mrid(self, mrid)

    def add_transmission_reservation(
        self, transmission_reservation: TransmissionReservation
    ) -> Self:
        return TransmissionPath.transmission_reservation.add(self, transmission_reservation)

    def remove_transmission_reservation(
        self, transmission_reservation: TransmissionReservation
    ) -> Self:
        return TransmissionPath.transmission_reservation.remove(self, transmission_reservation)

    def clear_transmission_reservation(self) -> Self:
        return TransmissionPath.transmission_reservation.clear(self)

    def num_transmission_reservation(self) -> int:
        return TransmissionPath.transmission_reservation.count(self)

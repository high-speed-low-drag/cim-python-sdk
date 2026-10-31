"""CIM class MarketObjectStatus (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class MarketObjectStatus(CimObject):
    """The condition or position of an object with regard to its standing."""

    __slots__ = ("_registered_resource", "_time_series", "status")

    status: str | None

    time_series: Many[TimeSeries] = Many(
        EndMeta(
            name="time_series",
            cim_role="TimeSeries",
            target="cim_python_sdk.model.iec62325.market_management.time_series:TimeSeries",
            many=True,
            lower=0,
            upper=None,
            inverse="market_object_status",
            aggregation="none",
        )
    )
    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="market_object_status",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MarketObjectStatus",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{DB7CC22D-A5B9-4978-9B03-155D3F3D7610}",
        attributes=(AttrMeta("status", "status", "str", 0, 1, "primitive"),),
        ends=(
            time_series.meta,
            registered_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        status: str | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if time_series is not None:
            MarketObjectStatus.time_series.extend(self, time_series)
        if registered_resource is not None:
            MarketObjectStatus.registered_resource.extend(self, registered_resource)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return MarketObjectStatus.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return MarketObjectStatus.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return MarketObjectStatus.time_series.clear(self)

    def num_time_series(self) -> int:
        return MarketObjectStatus.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return MarketObjectStatus.time_series.get_by_mrid(self, mrid)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return MarketObjectStatus.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return MarketObjectStatus.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return MarketObjectStatus.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return MarketObjectStatus.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return MarketObjectStatus.registered_resource.get_by_mrid(self, mrid)

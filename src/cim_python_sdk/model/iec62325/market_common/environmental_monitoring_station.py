"""CIM class EnvironmentalMonitoringStation (TC57CIM/IEC62325/MarketCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.location import Location
    from cim_python_sdk.model.iec61968.metering.usage_point import UsagePoint
    from cim_python_sdk.model.iec62325.environmental.environmental_analog import EnvironmentalAnalog
    from cim_python_sdk.model.iec62325.environmental.reporting_capability import ReportingCapability
    from cim_python_sdk.model.iec62325.market_management.time_series import TimeSeries


class EnvironmentalMonitoringStation(IdentifiedObject):
    """An environmental monitoring station, examples of which could be a weather station or a
    seismic monitoring station."""

    __slots__ = (
        "_environmental_analog",
        "_location",
        "_reporting_capability",
        "_time_series",
        "_usage_point",
        "dst_observed",
        "is_networked",
        "time_zone_offset",
    )

    dst_observed: bool | None
    is_networked: bool | None
    time_zone_offset: float | None  # Minutes

    usage_point: Many[UsagePoint] = Many(
        EndMeta(
            name="usage_point",
            cim_role="UsagePoint",
            target="cim_python_sdk.model.iec61968.metering.usage_point:UsagePoint",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_monitoring_station",
            aggregation="none",
        )
    )
    location: One[Location] = One(
        EndMeta(
            name="location",
            cim_role="Location",
            target="cim_python_sdk.model.iec61968.common.location:Location",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_monitoring_station",
            aggregation="none",
        )
    )
    reporting_capability: Many[ReportingCapability] = Many(
        EndMeta(
            name="reporting_capability",
            cim_role="ReportingCapability",
            target="cim_python_sdk.model.iec62325.environmental.reporting_capability:ReportingCapability",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_monitoring_station",
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
            inverse="environmental_monitoring_station",
            aggregation="none",
        )
    )
    environmental_analog: Many[EnvironmentalAnalog] = Many(
        EndMeta(
            name="environmental_analog",
            cim_role="EnvironmentalAnalog",
            target="cim_python_sdk.model.iec62325.environmental.environmental_analog:EnvironmentalAnalog",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_monitoring_station",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalMonitoringStation",
        package="TC57CIM/IEC62325/MarketCommon",
        guid="{C0EF36F4-1BF0-4f20-A428-819900BFFACA}",
        attributes=(
            AttrMeta("dst_observed", "dstObserved", "bool", 0, 1, "primitive"),
            AttrMeta("is_networked", "isNetworked", "bool", 0, 1, "primitive"),
            AttrMeta("time_zone_offset", "timeZoneOffset", "Minutes", 0, 1, "cimdatatype"),
        ),
        ends=(
            usage_point.meta,
            location.meta,
            reporting_capability.meta,
            time_series.meta,
            environmental_analog.meta,
        ),
    )

    def __init__(
        self,
        *,
        dst_observed: bool | None = None,
        is_networked: bool | None = None,
        time_zone_offset: float | None = None,
        usage_point: Iterable[UsagePoint] | None = None,
        location: Location | None = None,
        reporting_capability: Iterable[ReportingCapability] | None = None,
        time_series: Iterable[TimeSeries] | None = None,
        environmental_analog: Iterable[EnvironmentalAnalog] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dst_observed = dst_observed
        self.is_networked = is_networked
        self.time_zone_offset = time_zone_offset
        if usage_point is not None:
            EnvironmentalMonitoringStation.usage_point.extend(self, usage_point)
        if location is not None:
            self.location = location
        if reporting_capability is not None:
            EnvironmentalMonitoringStation.reporting_capability.extend(self, reporting_capability)
        if time_series is not None:
            EnvironmentalMonitoringStation.time_series.extend(self, time_series)
        if environmental_analog is not None:
            EnvironmentalMonitoringStation.environmental_analog.extend(self, environmental_analog)

    def add_usage_point(self, usage_point: UsagePoint) -> Self:
        return EnvironmentalMonitoringStation.usage_point.add(self, usage_point)

    def remove_usage_point(self, usage_point: UsagePoint) -> Self:
        return EnvironmentalMonitoringStation.usage_point.remove(self, usage_point)

    def clear_usage_point(self) -> Self:
        return EnvironmentalMonitoringStation.usage_point.clear(self)

    def num_usage_point(self) -> int:
        return EnvironmentalMonitoringStation.usage_point.count(self)

    def get_usage_point_by_mrid(self, mrid: str) -> UsagePoint | None:
        return EnvironmentalMonitoringStation.usage_point.get_by_mrid(self, mrid)

    def add_reporting_capability(self, reporting_capability: ReportingCapability) -> Self:
        return EnvironmentalMonitoringStation.reporting_capability.add(self, reporting_capability)

    def remove_reporting_capability(self, reporting_capability: ReportingCapability) -> Self:
        return EnvironmentalMonitoringStation.reporting_capability.remove(
            self, reporting_capability
        )

    def clear_reporting_capability(self) -> Self:
        return EnvironmentalMonitoringStation.reporting_capability.clear(self)

    def num_reporting_capability(self) -> int:
        return EnvironmentalMonitoringStation.reporting_capability.count(self)

    def add_time_series(self, time_series: TimeSeries) -> Self:
        return EnvironmentalMonitoringStation.time_series.add(self, time_series)

    def remove_time_series(self, time_series: TimeSeries) -> Self:
        return EnvironmentalMonitoringStation.time_series.remove(self, time_series)

    def clear_time_series(self) -> Self:
        return EnvironmentalMonitoringStation.time_series.clear(self)

    def num_time_series(self) -> int:
        return EnvironmentalMonitoringStation.time_series.count(self)

    def get_time_series_by_mrid(self, mrid: str) -> TimeSeries | None:
        return EnvironmentalMonitoringStation.time_series.get_by_mrid(self, mrid)

    def add_environmental_analog(self, environmental_analog: EnvironmentalAnalog) -> Self:
        return EnvironmentalMonitoringStation.environmental_analog.add(self, environmental_analog)

    def remove_environmental_analog(self, environmental_analog: EnvironmentalAnalog) -> Self:
        return EnvironmentalMonitoringStation.environmental_analog.remove(
            self, environmental_analog
        )

    def clear_environmental_analog(self) -> Self:
        return EnvironmentalMonitoringStation.environmental_analog.clear(self)

    def num_environmental_analog(self) -> int:
        return EnvironmentalMonitoringStation.environmental_analog.count(self)

    def get_environmental_analog_by_mrid(self, mrid: str) -> EnvironmentalAnalog | None:
        return EnvironmentalMonitoringStation.environmental_analog.get_by_mrid(self, mrid)

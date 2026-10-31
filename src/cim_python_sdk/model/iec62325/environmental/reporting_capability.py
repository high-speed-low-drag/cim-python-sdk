"""CIM class ReportingCapability (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_meas.calculation_interval_unit_kind import (
        CalculationIntervalUnitKind,
    )
    from cim_python_sdk.model.iec62325.environmental.env_domain.reporting_method_kind import (
        ReportingMethodKind,
    )
    from cim_python_sdk.model.iec62325.environmental.environmental_analog import EnvironmentalAnalog
    from cim_python_sdk.model.iec62325.market_common.environmental_monitoring_station import (
        EnvironmentalMonitoringStation,
    )


class ReportingCapability(CimObject):
    """Definition of one set of reporting capabilities for this monitoring station. The
    associated EnvironmentalValueSets describe the maximum range of possible environmental
    values the station is capable of returning. This attribute is intended primarily to
    assist a utility in managing its stations."""

    __slots__ = (
        "_environmental_analog",
        "_environmental_monitoring_station",
        "reporting_interval_period",
        "reporting_interval_type",
        "reporting_method",
    )

    reporting_interval_period: int | None
    reporting_interval_type: CalculationIntervalUnitKind | None
    reporting_method: ReportingMethodKind | None

    environmental_analog: Many[EnvironmentalAnalog] = Many(
        EndMeta(
            name="environmental_analog",
            cim_role="EnvironmentalAnalog",
            target="cim_python_sdk.model.iec62325.environmental.environmental_analog:EnvironmentalAnalog",
            many=True,
            lower=0,
            upper=None,
            inverse="reporting_capability",
            aggregation="none",
        )
    )
    environmental_monitoring_station: One[EnvironmentalMonitoringStation] = One(
        EndMeta(
            name="environmental_monitoring_station",
            cim_role="EnvironmentalMonitoringStation",
            target="cim_python_sdk.model.iec62325.market_common.environmental_monitoring_station:EnvironmentalMonitoringStation",
            many=False,
            lower=1,
            upper=1,
            inverse="reporting_capability",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ReportingCapability",
        package="TC57CIM/IEC62325/Environmental",
        guid="{32F281EE-89A4-4602-BB63-310AD3626494}",
        attributes=(
            AttrMeta(
                "reporting_interval_period", "reportingIntervalPeriod", "int", 0, 1, "primitive"
            ),
            AttrMeta(
                "reporting_interval_type",
                "reportingIntervalType",
                "CalculationIntervalUnitKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "reporting_method", "reportingMethod", "ReportingMethodKind", 0, 1, "enumeration"
            ),
        ),
        ends=(
            environmental_analog.meta,
            environmental_monitoring_station.meta,
        ),
    )

    def __init__(
        self,
        *,
        reporting_interval_period: int | None = None,
        reporting_interval_type: CalculationIntervalUnitKind | None = None,
        reporting_method: ReportingMethodKind | None = None,
        environmental_analog: Iterable[EnvironmentalAnalog] | None = None,
        environmental_monitoring_station: EnvironmentalMonitoringStation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.reporting_interval_period = reporting_interval_period
        self.reporting_interval_type = reporting_interval_type
        self.reporting_method = reporting_method
        if environmental_analog is not None:
            ReportingCapability.environmental_analog.extend(self, environmental_analog)
        if environmental_monitoring_station is not None:
            self.environmental_monitoring_station = environmental_monitoring_station

    def add_environmental_analog(self, environmental_analog: EnvironmentalAnalog) -> Self:
        return ReportingCapability.environmental_analog.add(self, environmental_analog)

    def remove_environmental_analog(self, environmental_analog: EnvironmentalAnalog) -> Self:
        return ReportingCapability.environmental_analog.remove(self, environmental_analog)

    def clear_environmental_analog(self) -> Self:
        return ReportingCapability.environmental_analog.clear(self)

    def num_environmental_analog(self) -> int:
        return ReportingCapability.environmental_analog.count(self)

    def get_environmental_analog_by_mrid(self, mrid: str) -> EnvironmentalAnalog | None:
        return ReportingCapability.environmental_analog.get_by_mrid(self, mrid)

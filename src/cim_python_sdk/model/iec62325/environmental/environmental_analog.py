"""CIM class EnvironmentalAnalog (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.analog import Analog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.environmental.classification_condition import (
        ClassificationCondition,
    )
    from cim_python_sdk.model.iec62325.environmental.environmental_information import (
        EnvironmentalInformation,
    )
    from cim_python_sdk.model.iec62325.environmental.reporting_capability import ReportingCapability
    from cim_python_sdk.model.iec62325.market_common.environmental_monitoring_station import (
        EnvironmentalMonitoringStation,
    )


class EnvironmentalAnalog(Analog):
    """Analog (float) measurement of relevance in the environmental domain."""

    __slots__ = (
        "_classification_condition",
        "_environmental_information",
        "_environmental_monitoring_station",
        "_reporting_capability",
    )

    reporting_capability: One[ReportingCapability] = One(
        EndMeta(
            name="reporting_capability",
            cim_role="ReportingCapability",
            target="cim_python_sdk.model.iec62325.environmental.reporting_capability:ReportingCapability",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_analog",
            aggregation="none",
        )
    )
    environmental_information: One[EnvironmentalInformation] = One(
        EndMeta(
            name="environmental_information",
            cim_role="EnvironmentalInformation",
            target="cim_python_sdk.model.iec62325.environmental.environmental_information:EnvironmentalInformation",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_analog",
            aggregation="none",
        )
    )
    classification_condition: One[ClassificationCondition] = One(
        EndMeta(
            name="classification_condition",
            cim_role="ClassificationCondition",
            target="cim_python_sdk.model.iec62325.environmental.classification_condition:ClassificationCondition",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_analog",
            aggregation="none",
        )
    )
    environmental_monitoring_station: One[EnvironmentalMonitoringStation] = One(
        EndMeta(
            name="environmental_monitoring_station",
            cim_role="EnvironmentalMonitoringStation",
            target="cim_python_sdk.model.iec62325.market_common.environmental_monitoring_station:EnvironmentalMonitoringStation",
            many=False,
            lower=0,
            upper=1,
            inverse="environmental_analog",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalAnalog",
        package="TC57CIM/IEC62325/Environmental",
        guid="{3FE893D1-3F9A-4b25-ADDB-5CF6191F2331}",
        ends=(
            reporting_capability.meta,
            environmental_information.meta,
            classification_condition.meta,
            environmental_monitoring_station.meta,
        ),
    )

    def __init__(
        self,
        *,
        reporting_capability: ReportingCapability | None = None,
        environmental_information: EnvironmentalInformation | None = None,
        classification_condition: ClassificationCondition | None = None,
        environmental_monitoring_station: EnvironmentalMonitoringStation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if reporting_capability is not None:
            self.reporting_capability = reporting_capability
        if environmental_information is not None:
            self.environmental_information = environmental_information
        if classification_condition is not None:
            self.classification_condition = classification_condition
        if environmental_monitoring_station is not None:
            self.environmental_monitoring_station = environmental_monitoring_station

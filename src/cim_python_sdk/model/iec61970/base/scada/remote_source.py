"""CIM class RemoteSource (TC57CIM/IEC61970/Base/SCADA). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.scada.remote_point import RemotePoint

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.measurement_value import MeasurementValue


class RemoteSource(RemotePoint):
    """Remote sources are state variables that are telemetered or calculated within the remote
    unit."""

    __slots__ = (
        "_measurement_value",
        "deadband",
        "scan_interval",
        "sensor_maximum",
        "sensor_minimum",
    )

    sensor_maximum: float | None
    sensor_minimum: float | None
    scan_interval: float | None  # Seconds
    deadband: float | None

    measurement_value: One[MeasurementValue] = One(
        EndMeta(
            name="measurement_value",
            cim_role="MeasurementValue",
            target="cim_python_sdk.model.iec61970.base.meas.measurement_value:MeasurementValue",
            many=False,
            lower=1,
            upper=1,
            inverse="remote_source",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RemoteSource",
        package="TC57CIM/IEC61970/Base/SCADA",
        guid="{CC135E99-5C6E-41ad-8FE4-E7EBEC8E0D8C}",
        attributes=(
            AttrMeta("sensor_maximum", "sensorMaximum", "float", 0, 1, "primitive"),
            AttrMeta("sensor_minimum", "sensorMinimum", "float", 0, 1, "primitive"),
            AttrMeta("scan_interval", "scanInterval", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("deadband", "deadband", "float", 0, 1, "primitive"),
        ),
        ends=(measurement_value.meta,),
    )

    def __init__(
        self,
        *,
        sensor_maximum: float | None = None,
        sensor_minimum: float | None = None,
        scan_interval: float | None = None,
        deadband: float | None = None,
        measurement_value: MeasurementValue | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sensor_maximum = sensor_maximum
        self.sensor_minimum = sensor_minimum
        self.scan_interval = scan_interval
        self.deadband = deadband
        if measurement_value is not None:
            self.measurement_value = measurement_value

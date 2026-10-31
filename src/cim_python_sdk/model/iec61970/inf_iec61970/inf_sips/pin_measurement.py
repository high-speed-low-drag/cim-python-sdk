"""CIM class PinMeasurement (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.gate_input_pin import GateInputPin

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.measurement_calculator import (
        MeasurementCalculator,
    )


class PinMeasurement(GateInputPin):
    """Gate input pin that is associated with a Measurement or a calculation of Measurement."""

    __slots__ = ("_measurement", "_measurement_calculator")

    measurement_calculator: One[MeasurementCalculator] = One(
        EndMeta(
            name="measurement_calculator",
            cim_role="MeasurementCalculator",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.measurement_calculator:MeasurementCalculator",
            many=False,
            lower=0,
            upper=1,
            inverse="pin_measurement",
            aggregation="none",
        )
    )
    measurement: One[Measurement] = One(
        EndMeta(
            name="measurement",
            cim_role="Measurement",
            target="cim_python_sdk.model.iec61970.base.meas.measurement:Measurement",
            many=False,
            lower=0,
            upper=1,
            inverse="pin_measurement",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PinMeasurement",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{8E12F655-DF68-4199-9B4F-59E5BF7467FF}",
        ends=(
            measurement_calculator.meta,
            measurement.meta,
        ),
    )

    def __init__(
        self,
        *,
        measurement_calculator: MeasurementCalculator | None = None,
        measurement: Measurement | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if measurement_calculator is not None:
            self.measurement_calculator = measurement_calculator
        if measurement is not None:
            self.measurement = measurement

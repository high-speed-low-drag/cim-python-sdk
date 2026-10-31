"""CIM class MeasurementCalculatorInput (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.measurement_calculator import (
        MeasurementCalculator,
    )


class MeasurementCalculatorInput(IdentifiedObject):
    """Input to measurement calculation. Support Analog, Discrete and Accumulator."""

    __slots__ = ("_measurement", "_measurement_calculator", "absolute_value", "order")

    absolute_value: bool | None
    order: int | None

    measurement: One[Measurement] = One(
        EndMeta(
            name="measurement",
            cim_role="Measurement",
            target="cim_python_sdk.model.iec61970.base.meas.measurement:Measurement",
            many=False,
            lower=1,
            upper=1,
            inverse="measurement_calculator_input",
            aggregation="none",
        )
    )
    measurement_calculator: One[MeasurementCalculator] = One(
        EndMeta(
            name="measurement_calculator",
            cim_role="MeasurementCalculator",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.measurement_calculator:MeasurementCalculator",
            many=False,
            lower=1,
            upper=1,
            inverse="measurement_calculator_input",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MeasurementCalculatorInput",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{74EA1CCE-5F3A-437b-B90E-3C4E02DE69A3}",
        attributes=(
            AttrMeta("absolute_value", "absoluteValue", "bool", 0, 1, "primitive"),
            AttrMeta("order", "order", "int", 0, 1, "primitive"),
        ),
        ends=(
            measurement.meta,
            measurement_calculator.meta,
        ),
    )

    def __init__(
        self,
        *,
        absolute_value: bool | None = None,
        order: int | None = None,
        measurement: Measurement | None = None,
        measurement_calculator: MeasurementCalculator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.absolute_value = absolute_value
        self.order = order
        if measurement is not None:
            self.measurement = measurement
        if measurement_calculator is not None:
            self.measurement_calculator = measurement_calculator

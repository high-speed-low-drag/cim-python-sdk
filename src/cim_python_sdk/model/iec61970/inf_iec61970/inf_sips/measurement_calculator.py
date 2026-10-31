"""CIM class MeasurementCalculator (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.calculation_kind import CalculationKind
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.measurement_calculator_input import (
        MeasurementCalculatorInput,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_measurement import PinMeasurement


class MeasurementCalculator(IdentifiedObject):
    """Result of a calculation of one or more measurement."""

    __slots__ = ("_measurement_calculator_input", "_pin_measurement", "kind")

    kind: CalculationKind | None

    pin_measurement: Many[PinMeasurement] = Many(
        EndMeta(
            name="pin_measurement",
            cim_role="PinMeasurement",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.pin_measurement:PinMeasurement",
            many=True,
            lower=0,
            upper=None,
            inverse="measurement_calculator",
            aggregation="none",
        )
    )
    measurement_calculator_input: Many[MeasurementCalculatorInput] = Many(
        EndMeta(
            name="measurement_calculator_input",
            cim_role="MeasurementCalculatorInput",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.measurement_calculator_input:MeasurementCalculatorInput",
            many=True,
            lower=1,
            upper=None,
            inverse="measurement_calculator",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MeasurementCalculator",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{87497F71-8E8B-4b4f-ADA0-35E128E5812C}",
        attributes=(AttrMeta("kind", "kind", "CalculationKind", 0, 1, "enumeration"),),
        ends=(
            pin_measurement.meta,
            measurement_calculator_input.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: CalculationKind | None = None,
        pin_measurement: Iterable[PinMeasurement] | None = None,
        measurement_calculator_input: Iterable[MeasurementCalculatorInput] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if pin_measurement is not None:
            MeasurementCalculator.pin_measurement.extend(self, pin_measurement)
        if measurement_calculator_input is not None:
            MeasurementCalculator.measurement_calculator_input.extend(
                self, measurement_calculator_input
            )

    def add_pin_measurement(self, pin_measurement: PinMeasurement) -> Self:
        return MeasurementCalculator.pin_measurement.add(self, pin_measurement)

    def remove_pin_measurement(self, pin_measurement: PinMeasurement) -> Self:
        return MeasurementCalculator.pin_measurement.remove(self, pin_measurement)

    def clear_pin_measurement(self) -> Self:
        return MeasurementCalculator.pin_measurement.clear(self)

    def num_pin_measurement(self) -> int:
        return MeasurementCalculator.pin_measurement.count(self)

    def get_pin_measurement_by_mrid(self, mrid: str) -> PinMeasurement | None:
        return MeasurementCalculator.pin_measurement.get_by_mrid(self, mrid)

    def add_measurement_calculator_input(
        self, measurement_calculator_input: MeasurementCalculatorInput
    ) -> Self:
        return MeasurementCalculator.measurement_calculator_input.add(
            self, measurement_calculator_input
        )

    def remove_measurement_calculator_input(
        self, measurement_calculator_input: MeasurementCalculatorInput
    ) -> Self:
        return MeasurementCalculator.measurement_calculator_input.remove(
            self, measurement_calculator_input
        )

    def clear_measurement_calculator_input(self) -> Self:
        return MeasurementCalculator.measurement_calculator_input.clear(self)

    def num_measurement_calculator_input(self) -> int:
        return MeasurementCalculator.measurement_calculator_input.count(self)

    def get_measurement_calculator_input_by_mrid(
        self, mrid: str
    ) -> MeasurementCalculatorInput | None:
        return MeasurementCalculator.measurement_calculator_input.get_by_mrid(self, mrid)

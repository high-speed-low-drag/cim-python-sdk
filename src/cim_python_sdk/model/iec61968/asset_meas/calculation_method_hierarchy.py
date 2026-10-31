"""CIM class CalculationMethodHierarchy (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_meas.calculation_method_order import (
        CalculationMethodOrder,
    )
    from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement
    from cim_python_sdk.model.iec61970.base.meas.measurement_value import MeasurementValue


class CalculationMethodHierarchy(IdentifiedObject):
    """The hierarchy of calculation methods used to derive this measurement.

    ."""

    __slots__ = ("_calculation_method_order", "_measurement", "_measurement_value")

    calculation_method_order: Many[CalculationMethodOrder] = Many(
        EndMeta(
            name="calculation_method_order",
            cim_role="CalculationMethodOrder",
            target="cim_python_sdk.model.iec61968.asset_meas.calculation_method_order:CalculationMethodOrder",
            many=True,
            lower=0,
            upper=None,
            inverse="calculation_method_hierarchy",
            aggregation="none",
        )
    )
    measurement_value: One[MeasurementValue] = One(
        EndMeta(
            name="measurement_value",
            cim_role="MeasurementValue",
            target="cim_python_sdk.model.iec61970.base.meas.measurement_value:MeasurementValue",
            many=False,
            lower=0,
            upper=1,
            inverse="calculation_method_hierarchy",
            aggregation="none",
        )
    )
    measurement: Many[Measurement] = Many(
        EndMeta(
            name="measurement",
            cim_role="Measurement",
            target="cim_python_sdk.model.iec61970.base.meas.measurement:Measurement",
            many=True,
            lower=0,
            upper=None,
            inverse="calculation_method_hierarchy",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CalculationMethodHierarchy",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{714364FE-E1F5-4ccd-85DC-31D2161624AB}",
        ends=(
            calculation_method_order.meta,
            measurement_value.meta,
            measurement.meta,
        ),
    )

    def __init__(
        self,
        *,
        calculation_method_order: Iterable[CalculationMethodOrder] | None = None,
        measurement_value: MeasurementValue | None = None,
        measurement: Iterable[Measurement] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if calculation_method_order is not None:
            CalculationMethodHierarchy.calculation_method_order.extend(
                self, calculation_method_order
            )
        if measurement_value is not None:
            self.measurement_value = measurement_value
        if measurement is not None:
            CalculationMethodHierarchy.measurement.extend(self, measurement)

    def add_calculation_method_order(
        self, calculation_method_order: CalculationMethodOrder
    ) -> Self:
        return CalculationMethodHierarchy.calculation_method_order.add(
            self, calculation_method_order
        )

    def remove_calculation_method_order(
        self, calculation_method_order: CalculationMethodOrder
    ) -> Self:
        return CalculationMethodHierarchy.calculation_method_order.remove(
            self, calculation_method_order
        )

    def clear_calculation_method_order(self) -> Self:
        return CalculationMethodHierarchy.calculation_method_order.clear(self)

    def num_calculation_method_order(self) -> int:
        return CalculationMethodHierarchy.calculation_method_order.count(self)

    def add_measurement(self, measurement: Measurement) -> Self:
        return CalculationMethodHierarchy.measurement.add(self, measurement)

    def remove_measurement(self, measurement: Measurement) -> Self:
        return CalculationMethodHierarchy.measurement.remove(self, measurement)

    def clear_measurement(self) -> Self:
        return CalculationMethodHierarchy.measurement.clear(self)

    def num_measurement(self) -> int:
        return CalculationMethodHierarchy.measurement.count(self)

    def get_measurement_by_mrid(self, mrid: str) -> Measurement | None:
        return CalculationMethodHierarchy.measurement.get_by_mrid(self, mrid)

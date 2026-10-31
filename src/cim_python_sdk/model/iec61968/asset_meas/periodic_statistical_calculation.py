"""CIM class PeriodicStatisticalCalculation (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.asset_meas.statistical_calculation import StatisticalCalculation

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.calculation_interval_unit_kind import (
        CalculationIntervalUnitKind,
    )


class PeriodicStatisticalCalculation(StatisticalCalculation):
    """Description of period for which calculation is performed."""

    __slots__ = ("calculation_interval_magnitude", "calculation_interval_unit")

    calculation_interval_unit: CalculationIntervalUnitKind | None
    calculation_interval_magnitude: int | None

    _cim_meta = ClassMeta(
        cim_name="PeriodicStatisticalCalculation",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{9265203F-579B-440d-B1AA-75F8EB309D82}",
        attributes=(
            AttrMeta(
                "calculation_interval_unit",
                "calculationIntervalUnit",
                "CalculationIntervalUnitKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "calculation_interval_magnitude",
                "calculationIntervalMagnitude",
                "int",
                0,
                1,
                "primitive",
            ),
        ),
    )

    def __init__(
        self,
        *,
        calculation_interval_unit: CalculationIntervalUnitKind | None = None,
        calculation_interval_magnitude: int | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.calculation_interval_unit = calculation_interval_unit
        self.calculation_interval_magnitude = calculation_interval_magnitude

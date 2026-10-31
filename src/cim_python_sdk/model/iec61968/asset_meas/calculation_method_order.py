"""CIM class CalculationMethodOrder (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_meas.calculation_method_hierarchy import (
        CalculationMethodHierarchy,
    )
    from cim_python_sdk.model.iec61968.asset_meas.statistical_calculation import (
        StatisticalCalculation,
    )


class CalculationMethodOrder(CimObject):
    """The order of this calculation method in a hierarchy of calculation methods."""

    __slots__ = ("_calculation_method_hierarchy", "_statisical_calculation", "order")

    order: int | None

    calculation_method_hierarchy: One[CalculationMethodHierarchy] = One(
        EndMeta(
            name="calculation_method_hierarchy",
            cim_role="CalculationMethodHierarchy",
            target="cim_python_sdk.model.iec61968.asset_meas.calculation_method_hierarchy:CalculationMethodHierarchy",
            many=False,
            lower=1,
            upper=1,
            inverse="calculation_method_order",
            aggregation="none",
        )
    )
    statisical_calculation: One[StatisticalCalculation] = One(
        EndMeta(
            name="statisical_calculation",
            cim_role="StatisicalCalculation",
            target="cim_python_sdk.model.iec61968.asset_meas.statistical_calculation:StatisticalCalculation",
            many=False,
            lower=1,
            upper=1,
            inverse="calculation_method_order",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CalculationMethodOrder",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{7B6358E2-AA72-4ceb-AF3A-F6D39E42FEA6}",
        attributes=(AttrMeta("order", "order", "int", 1, 1, "primitive"),),
        ends=(
            calculation_method_hierarchy.meta,
            statisical_calculation.meta,
        ),
    )

    def __init__(
        self,
        *,
        order: int | None = None,
        calculation_method_hierarchy: CalculationMethodHierarchy | None = None,
        statisical_calculation: StatisticalCalculation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.order = order
        if calculation_method_hierarchy is not None:
            self.calculation_method_hierarchy = calculation_method_hierarchy
        if statisical_calculation is not None:
            self.statisical_calculation = statisical_calculation

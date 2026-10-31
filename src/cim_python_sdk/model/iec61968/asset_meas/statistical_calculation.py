"""CIM class StatisticalCalculation (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_meas.calculation_method_order import (
        CalculationMethodOrder,
    )
    from cim_python_sdk.model.iec61968.asset_meas.calculation_mode_kind import CalculationModeKind
    from cim_python_sdk.model.iec61968.asset_meas.calculation_technique_kind import (
        CalculationTechniqueKind,
    )


class StatisticalCalculation(IdentifiedObject):
    """Description of statistical calculation performed."""

    __slots__ = ("_calculation_method_order", "calculation_mode", "calculation_technique")

    calculation_technique: CalculationTechniqueKind | None
    calculation_mode: CalculationModeKind | None

    calculation_method_order: Many[CalculationMethodOrder] = Many(
        EndMeta(
            name="calculation_method_order",
            cim_role="CalculationMethodOrder",
            target="cim_python_sdk.model.iec61968.asset_meas.calculation_method_order:CalculationMethodOrder",
            many=True,
            lower=0,
            upper=None,
            inverse="statisical_calculation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StatisticalCalculation",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{1FDD4916-3696-4ea3-9481-85106E3296DE}",
        attributes=(
            AttrMeta(
                "calculation_technique",
                "calculationTechnique",
                "CalculationTechniqueKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "calculation_mode", "calculationMode", "CalculationModeKind", 0, 1, "enumeration"
            ),
        ),
        ends=(calculation_method_order.meta,),
    )

    def __init__(
        self,
        *,
        calculation_technique: CalculationTechniqueKind | None = None,
        calculation_mode: CalculationModeKind | None = None,
        calculation_method_order: Iterable[CalculationMethodOrder] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.calculation_technique = calculation_technique
        self.calculation_mode = calculation_mode
        if calculation_method_order is not None:
            StatisticalCalculation.calculation_method_order.extend(self, calculation_method_order)

    def add_calculation_method_order(
        self, calculation_method_order: CalculationMethodOrder
    ) -> Self:
        return StatisticalCalculation.calculation_method_order.add(self, calculation_method_order)

    def remove_calculation_method_order(
        self, calculation_method_order: CalculationMethodOrder
    ) -> Self:
        return StatisticalCalculation.calculation_method_order.remove(
            self, calculation_method_order
        )

    def clear_calculation_method_order(self) -> Self:
        return StatisticalCalculation.calculation_method_order.clear(self)

    def num_calculation_method_order(self) -> int:
        return StatisticalCalculation.calculation_method_order.count(self)

"""CIM class TemperaturePolynomialLimit (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.environmental_dependent_limit import (
    EnvironmentalDependentLimit,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class TemperaturePolynomialLimit(EnvironmentalDependentLimit):
    """This describes the coefficients of a polynomial function that has temperature as input
    and calculates limit values as output."""

    __slots__ = ("coefficient0", "coefficient1", "coefficient2", "coefficient3", "coefficient4")

    coefficient0: float | None
    coefficient1: float | None
    coefficient2: float | None
    coefficient3: float | None
    coefficient4: float | None

    _cim_meta = ClassMeta(
        cim_name="TemperaturePolynomialLimit",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{D7320B08-B289-41d0-BC42-2F471427A93B}",
        attributes=(
            AttrMeta("coefficient0", "coefficient0", "float", 0, 1, "primitive"),
            AttrMeta("coefficient1", "coefficient1", "float", 0, 1, "primitive"),
            AttrMeta("coefficient2", "coefficient2", "float", 0, 1, "primitive"),
            AttrMeta("coefficient3", "coefficient3", "float", 0, 1, "primitive"),
            AttrMeta("coefficient4", "coefficient4", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        coefficient0: float | None = None,
        coefficient1: float | None = None,
        coefficient2: float | None = None,
        coefficient3: float | None = None,
        coefficient4: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.coefficient0 = coefficient0
        self.coefficient1 = coefficient1
        self.coefficient2 = coefficient2
        self.coefficient3 = coefficient3
        self.coefficient4 = coefficient4

"""CIM class EmissionCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.emission_type import EmissionType
    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class EmissionCurve(Curve):
    """Relationship between the unit's emission rate in units of mass per hour (Y-axis) and
    output active power (X-axis) for a given type of emission. This curve applies when only
    one type of fuel is being burned."""

    __slots__ = ("_thermal_generating_unit", "emission_content", "emission_type", "is_net_gross_p")

    emission_content: float | None  # Emission
    emission_type: EmissionType | None
    is_net_gross_p: bool | None

    thermal_generating_unit: One[ThermalGeneratingUnit] = One(
        EndMeta(
            name="thermal_generating_unit",
            cim_role="ThermalGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit:ThermalGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="emission_curves",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EmissionCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{A694A74C-046A-40e2-8A0F-EB8CC8F81BCD}",
        attributes=(
            AttrMeta("emission_content", "emissionContent", "Emission", 0, 1, "cimdatatype"),
            AttrMeta("emission_type", "emissionType", "EmissionType", 0, 1, "enumeration"),
            AttrMeta("is_net_gross_p", "isNetGrossP", "bool", 0, 1, "primitive"),
        ),
        ends=(thermal_generating_unit.meta,),
    )

    def __init__(
        self,
        *,
        emission_content: float | None = None,
        emission_type: EmissionType | None = None,
        is_net_gross_p: bool | None = None,
        thermal_generating_unit: ThermalGeneratingUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.emission_content = emission_content
        self.emission_type = emission_type
        self.is_net_gross_p = is_net_gross_p
        if thermal_generating_unit is not None:
            self.thermal_generating_unit = thermal_generating_unit

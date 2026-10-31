"""CIM class EmissionAccount (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.emission_type import EmissionType
    from cim_python_sdk.model.iec61970.base.generation.production.emission_value_source import (
        EmissionValueSource,
    )
    from cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit import (
        ThermalGeneratingUnit,
    )


class EmissionAccount(Curve):
    """Accounts for tracking emissions usage and credits for thermal generating units. A unit
    may have zero or more emission accounts, and will typically have one for tracking usage
    and one for tracking credits."""

    __slots__ = ("_thermal_generating_unit", "emission_type", "emission_value_source")

    emission_type: EmissionType | None
    emission_value_source: EmissionValueSource | None

    thermal_generating_unit: One[ThermalGeneratingUnit] = One(
        EndMeta(
            name="thermal_generating_unit",
            cim_role="ThermalGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.generation.production.thermal_generating_unit:ThermalGeneratingUnit",
            many=False,
            lower=1,
            upper=1,
            inverse="emmission_accounts",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EmissionAccount",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{86DC2BBA-08D4-4334-99C1-D40983F7F1AF}",
        attributes=(
            AttrMeta("emission_type", "emissionType", "EmissionType", 0, 1, "enumeration"),
            AttrMeta(
                "emission_value_source",
                "emissionValueSource",
                "EmissionValueSource",
                0,
                1,
                "enumeration",
            ),
        ),
        ends=(thermal_generating_unit.meta,),
    )

    def __init__(
        self,
        *,
        emission_type: EmissionType | None = None,
        emission_value_source: EmissionValueSource | None = None,
        thermal_generating_unit: ThermalGeneratingUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.emission_type = emission_type
        self.emission_value_source = emission_value_source
        if thermal_generating_unit is not None:
            self.thermal_generating_unit = thermal_generating_unit

"""CIM class CTTempActivePowerCurve (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.combustion_turbine import (
        CombustionTurbine,
    )


class CTTempActivePowerCurve(Curve):
    """Relationship between the combustion turbine's power output rating in gross active power
    (X-axis) and the ambient air temperature (Y-axis)."""

    __slots__ = ("_combustion_turbine",)

    combustion_turbine: One[CombustionTurbine] = One(
        EndMeta(
            name="combustion_turbine",
            cim_role="CombustionTurbine",
            target="cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.combustion_turbine:CombustionTurbine",
            many=False,
            lower=1,
            upper=1,
            inverse="ct_temp_active_power_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CTTempActivePowerCurve",
        package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
        guid="{69CCCEA0-DD09-4921-ABE4-D02ABF02888D}",
        ends=(combustion_turbine.meta,),
    )

    def __init__(
        self,
        *,
        combustion_turbine: CombustionTurbine | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if combustion_turbine is not None:
            self.combustion_turbine = combustion_turbine

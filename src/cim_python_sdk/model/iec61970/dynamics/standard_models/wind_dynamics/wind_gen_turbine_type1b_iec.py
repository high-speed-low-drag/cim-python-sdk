"""CIM class WindGenTurbineType1bIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_iec import (
    WindTurbineType1or2IEC,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_pitch_cont_power_iec import (
        WindPitchContPowerIEC,
    )


class WindGenTurbineType1bIEC(WindTurbineType1or2IEC):
    """Wind turbine IEC type 1B.

    Reference: IEC 61400-27-1:2015, 5.5.2.3."""

    __slots__ = ("_wind_pitch_cont_power_iec",)

    wind_pitch_cont_power_iec: One[WindPitchContPowerIEC] = One(
        EndMeta(
            name="wind_pitch_cont_power_iec",
            cim_role="WindPitchContPowerIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_pitch_cont_power_iec:WindPitchContPowerIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_gen_turbine_type1b_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindGenTurbineType1bIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{22011117-A0F2-475f-80B5-9008F7AB29E6}",
        ends=(wind_pitch_cont_power_iec.meta,),
    )

    def __init__(
        self,
        *,
        wind_pitch_cont_power_iec: WindPitchContPowerIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_pitch_cont_power_iec is not None:
            self.wind_pitch_cont_power_iec = wind_pitch_cont_power_iec

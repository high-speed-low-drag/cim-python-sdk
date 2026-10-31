"""CIM class WindGenTurbineType2IEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_iec import (
    WindTurbineType1or2IEC,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_rotor_riec import (
        WindContRotorRIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_pitch_cont_power_iec import (
        WindPitchContPowerIEC,
    )


class WindGenTurbineType2IEC(WindTurbineType1or2IEC):
    """Wind turbine IEC type 2.

    Reference: IEC 61400-27-1:2015, 5.5.3."""

    __slots__ = ("_wind_cont_rotor_riec", "_wind_pitch_cont_power_iec")

    wind_pitch_cont_power_iec: One[WindPitchContPowerIEC] = One(
        EndMeta(
            name="wind_pitch_cont_power_iec",
            cim_role="WindPitchContPowerIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_pitch_cont_power_iec:WindPitchContPowerIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_gen_turbine_type2_iec",
            aggregation="none",
        )
    )
    wind_cont_rotor_riec: One[WindContRotorRIEC] = One(
        EndMeta(
            name="wind_cont_rotor_riec",
            cim_role="WindContRotorRIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_rotor_riec:WindContRotorRIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_gen_turbine_type2_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindGenTurbineType2IEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{AB2082A1-658B-459c-86F7-E0256B0793F6}",
        ends=(
            wind_pitch_cont_power_iec.meta,
            wind_cont_rotor_riec.meta,
        ),
    )

    def __init__(
        self,
        *,
        wind_pitch_cont_power_iec: WindPitchContPowerIEC | None = None,
        wind_cont_rotor_riec: WindContRotorRIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_pitch_cont_power_iec is not None:
            self.wind_pitch_cont_power_iec = wind_pitch_cont_power_iec
        if wind_cont_rotor_riec is not None:
            self.wind_cont_rotor_riec = wind_cont_rotor_riec

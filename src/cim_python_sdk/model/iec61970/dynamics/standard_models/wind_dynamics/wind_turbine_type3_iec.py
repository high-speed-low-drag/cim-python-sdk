"""CIM class WindTurbineType3IEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec import (
    WindTurbineType3or4IEC,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_aero_one_dim_iec import (
        WindAeroOneDimIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_aero_two_dim_iec import (
        WindAeroTwoDimIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_p_type3_iec import (
        WindContPType3IEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_pitch_angle_iec import (
        WindContPitchAngleIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type3_iec import (
        WindGenType3IEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_mech_iec import (
        WindMechIEC,
    )


class WindTurbineType3IEC(WindTurbineType3or4IEC):
    """Parent class supporting relationships to IEC wind turbines type 3 including their
    control models."""

    __slots__ = (
        "_wind_aero_one_dim_iec",
        "_wind_aero_two_dim_iec",
        "_wind_cont_p_type3_iec",
        "_wind_cont_pitch_angle_iec",
        "_wind_gen_type3_iec",
        "_wind_mech_iec",
    )

    wind_aero_one_dim_iec: One[WindAeroOneDimIEC] = One(
        EndMeta(
            name="wind_aero_one_dim_iec",
            cim_role="WindAeroOneDimIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_aero_one_dim_iec:WindAeroOneDimIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_turbine_type3_iec",
            aggregation="none",
        )
    )
    wind_cont_p_type3_iec: One[WindContPType3IEC] = One(
        EndMeta(
            name="wind_cont_p_type3_iec",
            cim_role="WindContPType3IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_p_type3_iec:WindContPType3IEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type3_iec",
            aggregation="none",
        )
    )
    wind_gen_type3_iec: One[WindGenType3IEC] = One(
        EndMeta(
            name="wind_gen_type3_iec",
            cim_role="WindGenType3IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type3_iec:WindGenType3IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_turbine_type3_iec",
            aggregation="none",
        )
    )
    wind_cont_pitch_angle_iec: One[WindContPitchAngleIEC] = One(
        EndMeta(
            name="wind_cont_pitch_angle_iec",
            cim_role="WindContPitchAngleIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_pitch_angle_iec:WindContPitchAngleIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type3_iec",
            aggregation="none",
        )
    )
    wind_mech_iec: One[WindMechIEC] = One(
        EndMeta(
            name="wind_mech_iec",
            cim_role="WindMechIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_mech_iec:WindMechIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type3_iec",
            aggregation="none",
        )
    )
    wind_aero_two_dim_iec: One[WindAeroTwoDimIEC] = One(
        EndMeta(
            name="wind_aero_two_dim_iec",
            cim_role="WindAeroTwoDimIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_aero_two_dim_iec:WindAeroTwoDimIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_turbine_type3_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindTurbineType3IEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{376190F0-3641-4391-A5C7-E7529CC5D0B4}",
        ends=(
            wind_aero_one_dim_iec.meta,
            wind_cont_p_type3_iec.meta,
            wind_gen_type3_iec.meta,
            wind_cont_pitch_angle_iec.meta,
            wind_mech_iec.meta,
            wind_aero_two_dim_iec.meta,
        ),
    )

    def __init__(
        self,
        *,
        wind_aero_one_dim_iec: WindAeroOneDimIEC | None = None,
        wind_cont_p_type3_iec: WindContPType3IEC | None = None,
        wind_gen_type3_iec: WindGenType3IEC | None = None,
        wind_cont_pitch_angle_iec: WindContPitchAngleIEC | None = None,
        wind_mech_iec: WindMechIEC | None = None,
        wind_aero_two_dim_iec: WindAeroTwoDimIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_aero_one_dim_iec is not None:
            self.wind_aero_one_dim_iec = wind_aero_one_dim_iec
        if wind_cont_p_type3_iec is not None:
            self.wind_cont_p_type3_iec = wind_cont_p_type3_iec
        if wind_gen_type3_iec is not None:
            self.wind_gen_type3_iec = wind_gen_type3_iec
        if wind_cont_pitch_angle_iec is not None:
            self.wind_cont_pitch_angle_iec = wind_cont_pitch_angle_iec
        if wind_mech_iec is not None:
            self.wind_mech_iec = wind_mech_iec
        if wind_aero_two_dim_iec is not None:
            self.wind_aero_two_dim_iec = wind_aero_two_dim_iec

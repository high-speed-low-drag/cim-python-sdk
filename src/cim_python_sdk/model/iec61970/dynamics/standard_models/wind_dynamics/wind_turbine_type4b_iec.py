"""CIM class WindTurbineType4bIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4_iec import (
    WindTurbineType4IEC,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_p_type4b_iec import (
        WindContPType4bIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type4_iec import (
        WindGenType4IEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_mech_iec import (
        WindMechIEC,
    )


class WindTurbineType4bIEC(WindTurbineType4IEC):
    """Wind turbine IEC type 4B.

    Reference: IEC 61400-27-1:2015, 5.5.5.3."""

    __slots__ = ("_wind_cont_p_type4b_iec", "_wind_gen_type4_iec", "_wind_mech_iec")

    wind_cont_p_type4b_iec: One[WindContPType4bIEC] = One(
        EndMeta(
            name="wind_cont_p_type4b_iec",
            cim_role="WindContPType4bIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_p_type4b_iec:WindContPType4bIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type4b_iec",
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
            inverse="wind_turbine_type4b_iec",
            aggregation="none",
        )
    )
    wind_gen_type4_iec: One[WindGenType4IEC] = One(
        EndMeta(
            name="wind_gen_type4_iec",
            cim_role="WindGenType4IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type4_iec:WindGenType4IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_turbine_type4b_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindTurbineType4bIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{F255323C-ABF7-4552-B1BB-7C4F99632F6B}",
        ends=(
            wind_cont_p_type4b_iec.meta,
            wind_mech_iec.meta,
            wind_gen_type4_iec.meta,
        ),
    )

    def __init__(
        self,
        *,
        wind_cont_p_type4b_iec: WindContPType4bIEC | None = None,
        wind_mech_iec: WindMechIEC | None = None,
        wind_gen_type4_iec: WindGenType4IEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_cont_p_type4b_iec is not None:
            self.wind_cont_p_type4b_iec = wind_cont_p_type4b_iec
        if wind_mech_iec is not None:
            self.wind_mech_iec = wind_mech_iec
        if wind_gen_type4_iec is not None:
            self.wind_gen_type4_iec = wind_gen_type4_iec

"""CIM class WindTurbineType4aIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4_iec import (
    WindTurbineType4IEC,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_p_type4a_iec import (
        WindContPType4aIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type4_iec import (
        WindGenType4IEC,
    )


class WindTurbineType4aIEC(WindTurbineType4IEC):
    """Wind turbine IEC type 4A.

    Reference: IEC 61400-27-1:2015, 5.5.5.2."""

    __slots__ = ("_wind_cont_p_type4a_iec", "_wind_gen_type4_iec")

    wind_gen_type4_iec: One[WindGenType4IEC] = One(
        EndMeta(
            name="wind_gen_type4_iec",
            cim_role="WindGenType4IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type4_iec:WindGenType4IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_turbine_type4a_iec",
            aggregation="none",
        )
    )
    wind_cont_p_type4a_iec: One[WindContPType4aIEC] = One(
        EndMeta(
            name="wind_cont_p_type4a_iec",
            cim_role="WindContPType4aIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_cont_p_type4a_iec:WindContPType4aIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_turbine_type4a_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindTurbineType4aIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{1E6625D5-29E9-40db-B610-03E29C878925}",
        ends=(
            wind_gen_type4_iec.meta,
            wind_cont_p_type4a_iec.meta,
        ),
    )

    def __init__(
        self,
        *,
        wind_gen_type4_iec: WindGenType4IEC | None = None,
        wind_cont_p_type4a_iec: WindContPType4aIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_gen_type4_iec is not None:
            self.wind_gen_type4_iec = wind_gen_type4_iec
        if wind_cont_p_type4a_iec is not None:
            self.wind_cont_p_type4a_iec = wind_cont_p_type4a_iec

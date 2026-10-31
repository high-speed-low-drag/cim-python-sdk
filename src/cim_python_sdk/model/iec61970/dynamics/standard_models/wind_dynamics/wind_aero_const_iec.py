"""CIM class WindAeroConstIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_turbine_type1a_iec import (
        WindGenTurbineType1aIEC,
    )


class WindAeroConstIEC(IdentifiedObject):
    """Constant aerodynamic torque model which assumes that the aerodynamic torque is constant.

    Reference: IEC 61400-27-1:2015, 5.6.1.1."""

    __slots__ = ("_wind_gen_turbine_type1a_iec",)

    wind_gen_turbine_type1a_iec: One[WindGenTurbineType1aIEC] = One(
        EndMeta(
            name="wind_gen_turbine_type1a_iec",
            cim_role="WindGenTurbineType1aIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_turbine_type1a_iec:WindGenTurbineType1aIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_aero_const_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindAeroConstIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{383DDCA3-2DB5-4005-9AD9-ED86EB3FDCC5}",
        ends=(wind_gen_turbine_type1a_iec.meta,),
    )

    def __init__(
        self,
        *,
        wind_gen_turbine_type1a_iec: WindGenTurbineType1aIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_gen_turbine_type1a_iec is not None:
            self.wind_gen_turbine_type1a_iec = wind_gen_turbine_type1a_iec

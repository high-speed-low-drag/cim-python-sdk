"""CIM class WindGenTurbineType1aIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_iec import (
    WindTurbineType1or2IEC,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_aero_const_iec import (
        WindAeroConstIEC,
    )


class WindGenTurbineType1aIEC(WindTurbineType1or2IEC):
    """Wind turbine IEC type 1A.

    Reference: IEC 61400-27-1:2015, 5.5.2.2."""

    __slots__ = ("_wind_aero_const_iec",)

    wind_aero_const_iec: One[WindAeroConstIEC] = One(
        EndMeta(
            name="wind_aero_const_iec",
            cim_role="WindAeroConstIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_aero_const_iec:WindAeroConstIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_gen_turbine_type1a_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindGenTurbineType1aIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{5FCBDDD3-F7A7-47e9-A373-FF6228EEE7B9}",
        ends=(wind_aero_const_iec.meta,),
    )

    def __init__(
        self,
        *,
        wind_aero_const_iec: WindAeroConstIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_aero_const_iec is not None:
            self.wind_aero_const_iec = wind_aero_const_iec

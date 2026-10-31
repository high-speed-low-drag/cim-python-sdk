"""CIM class WindTurbineType4IEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec import (
    WindTurbineType3or4IEC,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type3a_iec import (
        WindGenType3aIEC,
    )


class WindTurbineType4IEC(WindTurbineType3or4IEC):
    """Parent class supporting relationships to IEC wind turbines type 4 including their
    control models."""

    __slots__ = ("_wind_gen_type3a_iec",)

    wind_gen_type3a_iec: One[WindGenType3aIEC] = One(
        EndMeta(
            name="wind_gen_type3a_iec",
            cim_role="WindGenType3aIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type3a_iec:WindGenType3aIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_turbine_type4_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindTurbineType4IEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{B2FC2B31-9A83-4262-8192-EA91A2AD1F11}",
        ends=(wind_gen_type3a_iec.meta,),
    )

    def __init__(
        self,
        *,
        wind_gen_type3a_iec: WindGenType3aIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if wind_gen_type3a_iec is not None:
            self.wind_gen_type3a_iec = wind_gen_type3a_iec

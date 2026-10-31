"""CIM class WindAeroOneDimIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec import (
        WindTurbineType3IEC,
    )


class WindAeroOneDimIEC(IdentifiedObject):
    """One-dimensional aerodynamic model.

    Reference: IEC 61400-27-1:2015, 5.6.1.2."""

    __slots__ = ("_wind_turbine_type3_iec", "ka", "thetaomega")

    ka: float | None
    thetaomega: float | None  # AngleDegrees

    wind_turbine_type3_iec: One[WindTurbineType3IEC] = One(
        EndMeta(
            name="wind_turbine_type3_iec",
            cim_role="WindTurbineType3IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec:WindTurbineType3IEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_aero_one_dim_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindAeroOneDimIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{E1709164-3A33-4153-A521-C9D9096FE066}",
        attributes=(
            AttrMeta("ka", "ka", "float", 0, 1, "primitive"),
            AttrMeta("thetaomega", "thetaomega", "AngleDegrees", 0, 1, "cimdatatype"),
        ),
        ends=(wind_turbine_type3_iec.meta,),
    )

    def __init__(
        self,
        *,
        ka: float | None = None,
        thetaomega: float | None = None,
        wind_turbine_type3_iec: WindTurbineType3IEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ka = ka
        self.thetaomega = thetaomega
        if wind_turbine_type3_iec is not None:
            self.wind_turbine_type3_iec = wind_turbine_type3_iec

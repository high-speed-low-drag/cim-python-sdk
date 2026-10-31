"""CIM class WindGenType3aIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type3_iec import (
    WindGenType3IEC,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4_iec import (
        WindTurbineType4IEC,
    )


class WindGenType3aIEC(WindGenType3IEC):
    """IEC type 3A generator set model.

    Reference: IEC 61400-27-1:2015, 5.6.3.2."""

    __slots__ = ("_wind_turbine_type4_iec", "kpc", "tic")

    kpc: float | None
    tic: float | None  # Seconds

    wind_turbine_type4_iec: One[WindTurbineType4IEC] = One(
        EndMeta(
            name="wind_turbine_type4_iec",
            cim_role="WindTurbineType4IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4_iec:WindTurbineType4IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_gen_type3a_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindGenType3aIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{829F160E-1632-4e20-8131-B3A150D7CEDD}",
        attributes=(
            AttrMeta("kpc", "kpc", "float", 0, 1, "primitive"),
            AttrMeta("tic", "tic", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(wind_turbine_type4_iec.meta,),
    )

    def __init__(
        self,
        *,
        kpc: float | None = None,
        tic: float | None = None,
        wind_turbine_type4_iec: WindTurbineType4IEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kpc = kpc
        self.tic = tic
        if wind_turbine_type4_iec is not None:
            self.wind_turbine_type4_iec = wind_turbine_type4_iec

"""CIM class WindGenType3IEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec import (
        WindTurbineType3IEC,
    )


class WindGenType3IEC(IdentifiedObject):
    """Parent class supporting relationships to IEC wind turbines type 3 generator models of
    IEC type 3A and 3B."""

    __slots__ = ("_wind_turbine_type3_iec", "dipmax", "diqmax", "xs")

    dipmax: float | None  # PU
    diqmax: float | None  # PU
    xs: float | None  # PU

    wind_turbine_type3_iec: One[WindTurbineType3IEC] = One(
        EndMeta(
            name="wind_turbine_type3_iec",
            cim_role="WindTurbineType3IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec:WindTurbineType3IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_gen_type3_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindGenType3IEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{32C4D844-4EB5-4f33-87C4-F382CD72C6E5}",
        attributes=(
            AttrMeta("dipmax", "dipmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("diqmax", "diqmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xs", "xs", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(wind_turbine_type3_iec.meta,),
    )

    def __init__(
        self,
        *,
        dipmax: float | None = None,
        diqmax: float | None = None,
        xs: float | None = None,
        wind_turbine_type3_iec: WindTurbineType3IEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dipmax = dipmax
        self.diqmax = diqmax
        self.xs = xs
        if wind_turbine_type3_iec is not None:
            self.wind_turbine_type3_iec = wind_turbine_type3_iec

"""CIM class WindContQLimIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec import (
        WindTurbineType3or4IEC,
    )


class WindContQLimIEC(IdentifiedObject):
    """Constant Q limitation model.

    Reference: IEC 61400-27-1:2015, 5.6.5.9."""

    __slots__ = ("_wind_turbine_type3or4_iec", "qmax", "qmin")

    qmax: float | None  # PU
    qmin: float | None  # PU

    wind_turbine_type3or4_iec: One[WindTurbineType3or4IEC] = One(
        EndMeta(
            name="wind_turbine_type3or4_iec",
            cim_role="WindTurbineType3or4IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec:WindTurbineType3or4IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_cont_q_lim_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindContQLimIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{0467343B-F045-4055-BC86-B324E456F959}",
        attributes=(
            AttrMeta("qmax", "qmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("qmin", "qmin", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(wind_turbine_type3or4_iec.meta,),
    )

    def __init__(
        self,
        *,
        qmax: float | None = None,
        qmin: float | None = None,
        wind_turbine_type3or4_iec: WindTurbineType3or4IEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.qmax = qmax
        self.qmin = qmin
        if wind_turbine_type3or4_iec is not None:
            self.wind_turbine_type3or4_iec = wind_turbine_type3or4_iec

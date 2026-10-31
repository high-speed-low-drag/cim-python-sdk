"""CIM class WindRefFrameRotIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec import (
        WindTurbineType3or4IEC,
    )


class WindRefFrameRotIEC(IdentifiedObject):
    """Reference frame rotation model.

    Reference: IEC 61400-27-1:2015, 5.6.3.5."""

    __slots__ = ("_wind_turbine_type3or4_iec", "tpll", "upll1", "upll2")

    tpll: float | None  # Seconds
    upll1: float | None  # PU
    upll2: float | None  # PU

    wind_turbine_type3or4_iec: One[WindTurbineType3or4IEC] = One(
        EndMeta(
            name="wind_turbine_type3or4_iec",
            cim_role="WindTurbineType3or4IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec:WindTurbineType3or4IEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_ref_frame_rot_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindRefFrameRotIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{88FA754F-33E4-439c-A372-88659F26101D}",
        attributes=(
            AttrMeta("tpll", "tpll", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("upll1", "upll1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("upll2", "upll2", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(wind_turbine_type3or4_iec.meta,),
    )

    def __init__(
        self,
        *,
        tpll: float | None = None,
        upll1: float | None = None,
        upll2: float | None = None,
        wind_turbine_type3or4_iec: WindTurbineType3or4IEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tpll = tpll
        self.upll1 = upll1
        self.upll2 = upll2
        if wind_turbine_type3or4_iec is not None:
            self.wind_turbine_type3or4_iec = wind_turbine_type3or4_iec

"""CIM class WindContPType4bIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4b_iec import (
        WindTurbineType4bIEC,
    )


class WindContPType4bIEC(IdentifiedObject):
    """P control model type 4B.

    Reference: IEC 61400-27-1:2015, 5.6.5.6."""

    __slots__ = ("_wind_turbine_type4b_iec", "dpmaxp4b", "tpaero", "tpordp4b", "tufiltp4b")

    dpmaxp4b: float | None  # PU
    tpaero: float | None  # Seconds
    tpordp4b: float | None  # Seconds
    tufiltp4b: float | None  # Seconds

    wind_turbine_type4b_iec: One[WindTurbineType4bIEC] = One(
        EndMeta(
            name="wind_turbine_type4b_iec",
            cim_role="WindTurbineType4bIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4b_iec:WindTurbineType4bIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_cont_p_type4b_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindContPType4bIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{1735A7CB-F76E-413d-97E8-6425A1C86BE5}",
        attributes=(
            AttrMeta("dpmaxp4b", "dpmaxp4b", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tpaero", "tpaero", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tpordp4b", "tpordp4b", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tufiltp4b", "tufiltp4b", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(wind_turbine_type4b_iec.meta,),
    )

    def __init__(
        self,
        *,
        dpmaxp4b: float | None = None,
        tpaero: float | None = None,
        tpordp4b: float | None = None,
        tufiltp4b: float | None = None,
        wind_turbine_type4b_iec: WindTurbineType4bIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dpmaxp4b = dpmaxp4b
        self.tpaero = tpaero
        self.tpordp4b = tpordp4b
        self.tufiltp4b = tufiltp4b
        if wind_turbine_type4b_iec is not None:
            self.wind_turbine_type4b_iec = wind_turbine_type4b_iec

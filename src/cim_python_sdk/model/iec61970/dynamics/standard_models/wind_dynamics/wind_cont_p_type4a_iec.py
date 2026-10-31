"""CIM class WindContPType4aIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4a_iec import (
        WindTurbineType4aIEC,
    )


class WindContPType4aIEC(IdentifiedObject):
    """P control model type 4A.

    Reference: IEC 61400-27-1:2015, 5.6.5.5."""

    __slots__ = ("_wind_turbine_type4a_iec", "dpmaxp4a", "tpordp4a", "tufiltp4a")

    dpmaxp4a: float | None  # PU
    tpordp4a: float | None  # Seconds
    tufiltp4a: float | None  # Seconds

    wind_turbine_type4a_iec: One[WindTurbineType4aIEC] = One(
        EndMeta(
            name="wind_turbine_type4a_iec",
            cim_role="WindTurbineType4aIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4a_iec:WindTurbineType4aIEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_cont_p_type4a_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindContPType4aIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{517C136D-F29A-4078-A451-70A4EF1CA1B5}",
        attributes=(
            AttrMeta("dpmaxp4a", "dpmaxp4a", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tpordp4a", "tpordp4a", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tufiltp4a", "tufiltp4a", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(wind_turbine_type4a_iec.meta,),
    )

    def __init__(
        self,
        *,
        dpmaxp4a: float | None = None,
        tpordp4a: float | None = None,
        tufiltp4a: float | None = None,
        wind_turbine_type4a_iec: WindTurbineType4aIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dpmaxp4a = dpmaxp4a
        self.tpordp4a = tpordp4a
        self.tufiltp4a = tufiltp4a
        if wind_turbine_type4a_iec is not None:
            self.wind_turbine_type4a_iec = wind_turbine_type4a_iec

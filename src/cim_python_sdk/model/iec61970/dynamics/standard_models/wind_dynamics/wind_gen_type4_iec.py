"""CIM class WindGenType4IEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4a_iec import (
        WindTurbineType4aIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4b_iec import (
        WindTurbineType4bIEC,
    )


class WindGenType4IEC(IdentifiedObject):
    """IEC type 4 generator set model.

    Reference: IEC 61400-27-1:2015, 5.6.3.4."""

    __slots__ = (
        "_wind_turbine_type4a_iec",
        "_wind_turbine_type4b_iec",
        "dipmax",
        "diqmax",
        "diqmin",
        "tg",
    )

    dipmax: float | None  # PU
    diqmin: float | None  # PU
    diqmax: float | None  # PU
    tg: float | None  # Seconds

    wind_turbine_type4a_iec: One[WindTurbineType4aIEC] = One(
        EndMeta(
            name="wind_turbine_type4a_iec",
            cim_role="WindTurbineType4aIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4a_iec:WindTurbineType4aIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_gen_type4_iec",
            aggregation="none",
        )
    )
    wind_turbine_type4b_iec: One[WindTurbineType4bIEC] = One(
        EndMeta(
            name="wind_turbine_type4b_iec",
            cim_role="WindTurbineType4bIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type4b_iec:WindTurbineType4bIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_gen_type4_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindGenType4IEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{69688BAC-2396-4a92-B7A6-F6B224B9AD75}",
        attributes=(
            AttrMeta("dipmax", "dipmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("diqmin", "diqmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("diqmax", "diqmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tg", "tg", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(
            wind_turbine_type4a_iec.meta,
            wind_turbine_type4b_iec.meta,
        ),
    )

    def __init__(
        self,
        *,
        dipmax: float | None = None,
        diqmin: float | None = None,
        diqmax: float | None = None,
        tg: float | None = None,
        wind_turbine_type4a_iec: WindTurbineType4aIEC | None = None,
        wind_turbine_type4b_iec: WindTurbineType4bIEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dipmax = dipmax
        self.diqmin = diqmin
        self.diqmax = diqmax
        self.tg = tg
        if wind_turbine_type4a_iec is not None:
            self.wind_turbine_type4a_iec = wind_turbine_type4a_iec
        if wind_turbine_type4b_iec is not None:
            self.wind_turbine_type4b_iec = wind_turbine_type4b_iec

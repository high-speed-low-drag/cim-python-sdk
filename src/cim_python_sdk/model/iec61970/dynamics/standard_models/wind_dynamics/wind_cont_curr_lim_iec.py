"""CIM class WindContCurrLimIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_dynamics_lookup_table import (
        WindDynamicsLookupTable,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec import (
        WindTurbineType3or4IEC,
    )


class WindContCurrLimIEC(IdentifiedObject):
    """Current limitation model. The current limitation model combines the physical limits and
    the control limits.

    Reference: IEC 61400-27-1:2015, 5.6.5.8."""

    __slots__ = (
        "_wind_dynamics_lookup_table",
        "_wind_turbine_type3or4_iec",
        "imax",
        "imaxdip",
        "kpqu",
        "mdfslim",
        "mqpri",
        "tufiltcl",
        "upqumax",
    )

    imax: float | None  # PU
    imaxdip: float | None  # PU
    kpqu: float | None  # PU
    mdfslim: bool | None
    mqpri: bool | None
    tufiltcl: float | None  # Seconds
    upqumax: float | None  # PU

    wind_dynamics_lookup_table: Many[WindDynamicsLookupTable] = Many(
        EndMeta(
            name="wind_dynamics_lookup_table",
            cim_role="WindDynamicsLookupTable",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_dynamics_lookup_table:WindDynamicsLookupTable",
            many=True,
            lower=1,
            upper=None,
            inverse="wind_cont_curr_lim_iec",
            aggregation="none",
        )
    )
    wind_turbine_type3or4_iec: One[WindTurbineType3or4IEC] = One(
        EndMeta(
            name="wind_turbine_type3or4_iec",
            cim_role="WindTurbineType3or4IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec:WindTurbineType3or4IEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_cont_curr_lim_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindContCurrLimIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{F8C470F8-1D2E-480b-90C1-01A9084B5231}",
        attributes=(
            AttrMeta("imax", "imax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("imaxdip", "imaxdip", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpqu", "kpqu", "PU", 0, 1, "cimdatatype"),
            AttrMeta("mdfslim", "mdfslim", "bool", 0, 1, "primitive"),
            AttrMeta("mqpri", "mqpri", "bool", 0, 1, "primitive"),
            AttrMeta("tufiltcl", "tufiltcl", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("upqumax", "upqumax", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(
            wind_dynamics_lookup_table.meta,
            wind_turbine_type3or4_iec.meta,
        ),
    )

    def __init__(
        self,
        *,
        imax: float | None = None,
        imaxdip: float | None = None,
        kpqu: float | None = None,
        mdfslim: bool | None = None,
        mqpri: bool | None = None,
        tufiltcl: float | None = None,
        upqumax: float | None = None,
        wind_dynamics_lookup_table: Iterable[WindDynamicsLookupTable] | None = None,
        wind_turbine_type3or4_iec: WindTurbineType3or4IEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.imax = imax
        self.imaxdip = imaxdip
        self.kpqu = kpqu
        self.mdfslim = mdfslim
        self.mqpri = mqpri
        self.tufiltcl = tufiltcl
        self.upqumax = upqumax
        if wind_dynamics_lookup_table is not None:
            WindContCurrLimIEC.wind_dynamics_lookup_table.extend(self, wind_dynamics_lookup_table)
        if wind_turbine_type3or4_iec is not None:
            self.wind_turbine_type3or4_iec = wind_turbine_type3or4_iec

    def add_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindContCurrLimIEC.wind_dynamics_lookup_table.add(self, wind_dynamics_lookup_table)

    def remove_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindContCurrLimIEC.wind_dynamics_lookup_table.remove(
            self, wind_dynamics_lookup_table
        )

    def clear_wind_dynamics_lookup_table(self) -> Self:
        return WindContCurrLimIEC.wind_dynamics_lookup_table.clear(self)

    def num_wind_dynamics_lookup_table(self) -> int:
        return WindContCurrLimIEC.wind_dynamics_lookup_table.count(self)

    def get_wind_dynamics_lookup_table_by_mrid(self, mrid: str) -> WindDynamicsLookupTable | None:
        return WindContCurrLimIEC.wind_dynamics_lookup_table.get_by_mrid(self, mrid)

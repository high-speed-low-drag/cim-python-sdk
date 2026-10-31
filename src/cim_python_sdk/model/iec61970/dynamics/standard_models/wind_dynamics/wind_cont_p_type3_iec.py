"""CIM class WindContPType3IEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec import (
        WindTurbineType3IEC,
    )


class WindContPType3IEC(IdentifiedObject):
    """P control model type 3.

    Reference: IEC 61400-27-1:2015, 5.6.5.4."""

    __slots__ = (
        "_wind_dynamics_lookup_table",
        "_wind_turbine_type3_iec",
        "dpmax",
        "dprefmax",
        "dprefmin",
        "dthetamax",
        "dthetamaxuvrt",
        "kdtd",
        "kip",
        "kpp",
        "mpuvrt",
        "omegadtd",
        "omegaoffset",
        "pdtdmax",
        "tdvs",
        "thetaemin",
        "thetauscale",
        "tomegafiltp3",
        "tomegaref",
        "tpfiltp3",
        "tpord",
        "tufiltp3",
        "udvs",
        "updip",
        "zeta",
    )

    dpmax: float | None  # PU
    dprefmax: float | None  # PU
    dprefmin: float | None  # PU
    dthetamax: float | None  # PU
    dthetamaxuvrt: float | None  # PU
    kdtd: float | None  # PU
    kip: float | None  # PU
    kpp: float | None  # PU
    mpuvrt: bool | None
    omegaoffset: float | None  # PU
    pdtdmax: float | None  # PU
    tdvs: float | None  # Seconds
    thetaemin: float | None  # PU
    thetauscale: float | None  # PU
    tomegafiltp3: float | None  # Seconds
    tpfiltp3: float | None  # Seconds
    tpord: float | None  # PU
    tufiltp3: float | None  # Seconds
    tomegaref: float | None  # Seconds
    udvs: float | None  # PU
    updip: float | None  # PU
    omegadtd: float | None  # PU
    zeta: float | None

    wind_turbine_type3_iec: One[WindTurbineType3IEC] = One(
        EndMeta(
            name="wind_turbine_type3_iec",
            cim_role="WindTurbineType3IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3_iec:WindTurbineType3IEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_cont_p_type3_iec",
            aggregation="none",
        )
    )
    wind_dynamics_lookup_table: Many[WindDynamicsLookupTable] = Many(
        EndMeta(
            name="wind_dynamics_lookup_table",
            cim_role="WindDynamicsLookupTable",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_dynamics_lookup_table:WindDynamicsLookupTable",
            many=True,
            lower=1,
            upper=None,
            inverse="wind_cont_p_type3_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindContPType3IEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{8C54657E-6009-43ee-9D5B-27347C81C160}",
        attributes=(
            AttrMeta("dpmax", "dpmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dprefmax", "dprefmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dprefmin", "dprefmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dthetamax", "dthetamax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dthetamaxuvrt", "dthetamaxuvrt", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kdtd", "kdtd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kip", "kip", "PU", 0, 1, "cimdatatype"),
            AttrMeta("kpp", "kpp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("mpuvrt", "mpuvrt", "bool", 0, 1, "primitive"),
            AttrMeta("omegaoffset", "omegaoffset", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pdtdmax", "pdtdmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tdvs", "tdvs", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("thetaemin", "thetaemin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("thetauscale", "thetauscale", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tomegafiltp3", "tomegafiltp3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tpfiltp3", "tpfiltp3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tpord", "tpord", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tufiltp3", "tufiltp3", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tomegaref", "tomegaref", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("udvs", "udvs", "PU", 0, 1, "cimdatatype"),
            AttrMeta("updip", "updip", "PU", 0, 1, "cimdatatype"),
            AttrMeta("omegadtd", "omegadtd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("zeta", "zeta", "float", 0, 1, "primitive"),
        ),
        ends=(
            wind_turbine_type3_iec.meta,
            wind_dynamics_lookup_table.meta,
        ),
    )

    def __init__(
        self,
        *,
        dpmax: float | None = None,
        dprefmax: float | None = None,
        dprefmin: float | None = None,
        dthetamax: float | None = None,
        dthetamaxuvrt: float | None = None,
        kdtd: float | None = None,
        kip: float | None = None,
        kpp: float | None = None,
        mpuvrt: bool | None = None,
        omegaoffset: float | None = None,
        pdtdmax: float | None = None,
        tdvs: float | None = None,
        thetaemin: float | None = None,
        thetauscale: float | None = None,
        tomegafiltp3: float | None = None,
        tpfiltp3: float | None = None,
        tpord: float | None = None,
        tufiltp3: float | None = None,
        tomegaref: float | None = None,
        udvs: float | None = None,
        updip: float | None = None,
        omegadtd: float | None = None,
        zeta: float | None = None,
        wind_turbine_type3_iec: WindTurbineType3IEC | None = None,
        wind_dynamics_lookup_table: Iterable[WindDynamicsLookupTable] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dpmax = dpmax
        self.dprefmax = dprefmax
        self.dprefmin = dprefmin
        self.dthetamax = dthetamax
        self.dthetamaxuvrt = dthetamaxuvrt
        self.kdtd = kdtd
        self.kip = kip
        self.kpp = kpp
        self.mpuvrt = mpuvrt
        self.omegaoffset = omegaoffset
        self.pdtdmax = pdtdmax
        self.tdvs = tdvs
        self.thetaemin = thetaemin
        self.thetauscale = thetauscale
        self.tomegafiltp3 = tomegafiltp3
        self.tpfiltp3 = tpfiltp3
        self.tpord = tpord
        self.tufiltp3 = tufiltp3
        self.tomegaref = tomegaref
        self.udvs = udvs
        self.updip = updip
        self.omegadtd = omegadtd
        self.zeta = zeta
        if wind_turbine_type3_iec is not None:
            self.wind_turbine_type3_iec = wind_turbine_type3_iec
        if wind_dynamics_lookup_table is not None:
            WindContPType3IEC.wind_dynamics_lookup_table.extend(self, wind_dynamics_lookup_table)

    def add_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindContPType3IEC.wind_dynamics_lookup_table.add(self, wind_dynamics_lookup_table)

    def remove_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindContPType3IEC.wind_dynamics_lookup_table.remove(self, wind_dynamics_lookup_table)

    def clear_wind_dynamics_lookup_table(self) -> Self:
        return WindContPType3IEC.wind_dynamics_lookup_table.clear(self)

    def num_wind_dynamics_lookup_table(self) -> int:
        return WindContPType3IEC.wind_dynamics_lookup_table.count(self)

    def get_wind_dynamics_lookup_table_by_mrid(self, mrid: str) -> WindDynamicsLookupTable | None:
        return WindContPType3IEC.wind_dynamics_lookup_table.get_by_mrid(self, mrid)

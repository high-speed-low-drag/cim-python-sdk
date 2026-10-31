"""CIM class WindPitchContPowerIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_turbine_type1b_iec import (
        WindGenTurbineType1bIEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_turbine_type2_iec import (
        WindGenTurbineType2IEC,
    )


class WindPitchContPowerIEC(IdentifiedObject):
    """Pitch control power model.

    Reference: IEC 61400-27-1:2015, 5.6.5.1."""

    __slots__ = (
        "_wind_dynamics_lookup_table",
        "_wind_gen_turbine_type1b_iec",
        "_wind_gen_turbine_type2_iec",
        "dpmax",
        "dpmin",
        "pmin",
        "pset",
        "t1",
        "tr",
        "uuvrt",
    )

    dpmax: float | None  # PU
    dpmin: float | None  # PU
    pmin: float | None  # PU
    pset: float | None  # PU
    t1: float | None  # Seconds
    tr: float | None  # Seconds
    uuvrt: float | None  # PU

    wind_gen_turbine_type1b_iec: One[WindGenTurbineType1bIEC] = One(
        EndMeta(
            name="wind_gen_turbine_type1b_iec",
            cim_role="WindGenTurbineType1bIEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_turbine_type1b_iec:WindGenTurbineType1bIEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_pitch_cont_power_iec",
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
            inverse="wind_pitch_cont_power_iec",
            aggregation="none",
        )
    )
    wind_gen_turbine_type2_iec: One[WindGenTurbineType2IEC] = One(
        EndMeta(
            name="wind_gen_turbine_type2_iec",
            cim_role="WindGenTurbineType2IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_turbine_type2_iec:WindGenTurbineType2IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_pitch_cont_power_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindPitchContPowerIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{03564493-C833-430f-8DDE-1BC031C171D9}",
        attributes=(
            AttrMeta("dpmax", "dpmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("dpmin", "dpmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pmin", "pmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pset", "pset", "PU", 0, 1, "cimdatatype"),
            AttrMeta("t1", "t1", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tr", "tr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("uuvrt", "uuvrt", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(
            wind_gen_turbine_type1b_iec.meta,
            wind_dynamics_lookup_table.meta,
            wind_gen_turbine_type2_iec.meta,
        ),
    )

    def __init__(
        self,
        *,
        dpmax: float | None = None,
        dpmin: float | None = None,
        pmin: float | None = None,
        pset: float | None = None,
        t1: float | None = None,
        tr: float | None = None,
        uuvrt: float | None = None,
        wind_gen_turbine_type1b_iec: WindGenTurbineType1bIEC | None = None,
        wind_dynamics_lookup_table: Iterable[WindDynamicsLookupTable] | None = None,
        wind_gen_turbine_type2_iec: WindGenTurbineType2IEC | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dpmax = dpmax
        self.dpmin = dpmin
        self.pmin = pmin
        self.pset = pset
        self.t1 = t1
        self.tr = tr
        self.uuvrt = uuvrt
        if wind_gen_turbine_type1b_iec is not None:
            self.wind_gen_turbine_type1b_iec = wind_gen_turbine_type1b_iec
        if wind_dynamics_lookup_table is not None:
            WindPitchContPowerIEC.wind_dynamics_lookup_table.extend(
                self, wind_dynamics_lookup_table
            )
        if wind_gen_turbine_type2_iec is not None:
            self.wind_gen_turbine_type2_iec = wind_gen_turbine_type2_iec

    def add_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindPitchContPowerIEC.wind_dynamics_lookup_table.add(
            self, wind_dynamics_lookup_table
        )

    def remove_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindPitchContPowerIEC.wind_dynamics_lookup_table.remove(
            self, wind_dynamics_lookup_table
        )

    def clear_wind_dynamics_lookup_table(self) -> Self:
        return WindPitchContPowerIEC.wind_dynamics_lookup_table.clear(self)

    def num_wind_dynamics_lookup_table(self) -> int:
        return WindPitchContPowerIEC.wind_dynamics_lookup_table.count(self)

    def get_wind_dynamics_lookup_table_by_mrid(self, mrid: str) -> WindDynamicsLookupTable | None:
        return WindPitchContPowerIEC.wind_dynamics_lookup_table.get_by_mrid(self, mrid)

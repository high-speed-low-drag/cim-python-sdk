"""CIM class WindContRotorRIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_turbine_type2_iec import (
        WindGenTurbineType2IEC,
    )


class WindContRotorRIEC(IdentifiedObject):
    """Rotor resistance control model.

    Reference: IEC 61400-27-1:2015, 5.6.5.3."""

    __slots__ = (
        "_wind_dynamics_lookup_table",
        "_wind_gen_turbine_type2_iec",
        "kirr",
        "komegafilt",
        "kpfilt",
        "kprr",
        "rmax",
        "rmin",
        "tomegafiltrr",
        "tpfiltrr",
    )

    kirr: float | None  # PU
    komegafilt: float | None
    kpfilt: float | None
    kprr: float | None  # PU
    rmax: float | None  # PU
    rmin: float | None  # PU
    tomegafiltrr: float | None  # Seconds
    tpfiltrr: float | None  # Seconds

    wind_gen_turbine_type2_iec: One[WindGenTurbineType2IEC] = One(
        EndMeta(
            name="wind_gen_turbine_type2_iec",
            cim_role="WindGenTurbineType2IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_turbine_type2_iec:WindGenTurbineType2IEC",
            many=False,
            lower=1,
            upper=1,
            inverse="wind_cont_rotor_riec",
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
            inverse="wind_cont_rotor_riec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindContRotorRIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{F502B382-DD6B-4ea9-B945-E4DDB050126C}",
        attributes=(
            AttrMeta("kirr", "kirr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("komegafilt", "komegafilt", "float", 0, 1, "primitive"),
            AttrMeta("kpfilt", "kpfilt", "float", 0, 1, "primitive"),
            AttrMeta("kprr", "kprr", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rmax", "rmax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rmin", "rmin", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tomegafiltrr", "tomegafiltrr", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tpfiltrr", "tpfiltrr", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(
            wind_gen_turbine_type2_iec.meta,
            wind_dynamics_lookup_table.meta,
        ),
    )

    def __init__(
        self,
        *,
        kirr: float | None = None,
        komegafilt: float | None = None,
        kpfilt: float | None = None,
        kprr: float | None = None,
        rmax: float | None = None,
        rmin: float | None = None,
        tomegafiltrr: float | None = None,
        tpfiltrr: float | None = None,
        wind_gen_turbine_type2_iec: WindGenTurbineType2IEC | None = None,
        wind_dynamics_lookup_table: Iterable[WindDynamicsLookupTable] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kirr = kirr
        self.komegafilt = komegafilt
        self.kpfilt = kpfilt
        self.kprr = kprr
        self.rmax = rmax
        self.rmin = rmin
        self.tomegafiltrr = tomegafiltrr
        self.tpfiltrr = tpfiltrr
        if wind_gen_turbine_type2_iec is not None:
            self.wind_gen_turbine_type2_iec = wind_gen_turbine_type2_iec
        if wind_dynamics_lookup_table is not None:
            WindContRotorRIEC.wind_dynamics_lookup_table.extend(self, wind_dynamics_lookup_table)

    def add_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindContRotorRIEC.wind_dynamics_lookup_table.add(self, wind_dynamics_lookup_table)

    def remove_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindContRotorRIEC.wind_dynamics_lookup_table.remove(self, wind_dynamics_lookup_table)

    def clear_wind_dynamics_lookup_table(self) -> Self:
        return WindContRotorRIEC.wind_dynamics_lookup_table.clear(self)

    def num_wind_dynamics_lookup_table(self) -> int:
        return WindContRotorRIEC.wind_dynamics_lookup_table.count(self)

    def get_wind_dynamics_lookup_table_by_mrid(self, mrid: str) -> WindDynamicsLookupTable | None:
        return WindContRotorRIEC.wind_dynamics_lookup_table.get_by_mrid(self, mrid)

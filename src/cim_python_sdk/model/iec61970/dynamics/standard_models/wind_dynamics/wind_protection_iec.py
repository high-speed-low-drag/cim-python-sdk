"""CIM class WindProtectionIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

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
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_iec import (
        WindTurbineType1or2IEC,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec import (
        WindTurbineType3or4IEC,
    )


class WindProtectionIEC(IdentifiedObject):
    """The grid protection model includes protection against over- and under-voltage, and
    against over- and under-frequency.

    Reference: IEC 61400-27-1:2015, 5.6.6."""

    __slots__ = (
        "_wind_dynamics_lookup_table",
        "_wind_turbine_type1or2_iec",
        "_wind_turbine_type3or4_iec",
        "dfimax",
        "fover",
        "funder",
        "mzc",
        "tfma",
        "uover",
        "uunder",
    )

    dfimax: float | None  # PU
    fover: float | None  # PU
    funder: float | None  # PU
    mzc: bool | None
    tfma: float | None  # Seconds
    uover: float | None  # PU
    uunder: float | None  # PU

    wind_turbine_type1or2_iec: One[WindTurbineType1or2IEC] = One(
        EndMeta(
            name="wind_turbine_type1or2_iec",
            cim_role="WindTurbineType1or2IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type1or2_iec:WindTurbineType1or2IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_protection_iec",
            aggregation="none",
        )
    )
    wind_turbine_type3or4_iec: One[WindTurbineType3or4IEC] = One(
        EndMeta(
            name="wind_turbine_type3or4_iec",
            cim_role="WindTurbineType3or4IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec:WindTurbineType3or4IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_protection_iec",
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
            inverse="wind_protection_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindProtectionIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{C2A06D61-8879-4b9b-A32E-68822308A460}",
        attributes=(
            AttrMeta("dfimax", "dfimax", "PU", 0, 1, "cimdatatype"),
            AttrMeta("fover", "fover", "PU", 0, 1, "cimdatatype"),
            AttrMeta("funder", "funder", "PU", 0, 1, "cimdatatype"),
            AttrMeta("mzc", "mzc", "bool", 0, 1, "primitive"),
            AttrMeta("tfma", "tfma", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("uover", "uover", "PU", 0, 1, "cimdatatype"),
            AttrMeta("uunder", "uunder", "PU", 0, 1, "cimdatatype"),
        ),
        ends=(
            wind_turbine_type1or2_iec.meta,
            wind_turbine_type3or4_iec.meta,
            wind_dynamics_lookup_table.meta,
        ),
    )

    def __init__(
        self,
        *,
        dfimax: float | None = None,
        fover: float | None = None,
        funder: float | None = None,
        mzc: bool | None = None,
        tfma: float | None = None,
        uover: float | None = None,
        uunder: float | None = None,
        wind_turbine_type1or2_iec: WindTurbineType1or2IEC | None = None,
        wind_turbine_type3or4_iec: WindTurbineType3or4IEC | None = None,
        wind_dynamics_lookup_table: Iterable[WindDynamicsLookupTable] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dfimax = dfimax
        self.fover = fover
        self.funder = funder
        self.mzc = mzc
        self.tfma = tfma
        self.uover = uover
        self.uunder = uunder
        if wind_turbine_type1or2_iec is not None:
            self.wind_turbine_type1or2_iec = wind_turbine_type1or2_iec
        if wind_turbine_type3or4_iec is not None:
            self.wind_turbine_type3or4_iec = wind_turbine_type3or4_iec
        if wind_dynamics_lookup_table is not None:
            WindProtectionIEC.wind_dynamics_lookup_table.extend(self, wind_dynamics_lookup_table)

    def add_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindProtectionIEC.wind_dynamics_lookup_table.add(self, wind_dynamics_lookup_table)

    def remove_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindProtectionIEC.wind_dynamics_lookup_table.remove(self, wind_dynamics_lookup_table)

    def clear_wind_dynamics_lookup_table(self) -> Self:
        return WindProtectionIEC.wind_dynamics_lookup_table.clear(self)

    def num_wind_dynamics_lookup_table(self) -> int:
        return WindProtectionIEC.wind_dynamics_lookup_table.count(self)

    def get_wind_dynamics_lookup_table_by_mrid(self, mrid: str) -> WindDynamicsLookupTable | None:
        return WindProtectionIEC.wind_dynamics_lookup_table.get_by_mrid(self, mrid)

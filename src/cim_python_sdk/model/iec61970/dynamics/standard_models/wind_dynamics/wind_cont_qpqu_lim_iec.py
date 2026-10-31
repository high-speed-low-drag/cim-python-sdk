"""CIM class WindContQPQULimIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

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


class WindContQPQULimIEC(IdentifiedObject):
    """QP and QU limitation model.

    Reference: IEC 61400-27-1:2015, 5.6.5.10."""

    __slots__ = (
        "_wind_dynamics_lookup_table",
        "_wind_turbine_type3or4_iec",
        "tpfiltql",
        "tufiltql",
    )

    tpfiltql: float | None  # Seconds
    tufiltql: float | None  # Seconds

    wind_turbine_type3or4_iec: One[WindTurbineType3or4IEC] = One(
        EndMeta(
            name="wind_turbine_type3or4_iec",
            cim_role="WindTurbineType3or4IEC",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_turbine_type3or4_iec:WindTurbineType3or4IEC",
            many=False,
            lower=0,
            upper=1,
            inverse="wind_cont_qpqu_lim_iec",
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
            inverse="wind_cont_qpqu_lim_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindContQPQULimIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{81CC172F-97DA-47a7-9FD3-05DB211DA99D}",
        attributes=(
            AttrMeta("tpfiltql", "tpfiltql", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tufiltql", "tufiltql", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(
            wind_turbine_type3or4_iec.meta,
            wind_dynamics_lookup_table.meta,
        ),
    )

    def __init__(
        self,
        *,
        tpfiltql: float | None = None,
        tufiltql: float | None = None,
        wind_turbine_type3or4_iec: WindTurbineType3or4IEC | None = None,
        wind_dynamics_lookup_table: Iterable[WindDynamicsLookupTable] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.tpfiltql = tpfiltql
        self.tufiltql = tufiltql
        if wind_turbine_type3or4_iec is not None:
            self.wind_turbine_type3or4_iec = wind_turbine_type3or4_iec
        if wind_dynamics_lookup_table is not None:
            WindContQPQULimIEC.wind_dynamics_lookup_table.extend(self, wind_dynamics_lookup_table)

    def add_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindContQPQULimIEC.wind_dynamics_lookup_table.add(self, wind_dynamics_lookup_table)

    def remove_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindContQPQULimIEC.wind_dynamics_lookup_table.remove(
            self, wind_dynamics_lookup_table
        )

    def clear_wind_dynamics_lookup_table(self) -> Self:
        return WindContQPQULimIEC.wind_dynamics_lookup_table.clear(self)

    def num_wind_dynamics_lookup_table(self) -> int:
        return WindContQPQULimIEC.wind_dynamics_lookup_table.count(self)

    def get_wind_dynamics_lookup_table_by_mrid(self, mrid: str) -> WindDynamicsLookupTable | None:
        return WindContQPQULimIEC.wind_dynamics_lookup_table.get_by_mrid(self, mrid)

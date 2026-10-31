"""CIM class WindGenType3bIEC (TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_gen_type3_iec import (
    WindGenType3IEC,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_dynamics_lookup_table import (
        WindDynamicsLookupTable,
    )


class WindGenType3bIEC(WindGenType3IEC):
    """IEC type 3B generator set model.

    Reference: IEC 61400-27-1:2015, 5.6.3.3."""

    __slots__ = ("_wind_dynamics_lookup_table", "mwtcwp", "tg", "two")

    mwtcwp: bool | None
    tg: float | None  # Seconds
    two: float | None  # Seconds

    wind_dynamics_lookup_table: Many[WindDynamicsLookupTable] = Many(
        EndMeta(
            name="wind_dynamics_lookup_table",
            cim_role="WindDynamicsLookupTable",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.wind_dynamics.wind_dynamics_lookup_table:WindDynamicsLookupTable",
            many=True,
            lower=1,
            upper=None,
            inverse="wind_gen_type3b_iec",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindGenType3bIEC",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/WindDynamics",
        guid="{CF018773-CA7C-42eb-9ABB-25B08171749C}",
        attributes=(
            AttrMeta("mwtcwp", "mwtcwp", "bool", 0, 1, "primitive"),
            AttrMeta("tg", "tg", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("two", "two", "Seconds", 0, 1, "cimdatatype"),
        ),
        ends=(wind_dynamics_lookup_table.meta,),
    )

    def __init__(
        self,
        *,
        mwtcwp: bool | None = None,
        tg: float | None = None,
        two: float | None = None,
        wind_dynamics_lookup_table: Iterable[WindDynamicsLookupTable] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.mwtcwp = mwtcwp
        self.tg = tg
        self.two = two
        if wind_dynamics_lookup_table is not None:
            WindGenType3bIEC.wind_dynamics_lookup_table.extend(self, wind_dynamics_lookup_table)

    def add_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindGenType3bIEC.wind_dynamics_lookup_table.add(self, wind_dynamics_lookup_table)

    def remove_wind_dynamics_lookup_table(
        self, wind_dynamics_lookup_table: WindDynamicsLookupTable
    ) -> Self:
        return WindGenType3bIEC.wind_dynamics_lookup_table.remove(self, wind_dynamics_lookup_table)

    def clear_wind_dynamics_lookup_table(self) -> Self:
        return WindGenType3bIEC.wind_dynamics_lookup_table.clear(self)

    def num_wind_dynamics_lookup_table(self) -> int:
        return WindGenType3bIEC.wind_dynamics_lookup_table.count(self)

    def get_wind_dynamics_lookup_table_by_mrid(self, mrid: str) -> WindDynamicsLookupTable | None:
        return WindGenType3bIEC.wind_dynamics_lookup_table.get_by_mrid(self, mrid)

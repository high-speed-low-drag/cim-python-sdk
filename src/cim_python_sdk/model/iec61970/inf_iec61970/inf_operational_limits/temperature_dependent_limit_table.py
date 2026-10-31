"""CIM class TemperatureDependentLimitTable (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.environmental_dependent_limit import (
    EnvironmentalDependentLimit,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.temperature_dependent_limit_point import (
        TemperatureDependentLimitPoint,
    )


class TemperatureDependentLimitTable(EnvironmentalDependentLimit):
    """This is a table lookup that provides limit values corresponding to a temperature input."""

    __slots__ = ("_temperature_limit_table_point",)

    temperature_limit_table_point: Many[TemperatureDependentLimitPoint] = Many(
        EndMeta(
            name="temperature_limit_table_point",
            cim_role="TemperatureLimitTablePoint",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.temperature_dependent_limit_point:TemperatureDependentLimitPoint",
            many=True,
            lower=0,
            upper=None,
            inverse="temperature_dependent_limit_table",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TemperatureDependentLimitTable",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{E27624EE-9CAF-45bb-8E53-5FF5083B6595}",
        ends=(temperature_limit_table_point.meta,),
    )

    def __init__(
        self,
        *,
        temperature_limit_table_point: Iterable[TemperatureDependentLimitPoint] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if temperature_limit_table_point is not None:
            TemperatureDependentLimitTable.temperature_limit_table_point.extend(
                self, temperature_limit_table_point
            )

    def add_temperature_limit_table_point(
        self, temperature_limit_table_point: TemperatureDependentLimitPoint
    ) -> Self:
        return TemperatureDependentLimitTable.temperature_limit_table_point.add(
            self, temperature_limit_table_point
        )

    def remove_temperature_limit_table_point(
        self, temperature_limit_table_point: TemperatureDependentLimitPoint
    ) -> Self:
        return TemperatureDependentLimitTable.temperature_limit_table_point.remove(
            self, temperature_limit_table_point
        )

    def clear_temperature_limit_table_point(self) -> Self:
        return TemperatureDependentLimitTable.temperature_limit_table_point.clear(self)

    def num_temperature_limit_table_point(self) -> int:
        return TemperatureDependentLimitTable.temperature_limit_table_point.count(self)

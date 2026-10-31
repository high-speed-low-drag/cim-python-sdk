"""CIM class TemperatureDependentLimitPoint (TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.temperature_dependent_limit_table import (
        TemperatureDependentLimitTable,
    )


class TemperatureDependentLimitPoint(CimObject):
    """A point on a table of limit verses temperature."""

    __slots__ = ("_temperature_dependent_limit_table", "limit_percent", "temperature")

    limit_percent: float | None  # PerCent
    temperature: float | None  # Temperature

    temperature_dependent_limit_table: One[TemperatureDependentLimitTable] = One(
        EndMeta(
            name="temperature_dependent_limit_table",
            cim_role="TemperatureDependentLimitTable",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_operational_limits.temperature_dependent_limit_table:TemperatureDependentLimitTable",
            many=False,
            lower=1,
            upper=1,
            inverse="temperature_limit_table_point",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TemperatureDependentLimitPoint",
        package="TC57CIM/IEC61970/InfIEC61970/InfOperationalLimits",
        guid="{D7663B24-BFFA-4226-82F3-FB51D0C254E1}",
        attributes=(
            AttrMeta("limit_percent", "limitPercent", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("temperature", "temperature", "Temperature", 0, 1, "cimdatatype"),
        ),
        ends=(temperature_dependent_limit_table.meta,),
    )

    def __init__(
        self,
        *,
        limit_percent: float | None = None,
        temperature: float | None = None,
        temperature_dependent_limit_table: TemperatureDependentLimitTable | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.limit_percent = limit_percent
        self.temperature = temperature
        if temperature_dependent_limit_table is not None:
            self.temperature_dependent_limit_table = temperature_dependent_limit_table

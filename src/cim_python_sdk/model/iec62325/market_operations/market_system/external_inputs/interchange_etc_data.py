"""CIM class InterchangeETCData (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.interchange_schedule import (
        InterchangeSchedule,
    )


class InterchangeETCData(CimObject):
    """Existing Transmission Contract data for an interchange schedule."""

    __slots__ = ("_interchange_schedule", "contract_number", "usage_mw")

    contract_number: str | None
    usage_mw: float | None

    interchange_schedule: One[InterchangeSchedule] = One(
        EndMeta(
            name="interchange_schedule",
            cim_role="InterchangeSchedule",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.interchange_schedule:InterchangeSchedule",
            many=False,
            lower=0,
            upper=1,
            inverse="interchange_etc_data",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InterchangeETCData",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{AA37D26B-B897-43ce-B8F6-FC8C02AB6BA7}",
        attributes=(
            AttrMeta("contract_number", "contractNumber", "str", 0, 1, "primitive"),
            AttrMeta("usage_mw", "usageMW", "float", 0, 1, "primitive"),
        ),
        ends=(interchange_schedule.meta,),
    )

    def __init__(
        self,
        *,
        contract_number: str | None = None,
        usage_mw: float | None = None,
        interchange_schedule: InterchangeSchedule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.contract_number = contract_number
        self.usage_mw = usage_mw
        if interchange_schedule is not None:
            self.interchange_schedule = interchange_schedule

"""CIM class SwitchStatus (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_switch import (
        MktSwitch,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.switch_status_type import (
        SwitchStatusType,
    )


class SwitchStatus(CimObject):
    """Optimal Power Flow or State Estimator Circuit Breaker Status."""

    __slots__ = ("_mkt_switch", "switch_status")

    switch_status: SwitchStatusType | None

    mkt_switch: One[MktSwitch] = One(
        EndMeta(
            name="mkt_switch",
            cim_role="MktSwitch",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_switch:MktSwitch",
            many=False,
            lower=1,
            upper=1,
            inverse="switch_status",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SwitchStatus",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{9694A566-8C17-475e-9EB1-0F10E084A6A6}",
        attributes=(
            AttrMeta("switch_status", "switchStatus", "SwitchStatusType", 0, 1, "enumeration"),
        ),
        ends=(mkt_switch.meta,),
    )

    def __init__(
        self,
        *,
        switch_status: SwitchStatusType | None = None,
        mkt_switch: MktSwitch | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.switch_status = switch_status
        if mkt_switch is not None:
            self.mkt_switch = mkt_switch

"""CIM class MktSwitch (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.switch import Switch

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.switch_status import (
        SwitchStatus,
    )


class MktSwitch(Switch):
    """Subclass of IEC 61970:Wires:Switch."""

    __slots__ = ("_switch_status",)

    switch_status: Many[SwitchStatus] = Many(
        EndMeta(
            name="switch_status",
            cim_role="SwitchStatus",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.switch_status:SwitchStatus",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_switch",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktSwitch",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{34A1D3B5-55F1-44f8-906D-73EB04C34B87}",
        ends=(switch_status.meta,),
    )

    def __init__(
        self,
        *,
        switch_status: Iterable[SwitchStatus] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if switch_status is not None:
            MktSwitch.switch_status.extend(self, switch_status)

    def add_switch_status(self, switch_status: SwitchStatus) -> Self:
        return MktSwitch.switch_status.add(self, switch_status)

    def remove_switch_status(self, switch_status: SwitchStatus) -> Self:
        return MktSwitch.switch_status.remove(self, switch_status)

    def clear_switch_status(self) -> Self:
        return MktSwitch.switch_status.clear(self)

    def num_switch_status(self) -> int:
        return MktSwitch.switch_status.count(self)

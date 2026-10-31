"""CIM class MktTapChanger (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.wires.tap_changer import TapChanger

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.tap_changer_dynamic_data import (
        TapChangerDynamicData,
    )


class MktTapChanger(TapChanger):
    """Subclass of IEC 61970:Wires:TapChanger."""

    __slots__ = ("_tap_changer_dynamic_data",)

    tap_changer_dynamic_data: Many[TapChangerDynamicData] = Many(
        EndMeta(
            name="tap_changer_dynamic_data",
            cim_role="TapChangerDynamicData",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.tap_changer_dynamic_data:TapChangerDynamicData",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_tap_changer",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktTapChanger",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{BCEAC343-15E5-4871-B74F-1FE4593A6128}",
        ends=(tap_changer_dynamic_data.meta,),
    )

    def __init__(
        self,
        *,
        tap_changer_dynamic_data: Iterable[TapChangerDynamicData] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if tap_changer_dynamic_data is not None:
            MktTapChanger.tap_changer_dynamic_data.extend(self, tap_changer_dynamic_data)

    def add_tap_changer_dynamic_data(self, tap_changer_dynamic_data: TapChangerDynamicData) -> Self:
        return MktTapChanger.tap_changer_dynamic_data.add(self, tap_changer_dynamic_data)

    def remove_tap_changer_dynamic_data(
        self, tap_changer_dynamic_data: TapChangerDynamicData
    ) -> Self:
        return MktTapChanger.tap_changer_dynamic_data.remove(self, tap_changer_dynamic_data)

    def clear_tap_changer_dynamic_data(self) -> Self:
        return MktTapChanger.tap_changer_dynamic_data.clear(self)

    def num_tap_changer_dynamic_data(self) -> int:
        return MktTapChanger.tap_changer_dynamic_data.count(self)

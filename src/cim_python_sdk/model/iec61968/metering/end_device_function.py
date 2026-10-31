"""CIM class EndDeviceFunction (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.assets.asset_function import AssetFunction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.end_device import EndDevice
    from cim_python_sdk.model.iec61968.metering.register import Register


class EndDeviceFunction(AssetFunction):
    """Function performed by an end device such as a meter, communication equipment,
    controllers, etc."""

    __slots__ = ("_end_device", "_registers", "enabled")

    enabled: bool | None

    end_device: One[EndDevice] = One(
        EndMeta(
            name="end_device",
            cim_role="EndDevice",
            target="cim_python_sdk.model.iec61968.metering.end_device:EndDevice",
            many=False,
            lower=0,
            upper=1,
            inverse="end_device_functions",
            aggregation="none",
        )
    )
    registers: Many[Register] = Many(
        EndMeta(
            name="registers",
            cim_role="Registers",
            target="cim_python_sdk.model.iec61968.metering.register:Register",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_function",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EndDeviceFunction",
        package="TC57CIM/IEC61968/Metering",
        guid="{2D3B1D7A-126C-4978-AD23-878983457DA8}",
        attributes=(AttrMeta("enabled", "enabled", "bool", 0, 1, "primitive"),),
        ends=(
            end_device.meta,
            registers.meta,
        ),
    )

    def __init__(
        self,
        *,
        enabled: bool | None = None,
        end_device: EndDevice | None = None,
        registers: Iterable[Register] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.enabled = enabled
        if end_device is not None:
            self.end_device = end_device
        if registers is not None:
            EndDeviceFunction.registers.extend(self, registers)

    def add_register(self, register: Register) -> Self:
        return EndDeviceFunction.registers.add(self, register)

    def remove_register(self, register: Register) -> Self:
        return EndDeviceFunction.registers.remove(self, register)

    def clear_registers(self) -> Self:
        return EndDeviceFunction.registers.clear(self)

    def num_register(self) -> int:
        return EndDeviceFunction.registers.count(self)

    def get_register_by_mrid(self, mrid: str) -> Register | None:
        return EndDeviceFunction.registers.get_by_mrid(self, mrid)

"""CIM class ComModule (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.com_function import ComFunction


class ComModule(Asset):
    """An asset having communications capabilities that can be paired with a meter or other end
    device to provide the device with communication ability, through associated
    communication function. An end device that has communications capabilities through
    embedded hardware can use that function directly (without the communication module), or
    combine embedded communication function with additional communication functions provided
    through an external communication module (e.g. zigbee)."""

    __slots__ = ("_com_functions", "amr_system", "supports_autonomous_dst", "time_zone_offset")

    amr_system: str | None
    time_zone_offset: float | None  # Minutes
    supports_autonomous_dst: bool | None

    com_functions: Many[ComFunction] = Many(
        EndMeta(
            name="com_functions",
            cim_role="ComFunctions",
            target="cim_python_sdk.model.iec61968.metering.com_function:ComFunction",
            many=True,
            lower=0,
            upper=None,
            inverse="com_module",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ComModule",
        package="TC57CIM/IEC61968/Metering",
        guid="{EF20287A-38B8-441c-B30F-FD1A333DC294}",
        attributes=(
            AttrMeta("amr_system", "amrSystem", "str", 0, 1, "primitive"),
            AttrMeta("time_zone_offset", "timeZoneOffset", "Minutes", 0, 1, "cimdatatype"),
            AttrMeta("supports_autonomous_dst", "supportsAutonomousDst", "bool", 0, 1, "primitive"),
        ),
        ends=(com_functions.meta,),
    )

    def __init__(
        self,
        *,
        amr_system: str | None = None,
        time_zone_offset: float | None = None,
        supports_autonomous_dst: bool | None = None,
        com_functions: Iterable[ComFunction] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.amr_system = amr_system
        self.time_zone_offset = time_zone_offset
        self.supports_autonomous_dst = supports_autonomous_dst
        if com_functions is not None:
            ComModule.com_functions.extend(self, com_functions)

    def add_com_function(self, com_function: ComFunction) -> Self:
        return ComModule.com_functions.add(self, com_function)

    def remove_com_function(self, com_function: ComFunction) -> Self:
        return ComModule.com_functions.remove(self, com_function)

    def clear_com_functions(self) -> Self:
        return ComModule.com_functions.clear(self)

    def num_com_function(self) -> int:
        return ComModule.com_functions.count(self)

    def get_com_function_by_mrid(self, mrid: str) -> ComFunction | None:
        return ComModule.com_functions.get_by_mrid(self, mrid)

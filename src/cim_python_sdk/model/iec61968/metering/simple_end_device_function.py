"""CIM class SimpleEndDeviceFunction (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.metering.end_device_function import EndDeviceFunction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.end_device_function_kind import (
        EndDeviceFunctionKind,
    )


class SimpleEndDeviceFunction(EndDeviceFunction):
    """Simple end device function distinguished by 'kind'. Use this class for instances that
    cannot be represented by another end device function specialisations."""

    __slots__ = ("kind",)

    kind: EndDeviceFunctionKind | None

    _cim_meta = ClassMeta(
        cim_name="SimpleEndDeviceFunction",
        package="TC57CIM/IEC61968/Metering",
        guid="{A31060F5-6C63-4ddd-8F07-A06D752DA79A}",
        attributes=(AttrMeta("kind", "kind", "EndDeviceFunctionKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: EndDeviceFunctionKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind

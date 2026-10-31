"""CIM class Breaker (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.protected_switch import ProtectedSwitch

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Breaker(ProtectedSwitch):
    """A mechanical switching device capable of making, carrying, and breaking currents under
    normal circuit conditions and also making, carrying for a specified time, and breaking
    currents under specified abnormal circuit conditions e.g. those of short circuit."""

    __slots__ = ("in_transit_time",)

    in_transit_time: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="Breaker",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{380D92AA-1D80-4e84-A8EE-843DACEB59DD}",
        attributes=(AttrMeta("in_transit_time", "inTransitTime", "Seconds", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        in_transit_time: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.in_transit_time = in_transit_time

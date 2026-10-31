"""CIM class DisconnectingCircuitBreaker (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.wires.breaker import Breaker


class DisconnectingCircuitBreaker(Breaker):
    """A circuit breaking device including disconnecting function, eliminating the need for
    separate disconnectors."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="DisconnectingCircuitBreaker",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{E15222BE-C02A-4417-AED7-A395E55A943A}",
    )

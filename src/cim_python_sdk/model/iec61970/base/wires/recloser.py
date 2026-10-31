"""CIM class Recloser (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.wires.protected_switch import ProtectedSwitch


class Recloser(ProtectedSwitch):
    """Pole-mounted fault interrupter with built-in phase and ground relays, current
    transformer (CT), and supplemental controls."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="Recloser",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{6408BE78-ED1B-4fcc-9463-EBC827CDFEBB}",
    )

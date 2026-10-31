"""CIM class LoadBreakSwitch (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.wires.protected_switch import ProtectedSwitch


class LoadBreakSwitch(ProtectedSwitch):
    """A mechanical switching device capable of making, carrying, and breaking currents under
    normal operating conditions."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="LoadBreakSwitch",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{D64FF392-C9F8-4220-8861-1944D504F342}",
    )

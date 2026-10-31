"""CIM class Fuse (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.wires.switch import Switch


class Fuse(Switch):
    """An overcurrent protective device with a circuit opening fusible part that is heated and
    severed by the passage of overcurrent through it. A fuse is considered a switching
    device because it breaks current."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="Fuse",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{48B8830C-2798-4c86-8B89-01449EA9D4F6}",
    )

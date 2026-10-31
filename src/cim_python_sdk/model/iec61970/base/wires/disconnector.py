"""CIM class Disconnector (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.wires.switch import Switch


class Disconnector(Switch):
    """A manually operated or motor operated mechanical switching device used for changing the
    connections in a circuit, or for isolating a circuit or equipment from a source of
    power. It is required to open or close circuits when negligible current is broken or
    made."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="Disconnector",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{1B506DF7-CBD6-492a-8C9E-F6752F0F0185}",
    )

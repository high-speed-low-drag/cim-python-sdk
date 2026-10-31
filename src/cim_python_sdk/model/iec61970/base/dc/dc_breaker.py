"""CIM class DCBreaker (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.dc.dc_switch import DCSwitch


class DCBreaker(DCSwitch):
    """A breaker within a DC system."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="DCBreaker",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{CB3F5326-2F99-442b-A0EC-ED9CDC93E629}",
    )

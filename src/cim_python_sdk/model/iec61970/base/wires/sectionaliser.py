"""CIM class Sectionaliser (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.wires.switch import Switch


class Sectionaliser(Switch):
    """Automatic switch that will lock open to isolate a faulted section. It may, or may not,
    have load breaking capability. Its primary purpose is to provide fault sectionalising at
    locations where the fault current is either too high, or too low, for proper
    coordination of fuses."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="Sectionaliser",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{6F75B963-A39E-4dc7-B75B-E205EE11AE4F}",
    )

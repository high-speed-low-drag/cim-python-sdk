"""CIM enumeration GeneratorControlSource (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class GeneratorControlSource(CimEnum):
    """The source of controls for a generating unit."""

    unavailable = "unavailable"
    offAGC = "offAGC"
    onAGC = "onAGC"
    plantControl = "plantControl"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="GeneratorControlSource",
            package="TC57CIM/IEC61970/Base/Generation/Production",
            guid="{3C0C9F3D-956D-4459-A81A-40D922761537}",
            kind="enumeration",
        )
    )

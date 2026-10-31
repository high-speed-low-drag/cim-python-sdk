"""CIM enumeration EmissionValueSource (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EmissionValueSource(CimEnum):
    """The source of the emission value."""

    measured = "measured"
    calculated = "calculated"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EmissionValueSource",
            package="TC57CIM/IEC61970/Base/Generation/Production",
            guid="{CEFBC9A4-53DF-487d-B557-DA0A61E2D090}",
            kind="enumeration",
        )
    )

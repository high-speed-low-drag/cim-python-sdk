"""CIM enumeration Source (TC57CIM/IEC61970/Base/SCADA). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class Source(CimEnum):
    """Source gives information related to the origin of a value."""

    PROCESS = "PROCESS"
    DEFAULTED = "DEFAULTED"
    SUBSTITUTED = "SUBSTITUTED"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="Source",
            package="TC57CIM/IEC61970/Base/SCADA",
            guid="{2DDE9E7D-6C38-4e8d-83FD-E0CE637A0E37}",
            kind="enumeration",
        )
    )

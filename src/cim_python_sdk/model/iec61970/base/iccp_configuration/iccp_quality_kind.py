"""CIM enumeration ICCPQualityKind (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ICCPQualityKind(CimEnum):
    """Indicates the type of quality information that is to be exchanged. For protection events
    the value shall be "none"."""

    none = "none"
    qualityOnly = "qualityOnly"
    qualityAndTime = "qualityAndTime"
    extended = "extended"
    extendedwithQualityTime = "extendedwithQualityTime"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ICCPQualityKind",
            package="TC57CIM/IEC61970/Base/ICCPConfiguration",
            guid="{3151BAD5-095A-49e4-ABBC-CF40C5B0182E}",
            kind="enumeration",
        )
    )

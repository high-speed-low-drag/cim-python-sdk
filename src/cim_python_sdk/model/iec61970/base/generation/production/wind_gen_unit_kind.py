"""CIM enumeration WindGenUnitKind (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WindGenUnitKind(CimEnum):
    """Kind of wind generating unit."""

    offshore = "offshore"
    onshore = "onshore"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WindGenUnitKind",
            package="TC57CIM/IEC61970/Base/Generation/Production",
            guid="{F66917CD-B970-42ec-B82C-3696341AB38C}",
            kind="enumeration",
        )
    )

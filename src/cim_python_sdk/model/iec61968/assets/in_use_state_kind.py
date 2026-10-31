"""CIM enumeration InUseStateKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class InUseStateKind(CimEnum):
    """Possible 'in use' states that an asset can be in."""

    inUse = "inUse"
    readyForUse = "readyForUse"
    notReadyForUse = "notReadyForUse"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="InUseStateKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{2DACF751-AA54-4347-ABD3-A1F43DC35D98}",
            kind="enumeration",
        )
    )

"""CIM enumeration PetersenCoilModeKind (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PetersenCoilModeKind(CimEnum):
    """The mode of operation for a Petersen coil."""

    fixed = "fixed"
    manual = "manual"
    automaticPositioning = "automaticPositioning"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PetersenCoilModeKind",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{D7A85068-34C3-4fcd-ABCF-8D0867FEC0FF}",
            kind="enumeration",
        )
    )

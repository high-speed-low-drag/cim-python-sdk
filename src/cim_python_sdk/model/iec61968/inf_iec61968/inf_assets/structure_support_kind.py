"""CIM enumeration StructureSupportKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class StructureSupportKind(CimEnum):
    """Kind of structure support."""

    anchor = "anchor"
    guy = "guy"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="StructureSupportKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{5BD2EFA5-CD28-4785-B9A7-10EF38FD47C9}",
            kind="enumeration",
        )
    )

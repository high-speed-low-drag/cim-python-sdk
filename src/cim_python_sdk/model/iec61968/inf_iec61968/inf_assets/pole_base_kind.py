"""CIM enumeration PoleBaseKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PoleBaseKind(CimEnum):
    """Kind of base for poles."""

    asphalt = "asphalt"
    cement = "cement"
    dirt = "dirt"
    unknown = "unknown"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PoleBaseKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{34B79F57-EA29-4a4e-A3E4-A13C1383B3E7}",
            kind="enumeration",
        )
    )

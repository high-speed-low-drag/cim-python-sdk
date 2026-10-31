"""CIM enumeration UndergroundStructureKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class UndergroundStructureKind(CimEnum):
    """Kind of underground structure."""

    burd = "burd"
    enclosure = "enclosure"
    handhole = "handhole"
    manhole = "manhole"
    pad = "pad"
    subsurfaceEnclosure = "subsurfaceEnclosure"
    trench = "trench"
    tunnel = "tunnel"
    vault = "vault"
    pullbox = "pullbox"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="UndergroundStructureKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{328E2139-78D6-4b24-BA0D-486D58516712}",
            kind="enumeration",
        )
    )

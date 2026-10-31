"""CIM enumeration EmissionType (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EmissionType(CimEnum):
    """The type of emission."""

    sulfurDioxide = "sulfurDioxide"
    carbonDioxide = "carbonDioxide"
    nitrogenOxide = "nitrogenOxide"
    hydrogenSulfide = "hydrogenSulfide"
    chlorine = "chlorine"
    carbonDisulfide = "carbonDisulfide"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EmissionType",
            package="TC57CIM/IEC61970/Base/Generation/Production",
            guid="{6BD2D9BD-8C9F-421c-8E0B-2B6B81ECC31F}",
            kind="enumeration",
        )
    )

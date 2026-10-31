"""CIM enumeration HydroPlantStorageKind (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class HydroPlantStorageKind(CimEnum):
    """The type of hydro power plant."""

    runOfRiver = "runOfRiver"
    pumpedStorage = "pumpedStorage"
    storage = "storage"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="HydroPlantStorageKind",
            package="TC57CIM/IEC61970/Base/Generation/Production",
            guid="{9CBFF0AA-F3E6-4c65-A545-71017DDFC252}",
            kind="enumeration",
        )
    )

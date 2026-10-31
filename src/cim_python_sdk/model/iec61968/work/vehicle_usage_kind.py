"""CIM enumeration VehicleUsageKind (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class VehicleUsageKind(CimEnum):
    """Usage of a vehicle."""

    crew = "crew"
    user = "user"
    contractor = "contractor"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="VehicleUsageKind",
            package="TC57CIM/IEC61968/Work",
            guid="{EC6DF29B-5A61-4d44-96D8-6DD0D5D4DFB8}",
            kind="enumeration",
        )
    )

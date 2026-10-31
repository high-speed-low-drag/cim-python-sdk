"""CIM enumeration LandPropertyKind (TC57CIM/IEC61968/InfIEC61968/InfLocations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class LandPropertyKind(CimEnum):
    """Kind of (land) property."""

    building = "building"
    customerPremise = "customerPremise"
    depot = "depot"
    store = "store"
    substation = "substation"
    gridSupplyPoint = "gridSupplyPoint"
    external = "external"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="LandPropertyKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfLocations",
            guid="{85409433-8660-4b97-8E0D-CCA8BDE45DEC}",
            kind="enumeration",
        )
    )

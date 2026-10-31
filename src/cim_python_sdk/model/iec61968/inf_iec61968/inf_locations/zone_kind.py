"""CIM enumeration ZoneKind (TC57CIM/IEC61968/InfIEC61968/InfLocations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ZoneKind(CimEnum):
    """Kind of zone."""

    electricalNetwork = "electricalNetwork"
    specialRestrictionLand = "specialRestrictionLand"
    weatherZone = "weatherZone"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ZoneKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfLocations",
            guid="{58B3E8B9-CC93-4616-A231-BE1178D76314}",
            kind="enumeration",
        )
    )

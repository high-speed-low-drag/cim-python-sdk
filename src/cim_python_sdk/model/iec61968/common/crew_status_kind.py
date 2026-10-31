"""CIM enumeration CrewStatusKind (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CrewStatusKind(CimEnum):
    """Defines the current status of the Crew - assigned, arrived, etc."""

    arrived = "arrived"
    assigned = "assigned"
    awaitingCrewAssignment = "awaitingCrewAssignment"
    enroute = "enroute"
    fieldComplete = "fieldComplete"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CrewStatusKind",
            package="TC57CIM/IEC61968/Common",
            guid="{0256250A-25A5-444f-A3E8-EF37291A12FB}",
            kind="enumeration",
        )
    )

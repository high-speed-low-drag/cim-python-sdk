"""CIM enumeration OutageCauseKind (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OutageCauseKind(CimEnum):
    """This enumeration describes the primary cause of the outage - planned, unplanned, etc."""

    lightingStrike = "lightingStrike"
    animal = "animal"
    lineDown = "lineDown"
    poleDown = "poleDown"
    treeDown = "treeDown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OutageCauseKind",
            package="TC57CIM/IEC61968/Operations",
            guid="{288135CD-0CCB-48d9-906B-2E3998575562}",
            kind="enumeration",
        )
    )

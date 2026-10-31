"""CIM enumeration TowerConstructionKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TowerConstructionKind(CimEnum):
    """Kind of tower construction."""

    suspension = "suspension"
    tension = "tension"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TowerConstructionKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{05A4A8FC-A77F-4900-BAF4-E434DE69B080}",
            kind="enumeration",
        )
    )

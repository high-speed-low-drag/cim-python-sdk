"""CIM enumeration ContingencyEquipmentStatusKind (TC57CIM/IEC61970/Base/Contingency). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ContingencyEquipmentStatusKind(CimEnum):
    """Indicates the state which the contingency equipment is to be in when the contingency is
    applied."""

    inService = "inService"
    outOfService = "outOfService"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ContingencyEquipmentStatusKind",
            package="TC57CIM/IEC61970/Base/Contingency",
            guid="{CFCD4106-3B7F-4dac-8553-B06D8CB19117}",
            kind="enumeration",
        )
    )

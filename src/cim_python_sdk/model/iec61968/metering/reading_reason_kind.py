"""CIM enumeration ReadingReasonKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ReadingReasonKind(CimEnum):
    """Reason for the reading being taken."""

    installation = "installation"
    removal = "removal"
    inquiry = "inquiry"
    billing = "billing"
    moveIn = "moveIn"
    moveOut = "moveOut"
    demandReset = "demandReset"
    serviceDisconnect = "serviceDisconnect"
    serviceConnect = "serviceConnect"
    loadManagement = "loadManagement"
    loadResearch = "loadResearch"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ReadingReasonKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{7EE63604-51AF-4e8b-AFD4-6117CB2C7D8A}",
            kind="enumeration",
        )
    )

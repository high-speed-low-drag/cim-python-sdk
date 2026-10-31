"""CIM enumeration AutomaticDispInstTypeCommitment (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AutomaticDispInstTypeCommitment(CimEnum):
    """Commitment instruction types."""

    START_UP = "START_UP"
    SHUT_DOWN = "SHUT_DOWN"
    DR_DEPLOY = "DR_DEPLOY"
    DR_RELEASE = "DR_RELEASE"
    DR_ADJUSTMENT = "DR_ADJUSTMENT"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AutomaticDispInstTypeCommitment",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{46164A1F-AEF5-4d65-B589-49A23E056325}",
            kind="enumeration",
        )
    )

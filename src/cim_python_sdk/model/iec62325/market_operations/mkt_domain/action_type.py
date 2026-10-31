"""CIM enumeration ActionType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ActionType(CimEnum):
    """Action type associated with an ActionRequest against a ParticipantInterfaces::Trade."""

    CANCEL = "CANCEL"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ActionType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{5FF231B0-DE11-4e32-B970-0E658986ABCD}",
            kind="enumeration",
        )
    )

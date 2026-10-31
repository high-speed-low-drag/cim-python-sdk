"""CIM enumeration MarketEventStatusKind (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MarketEventStatusKind(CimEnum):
    """Market event status types."""

    active = "active"
    cancelled = "cancelled"
    completed = "completed"
    planned = "planned"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MarketEventStatusKind",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{C140C991-419D-4093-9496-7C884CD999DA}",
            kind="enumeration",
        )
    )

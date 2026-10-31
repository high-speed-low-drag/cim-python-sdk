"""CIM enumeration MarketStatementDocStatus (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MarketStatementDocStatus(CimEnum):
    """market statement document status"""

    APPROVED = "APPROVED"
    CANCELLED = "CANCELLED"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MarketStatementDocStatus",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{4480C85A-D453-4552-8264-6FC758A87B1B}",
            kind="enumeration",
        )
    )

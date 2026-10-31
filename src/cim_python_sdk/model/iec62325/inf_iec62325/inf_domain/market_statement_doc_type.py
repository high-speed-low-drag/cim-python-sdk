"""CIM enumeration MarketStatementDocType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MarketStatementDocType(CimEnum):
    """market statement document type"""

    CREDIT = "CREDIT"
    MARKET_INITIAL = "MARKET_INITIAL"
    MARKET_RECALC = "MARKET_RECALC"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MarketStatementDocType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{FA72604B-B44B-4c63-9BD7-6525568312C5}",
            kind="enumeration",
        )
    )

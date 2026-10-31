"""CIM enumeration MarketStatementDescription (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MarketStatementDescription(CimEnum):
    """Description of market statement"""

    DAILY_INITIAL_CREDIT = "DAILY_INITIAL_CREDIT"
    DAILY_INITIAL_MARKET = "DAILY_INITIAL_MARKET"
    MONTHLY_INITIAL_MARKET = "MONTHLY_INITIAL_MARKET"
    DAILY_RECALC_MARKET = "DAILY_RECALC_MARKET"
    MONTHLY_RECALC_MARKET = "MONTHLY_RECALC_MARKET"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MarketStatementDescription",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{3F2FEF60-EB83-434c-87B5-39B726201FEE}",
            kind="enumeration",
        )
    )

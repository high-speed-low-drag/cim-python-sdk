"""CIM enumeration MarketStatementLineItemAliasName (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MarketStatementLineItemAliasName(CimEnum):
    """market statement line item alias name"""

    TRADE_DATE = "TRADE_DATE"
    PARENT_CHARGE_GROUP = "PARENT_CHARGE_GROUP"
    CHARGE_GROUP = "CHARGE_GROUP"
    CHARGE_CODE_SUMMARY = "CHARGE_CODE_SUMMARY"
    CHARGE_CODE_INTERVAL_TOTAL = "CHARGE_CODE_INTERVAL_TOTAL"
    CHARGE_CODE_INTERVAL_DETAIL = "CHARGE_CODE_INTERVAL_DETAIL"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MarketStatementLineItemAliasName",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{2F07BFB9-CA35-4767-9306-2C9756789465}",
            kind="enumeration",
        )
    )

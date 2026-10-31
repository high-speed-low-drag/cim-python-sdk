"""CIM class BilateralTransaction (TC57CIM/IEC62325/InfIEC62325/InfMarketOperations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from typing import Any


class BilateralTransaction(CimObject):
    """Bilateral transaction"""

    __slots__ = (
        "curtail_time_max",
        "curtail_time_min",
        "market_type",
        "purchase_time_max",
        "purchase_time_min",
        "scope",
        "total_tran_charge_max",
        "transaction_type",
    )

    scope: str | None
    transaction_type: str | None
    market_type: str | None
    purchase_time_min: int | None
    purchase_time_max: int | None
    curtail_time_min: int | None
    curtail_time_max: int | None
    total_tran_charge_max: _decimal.Decimal | None  # Money

    _cim_meta = ClassMeta(
        cim_name="BilateralTransaction",
        package="TC57CIM/IEC62325/InfIEC62325/InfMarketOperations",
        guid="{28E537B0-A5D2-4482-86F7-AF980E2C1A1C}",
        attributes=(
            AttrMeta("scope", "scope", "str", 0, 1, "primitive"),
            AttrMeta("transaction_type", "transactionType", "str", 0, 1, "primitive"),
            AttrMeta("market_type", "marketType", "str", 0, 1, "primitive"),
            AttrMeta("purchase_time_min", "purchaseTimeMin", "int", 0, 1, "primitive"),
            AttrMeta("purchase_time_max", "purchaseTimeMax", "int", 0, 1, "primitive"),
            AttrMeta("curtail_time_min", "curtailTimeMin", "int", 0, 1, "primitive"),
            AttrMeta("curtail_time_max", "curtailTimeMax", "int", 0, 1, "primitive"),
            AttrMeta("total_tran_charge_max", "totalTranChargeMax", "Money", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        scope: str | None = None,
        transaction_type: str | None = None,
        market_type: str | None = None,
        purchase_time_min: int | None = None,
        purchase_time_max: int | None = None,
        curtail_time_min: int | None = None,
        curtail_time_max: int | None = None,
        total_tran_charge_max: _decimal.Decimal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.scope = scope
        self.transaction_type = transaction_type
        self.market_type = market_type
        self.purchase_time_min = purchase_time_min
        self.purchase_time_max = purchase_time_max
        self.curtail_time_min = curtail_time_min
        self.curtail_time_max = curtail_time_max
        self.total_tran_charge_max = total_tran_charge_max

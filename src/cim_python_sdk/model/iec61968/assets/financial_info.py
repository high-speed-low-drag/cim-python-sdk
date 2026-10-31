"""CIM class FinancialInfo (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61970.base.domain.integer_quantity import IntegerQuantity


class FinancialInfo(IdentifiedObject):
    """Various current financial properties associated with a particular asset. Historical
    properties may be determined by ActivityRecords associated with the asset."""

    __slots__ = (
        "_asset",
        "account",
        "actual_purchase_cost",
        "cost_description",
        "cost_type",
        "financial_value",
        "plant_transfer_date_time",
        "purchase_date_time",
        "purchase_order_number",
        "quantity",
        "value_date_time",
        "warranty_end_date_time",
    )

    financial_value: _decimal.Decimal | None  # Money
    value_date_time: _dt.datetime | None
    plant_transfer_date_time: _dt.datetime | None
    warranty_end_date_time: _dt.datetime | None
    purchase_date_time: _dt.datetime | None
    purchase_order_number: str | None
    actual_purchase_cost: _decimal.Decimal | None  # Money
    account: str | None
    quantity: IntegerQuantity | None
    cost_description: str | None
    cost_type: str | None

    asset: One[Asset] = One(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="financial_info",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FinancialInfo",
        package="TC57CIM/IEC61968/Assets",
        guid="{2286987A-2E81-4f68-A13E-86A855D3441C}",
        attributes=(
            AttrMeta("financial_value", "financialValue", "Money", 0, 1, "cimdatatype"),
            AttrMeta("value_date_time", "valueDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta(
                "plant_transfer_date_time", "plantTransferDateTime", "datetime", 0, 1, "primitive"
            ),
            AttrMeta(
                "warranty_end_date_time", "warrantyEndDateTime", "datetime", 0, 1, "primitive"
            ),
            AttrMeta("purchase_date_time", "purchaseDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("purchase_order_number", "purchaseOrderNumber", "str", 0, 1, "primitive"),
            AttrMeta("actual_purchase_cost", "actualPurchaseCost", "Money", 0, 1, "cimdatatype"),
            AttrMeta("account", "account", "str", 0, 1, "primitive"),
            AttrMeta("quantity", "quantity", "IntegerQuantity", 0, 1, "compound"),
            AttrMeta("cost_description", "costDescription", "str", 0, 1, "primitive"),
            AttrMeta("cost_type", "costType", "str", 0, 1, "primitive"),
        ),
        ends=(asset.meta,),
    )

    def __init__(
        self,
        *,
        financial_value: _decimal.Decimal | None = None,
        value_date_time: _dt.datetime | None = None,
        plant_transfer_date_time: _dt.datetime | None = None,
        warranty_end_date_time: _dt.datetime | None = None,
        purchase_date_time: _dt.datetime | None = None,
        purchase_order_number: str | None = None,
        actual_purchase_cost: _decimal.Decimal | None = None,
        account: str | None = None,
        quantity: IntegerQuantity | None = None,
        cost_description: str | None = None,
        cost_type: str | None = None,
        asset: Asset | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.financial_value = financial_value
        self.value_date_time = value_date_time
        self.plant_transfer_date_time = plant_transfer_date_time
        self.warranty_end_date_time = warranty_end_date_time
        self.purchase_date_time = purchase_date_time
        self.purchase_order_number = purchase_order_number
        self.actual_purchase_cost = actual_purchase_cost
        self.account = account
        self.quantity = quantity
        self.cost_description = cost_description
        self.cost_type = cost_type
        if asset is not None:
            self.asset = asset

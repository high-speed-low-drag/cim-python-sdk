"""CIM class ErpPayment (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item import (
        ErpInvoiceLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable_line_item import (
        ErpPayableLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_line_item import (
        ErpRecLineItem,
    )


class ErpPayment(ErpDocument):
    """Payment infromation and status for any individual line item of an ErpInvoice (e.g., when
    payment is from a customer). ErpPayable is also updated when payment is to a supplier
    and ErpReceivable is updated when payment is from a customer. Multiple payments can be
    made against a single line item and an individual payment can apply to more that one
    line item."""

    __slots__ = (
        "_erp_invoice_line_items",
        "_erp_payable_line_items",
        "_erp_rec_line_items",
        "terms_payment",
    )

    terms_payment: str | None

    erp_invoice_line_items: Many[ErpInvoiceLineItem] = Many(
        EndMeta(
            name="erp_invoice_line_items",
            cim_role="ErpInvoiceLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item:ErpInvoiceLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_payments",
            aggregation="none",
        )
    )
    erp_payable_line_items: Many[ErpPayableLineItem] = Many(
        EndMeta(
            name="erp_payable_line_items",
            cim_role="ErpPayableLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable_line_item:ErpPayableLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_payments",
            aggregation="none",
        )
    )
    erp_rec_line_items: Many[ErpRecLineItem] = Many(
        EndMeta(
            name="erp_rec_line_items",
            cim_role="ErpRecLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_rec_line_item:ErpRecLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_payments",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpPayment",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{2A7E7F00-35B2-44ba-ABFA-659EF1E521DE}",
        attributes=(AttrMeta("terms_payment", "termsPayment", "str", 0, 1, "primitive"),),
        ends=(
            erp_invoice_line_items.meta,
            erp_payable_line_items.meta,
            erp_rec_line_items.meta,
        ),
    )

    def __init__(
        self,
        *,
        terms_payment: str | None = None,
        erp_invoice_line_items: Iterable[ErpInvoiceLineItem] | None = None,
        erp_payable_line_items: Iterable[ErpPayableLineItem] | None = None,
        erp_rec_line_items: Iterable[ErpRecLineItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.terms_payment = terms_payment
        if erp_invoice_line_items is not None:
            ErpPayment.erp_invoice_line_items.extend(self, erp_invoice_line_items)
        if erp_payable_line_items is not None:
            ErpPayment.erp_payable_line_items.extend(self, erp_payable_line_items)
        if erp_rec_line_items is not None:
            ErpPayment.erp_rec_line_items.extend(self, erp_rec_line_items)

    def add_erp_invoice_line_item(self, erp_invoice_line_item: ErpInvoiceLineItem) -> Self:
        return ErpPayment.erp_invoice_line_items.add(self, erp_invoice_line_item)

    def remove_erp_invoice_line_item(self, erp_invoice_line_item: ErpInvoiceLineItem) -> Self:
        return ErpPayment.erp_invoice_line_items.remove(self, erp_invoice_line_item)

    def clear_erp_invoice_line_items(self) -> Self:
        return ErpPayment.erp_invoice_line_items.clear(self)

    def num_erp_invoice_line_item(self) -> int:
        return ErpPayment.erp_invoice_line_items.count(self)

    def get_erp_invoice_line_item_by_mrid(self, mrid: str) -> ErpInvoiceLineItem | None:
        return ErpPayment.erp_invoice_line_items.get_by_mrid(self, mrid)

    def add_erp_payable_line_item(self, erp_payable_line_item: ErpPayableLineItem) -> Self:
        return ErpPayment.erp_payable_line_items.add(self, erp_payable_line_item)

    def remove_erp_payable_line_item(self, erp_payable_line_item: ErpPayableLineItem) -> Self:
        return ErpPayment.erp_payable_line_items.remove(self, erp_payable_line_item)

    def clear_erp_payable_line_items(self) -> Self:
        return ErpPayment.erp_payable_line_items.clear(self)

    def num_erp_payable_line_item(self) -> int:
        return ErpPayment.erp_payable_line_items.count(self)

    def get_erp_payable_line_item_by_mrid(self, mrid: str) -> ErpPayableLineItem | None:
        return ErpPayment.erp_payable_line_items.get_by_mrid(self, mrid)

    def add_erp_rec_line_item(self, erp_rec_line_item: ErpRecLineItem) -> Self:
        return ErpPayment.erp_rec_line_items.add(self, erp_rec_line_item)

    def remove_erp_rec_line_item(self, erp_rec_line_item: ErpRecLineItem) -> Self:
        return ErpPayment.erp_rec_line_items.remove(self, erp_rec_line_item)

    def clear_erp_rec_line_items(self) -> Self:
        return ErpPayment.erp_rec_line_items.clear(self)

    def num_erp_rec_line_item(self) -> int:
        return ErpPayment.erp_rec_line_items.count(self)

    def get_erp_rec_line_item_by_mrid(self, mrid: str) -> ErpRecLineItem | None:
        return ErpPayment.erp_rec_line_items.get_by_mrid(self, mrid)

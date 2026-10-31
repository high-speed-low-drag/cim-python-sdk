"""CIM class ErpPayable (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable_line_item import (
        ErpPayableLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.contractor_item import ContractorItem


class ErpPayable(ErpDocument):
    """A transaction that represents an invoice from a supplier. A payable (or voucher) is an
    open item, approved and ready for payment, in the Accounts Payable ledger."""

    __slots__ = ("_contractor_items", "_erp_payable_line_items")

    erp_payable_line_items: Many[ErpPayableLineItem] = Many(
        EndMeta(
            name="erp_payable_line_items",
            cim_role="ErpPayableLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_payable_line_item:ErpPayableLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_payable",
            aggregation="none",
        )
    )
    contractor_items: Many[ContractorItem] = Many(
        EndMeta(
            name="contractor_items",
            cim_role="ContractorItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.contractor_item:ContractorItem",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_payables",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpPayable",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{7E9CB1F8-B68D-4dec-B5AA-50E8C891FA04}",
        ends=(
            erp_payable_line_items.meta,
            contractor_items.meta,
        ),
    )

    def __init__(
        self,
        *,
        erp_payable_line_items: Iterable[ErpPayableLineItem] | None = None,
        contractor_items: Iterable[ContractorItem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_payable_line_items is not None:
            ErpPayable.erp_payable_line_items.extend(self, erp_payable_line_items)
        if contractor_items is not None:
            ErpPayable.contractor_items.extend(self, contractor_items)

    def add_erp_payable_line_item(self, erp_payable_line_item: ErpPayableLineItem) -> Self:
        return ErpPayable.erp_payable_line_items.add(self, erp_payable_line_item)

    def remove_erp_payable_line_item(self, erp_payable_line_item: ErpPayableLineItem) -> Self:
        return ErpPayable.erp_payable_line_items.remove(self, erp_payable_line_item)

    def clear_erp_payable_line_items(self) -> Self:
        return ErpPayable.erp_payable_line_items.clear(self)

    def num_erp_payable_line_item(self) -> int:
        return ErpPayable.erp_payable_line_items.count(self)

    def get_erp_payable_line_item_by_mrid(self, mrid: str) -> ErpPayableLineItem | None:
        return ErpPayable.erp_payable_line_items.get_by_mrid(self, mrid)

    def add_contractor_item(self, contractor_item: ContractorItem) -> Self:
        return ErpPayable.contractor_items.add(self, contractor_item)

    def remove_contractor_item(self, contractor_item: ContractorItem) -> Self:
        return ErpPayable.contractor_items.remove(self, contractor_item)

    def clear_contractor_items(self) -> Self:
        return ErpPayable.contractor_items.clear(self)

    def num_contractor_item(self) -> int:
        return ErpPayable.contractor_items.count(self)

    def get_contractor_item_by_mrid(self, mrid: str) -> ContractorItem | None:
        return ErpPayable.contractor_items.get_by_mrid(self, mrid)

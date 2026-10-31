"""CIM class UserAttribute (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.procedure_data_set import ProcedureDataSet
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification import Specification
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item import (
        ErpInvoiceLineItem,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger_entry import (
        ErpLedgerEntry,
    )
    from cim_python_sdk.model.iec61968.payment_metering.transaction import Transaction
    from cim_python_sdk.model.iec61970.base.domain.string_quantity import StringQuantity


class UserAttribute(CimObject):
    """Generic name-value pair class, with optional sequence number and units for value; can be
    used to model parts of information exchange when concrete types are not known in
    advance."""

    __slots__ = (
        "_erp_invoice_line_items",
        "_erp_ledger_entries",
        "_procedure_data_sets",
        "_property_specification",
        "_rating_specification",
        "_transaction",
        "name",
        "sequence_number",
        "value",
    )

    sequence_number: int | None
    name: str | None
    value: StringQuantity | None

    transaction: One[Transaction] = One(
        EndMeta(
            name="transaction",
            cim_role="Transaction",
            target="cim_python_sdk.model.iec61968.payment_metering.transaction:Transaction",
            many=False,
            lower=0,
            upper=1,
            inverse="user_attributes",
            aggregation="none",
        )
    )
    erp_invoice_line_items: Many[ErpInvoiceLineItem] = Many(
        EndMeta(
            name="erp_invoice_line_items",
            cim_role="ErpInvoiceLineItems",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice_line_item:ErpInvoiceLineItem",
            many=True,
            lower=0,
            upper=None,
            inverse="user_attributes",
            aggregation="none",
        )
    )
    procedure_data_sets: Many[ProcedureDataSet] = Many(
        EndMeta(
            name="procedure_data_sets",
            cim_role="ProcedureDataSets",
            target="cim_python_sdk.model.iec61968.assets.procedure_data_set:ProcedureDataSet",
            many=True,
            lower=0,
            upper=None,
            inverse="properties",
            aggregation="none",
        )
    )
    property_specification: One[Specification] = One(
        EndMeta(
            name="property_specification",
            cim_role="PropertySpecification",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification:Specification",
            many=False,
            lower=0,
            upper=1,
            inverse="asset_properites",
            aggregation="none",
        )
    )
    erp_ledger_entries: Many[ErpLedgerEntry] = Many(
        EndMeta(
            name="erp_ledger_entries",
            cim_role="ErpLedgerEntries",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_ledger_entry:ErpLedgerEntry",
            many=True,
            lower=0,
            upper=None,
            inverse="user_attributes",
            aggregation="none",
        )
    )
    rating_specification: One[Specification] = One(
        EndMeta(
            name="rating_specification",
            cim_role="RatingSpecification",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.specification:Specification",
            many=False,
            lower=0,
            upper=1,
            inverse="ratings",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="UserAttribute",
        package="TC57CIM/IEC61968/Common",
        guid="{33A9E156-1160-4c87-B9BC-EF96C09A6BFB}",
        attributes=(
            AttrMeta("sequence_number", "sequenceNumber", "int", 0, 1, "primitive"),
            AttrMeta("name", "name", "str", 0, 1, "primitive"),
            AttrMeta("value", "value", "StringQuantity", 0, 1, "compound"),
        ),
        ends=(
            transaction.meta,
            erp_invoice_line_items.meta,
            procedure_data_sets.meta,
            property_specification.meta,
            erp_ledger_entries.meta,
            rating_specification.meta,
        ),
    )

    def __init__(
        self,
        *,
        sequence_number: int | None = None,
        name: str | None = None,
        value: StringQuantity | None = None,
        transaction: Transaction | None = None,
        erp_invoice_line_items: Iterable[ErpInvoiceLineItem] | None = None,
        procedure_data_sets: Iterable[ProcedureDataSet] | None = None,
        property_specification: Specification | None = None,
        erp_ledger_entries: Iterable[ErpLedgerEntry] | None = None,
        rating_specification: Specification | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence_number = sequence_number
        self.name = name
        self.value = value
        if transaction is not None:
            self.transaction = transaction
        if erp_invoice_line_items is not None:
            UserAttribute.erp_invoice_line_items.extend(self, erp_invoice_line_items)
        if procedure_data_sets is not None:
            UserAttribute.procedure_data_sets.extend(self, procedure_data_sets)
        if property_specification is not None:
            self.property_specification = property_specification
        if erp_ledger_entries is not None:
            UserAttribute.erp_ledger_entries.extend(self, erp_ledger_entries)
        if rating_specification is not None:
            self.rating_specification = rating_specification

    def add_erp_invoice_line_item(self, erp_invoice_line_item: ErpInvoiceLineItem) -> Self:
        return UserAttribute.erp_invoice_line_items.add(self, erp_invoice_line_item)

    def remove_erp_invoice_line_item(self, erp_invoice_line_item: ErpInvoiceLineItem) -> Self:
        return UserAttribute.erp_invoice_line_items.remove(self, erp_invoice_line_item)

    def clear_erp_invoice_line_items(self) -> Self:
        return UserAttribute.erp_invoice_line_items.clear(self)

    def num_erp_invoice_line_item(self) -> int:
        return UserAttribute.erp_invoice_line_items.count(self)

    def get_erp_invoice_line_item_by_mrid(self, mrid: str) -> ErpInvoiceLineItem | None:
        return UserAttribute.erp_invoice_line_items.get_by_mrid(self, mrid)

    def add_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return UserAttribute.procedure_data_sets.add(self, procedure_data_set)

    def remove_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return UserAttribute.procedure_data_sets.remove(self, procedure_data_set)

    def clear_procedure_data_sets(self) -> Self:
        return UserAttribute.procedure_data_sets.clear(self)

    def num_procedure_data_set(self) -> int:
        return UserAttribute.procedure_data_sets.count(self)

    def get_procedure_data_set_by_mrid(self, mrid: str) -> ProcedureDataSet | None:
        return UserAttribute.procedure_data_sets.get_by_mrid(self, mrid)

    def add_erp_ledger_entry(self, erp_ledger_entry: ErpLedgerEntry) -> Self:
        return UserAttribute.erp_ledger_entries.add(self, erp_ledger_entry)

    def remove_erp_ledger_entry(self, erp_ledger_entry: ErpLedgerEntry) -> Self:
        return UserAttribute.erp_ledger_entries.remove(self, erp_ledger_entry)

    def clear_erp_ledger_entries(self) -> Self:
        return UserAttribute.erp_ledger_entries.clear(self)

    def num_erp_ledger_entry(self) -> int:
        return UserAttribute.erp_ledger_entries.count(self)

    def get_erp_ledger_entry_by_mrid(self, mrid: str) -> ErpLedgerEntry | None:
        return UserAttribute.erp_ledger_entries.get_by_mrid(self, mrid)

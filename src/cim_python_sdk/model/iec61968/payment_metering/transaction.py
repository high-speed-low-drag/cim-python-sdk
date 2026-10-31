"""CIM class Transaction (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.user_attribute import UserAttribute
    from cim_python_sdk.model.iec61968.customers.customer_account import CustomerAccount
    from cim_python_sdk.model.iec61968.customers.pricing_structure import PricingStructure
    from cim_python_sdk.model.iec61968.metering.meter import Meter
    from cim_python_sdk.model.iec61968.payment_metering.auxiliary_account import AuxiliaryAccount
    from cim_python_sdk.model.iec61968.payment_metering.cashier_shift import CashierShift
    from cim_python_sdk.model.iec61968.payment_metering.line_detail import LineDetail
    from cim_python_sdk.model.iec61968.payment_metering.receipt import Receipt
    from cim_python_sdk.model.iec61968.payment_metering.transaction_kind import TransactionKind
    from cim_python_sdk.model.iec61968.payment_metering.vendor_shift import VendorShift


class Transaction(IdentifiedObject):
    """The record of details of payment for service or token sale."""

    __slots__ = (
        "_auxiliary_account",
        "_cashier_shift",
        "_customer_account",
        "_meter",
        "_pricing_structure",
        "_receipt",
        "_user_attributes",
        "_vendor_shift",
        "diverse_reference",
        "donor_reference",
        "kind",
        "line",
        "receiver_reference",
        "reversed_id",
        "service_units_energy",
        "service_units_error",
    )

    kind: TransactionKind | None
    receiver_reference: str | None
    donor_reference: str | None
    diverse_reference: str | None
    reversed_id: str | None
    service_units_energy: float | None  # RealEnergy
    service_units_error: float | None  # RealEnergy
    line: LineDetail | None

    customer_account: One[CustomerAccount] = One(
        EndMeta(
            name="customer_account",
            cim_role="CustomerAccount",
            target="cim_python_sdk.model.iec61968.customers.customer_account:CustomerAccount",
            many=False,
            lower=0,
            upper=1,
            inverse="payment_transactions",
            aggregation="none",
        )
    )
    pricing_structure: One[PricingStructure] = One(
        EndMeta(
            name="pricing_structure",
            cim_role="PricingStructure",
            target="cim_python_sdk.model.iec61968.customers.pricing_structure:PricingStructure",
            many=False,
            lower=0,
            upper=1,
            inverse="transactions",
            aggregation="none",
        )
    )
    user_attributes: Many[UserAttribute] = Many(
        EndMeta(
            name="user_attributes",
            cim_role="UserAttributes",
            target="cim_python_sdk.model.iec61968.common.user_attribute:UserAttribute",
            many=True,
            lower=0,
            upper=None,
            inverse="transaction",
            aggregation="none",
        )
    )
    cashier_shift: One[CashierShift] = One(
        EndMeta(
            name="cashier_shift",
            cim_role="CashierShift",
            target="cim_python_sdk.model.iec61968.payment_metering.cashier_shift:CashierShift",
            many=False,
            lower=0,
            upper=1,
            inverse="transactions",
            aggregation="none",
        )
    )
    receipt: One[Receipt] = One(
        EndMeta(
            name="receipt",
            cim_role="Receipt",
            target="cim_python_sdk.model.iec61968.payment_metering.receipt:Receipt",
            many=False,
            lower=0,
            upper=1,
            inverse="transactions",
            aggregation="none",
        )
    )
    meter: One[Meter] = One(
        EndMeta(
            name="meter",
            cim_role="Meter",
            target="cim_python_sdk.model.iec61968.metering.meter:Meter",
            many=False,
            lower=0,
            upper=1,
            inverse="vending_transactions",
            aggregation="none",
        )
    )
    vendor_shift: One[VendorShift] = One(
        EndMeta(
            name="vendor_shift",
            cim_role="VendorShift",
            target="cim_python_sdk.model.iec61968.payment_metering.vendor_shift:VendorShift",
            many=False,
            lower=0,
            upper=1,
            inverse="transactions",
            aggregation="none",
        )
    )
    auxiliary_account: One[AuxiliaryAccount] = One(
        EndMeta(
            name="auxiliary_account",
            cim_role="AuxiliaryAccount",
            target="cim_python_sdk.model.iec61968.payment_metering.auxiliary_account:AuxiliaryAccount",
            many=False,
            lower=0,
            upper=1,
            inverse="payment_transactions",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Transaction",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{5D8018E8-DD12-4e67-B98A-26B79A920B63}",
        attributes=(
            AttrMeta("kind", "kind", "TransactionKind", 0, 1, "enumeration"),
            AttrMeta("receiver_reference", "receiverReference", "str", 0, 1, "primitive"),
            AttrMeta("donor_reference", "donorReference", "str", 0, 1, "primitive"),
            AttrMeta("diverse_reference", "diverseReference", "str", 0, 1, "primitive"),
            AttrMeta("reversed_id", "reversedId", "str", 0, 1, "primitive"),
            AttrMeta(
                "service_units_energy", "serviceUnitsEnergy", "RealEnergy", 0, 1, "cimdatatype"
            ),
            AttrMeta("service_units_error", "serviceUnitsError", "RealEnergy", 0, 1, "cimdatatype"),
            AttrMeta("line", "line", "LineDetail", 0, 1, "compound"),
        ),
        ends=(
            customer_account.meta,
            pricing_structure.meta,
            user_attributes.meta,
            cashier_shift.meta,
            receipt.meta,
            meter.meta,
            vendor_shift.meta,
            auxiliary_account.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: TransactionKind | None = None,
        receiver_reference: str | None = None,
        donor_reference: str | None = None,
        diverse_reference: str | None = None,
        reversed_id: str | None = None,
        service_units_energy: float | None = None,
        service_units_error: float | None = None,
        line: LineDetail | None = None,
        customer_account: CustomerAccount | None = None,
        pricing_structure: PricingStructure | None = None,
        user_attributes: Iterable[UserAttribute] | None = None,
        cashier_shift: CashierShift | None = None,
        receipt: Receipt | None = None,
        meter: Meter | None = None,
        vendor_shift: VendorShift | None = None,
        auxiliary_account: AuxiliaryAccount | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.receiver_reference = receiver_reference
        self.donor_reference = donor_reference
        self.diverse_reference = diverse_reference
        self.reversed_id = reversed_id
        self.service_units_energy = service_units_energy
        self.service_units_error = service_units_error
        self.line = line
        if customer_account is not None:
            self.customer_account = customer_account
        if pricing_structure is not None:
            self.pricing_structure = pricing_structure
        if user_attributes is not None:
            Transaction.user_attributes.extend(self, user_attributes)
        if cashier_shift is not None:
            self.cashier_shift = cashier_shift
        if receipt is not None:
            self.receipt = receipt
        if meter is not None:
            self.meter = meter
        if vendor_shift is not None:
            self.vendor_shift = vendor_shift
        if auxiliary_account is not None:
            self.auxiliary_account = auxiliary_account

    def add_user_attribute(self, user_attribute: UserAttribute) -> Self:
        return Transaction.user_attributes.add(self, user_attribute)

    def remove_user_attribute(self, user_attribute: UserAttribute) -> Self:
        return Transaction.user_attributes.remove(self, user_attribute)

    def clear_user_attributes(self) -> Self:
        return Transaction.user_attributes.clear(self)

    def num_user_attribute(self) -> int:
        return Transaction.user_attributes.count(self)

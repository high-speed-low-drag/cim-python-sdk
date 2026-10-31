"""CIM class CustomerAccount (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.customers.account_notification import AccountNotification
    from cim_python_sdk.model.iec61968.customers.customer import Customer
    from cim_python_sdk.model.iec61968.customers.customer_agreement import CustomerAgreement
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.customer_billing_info import (
        CustomerBillingInfo,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.work_billing_info import (
        WorkBillingInfo,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice import ErpInvoice
    from cim_python_sdk.model.iec61968.metering.meter_read_schedule import MeterReadSchedule
    from cim_python_sdk.model.iec61968.payment_metering.transaction import Transaction


class CustomerAccount(Document):
    """Assignment of a group of products and services purchased by the customer through a
    customer agreement, used as a mechanism for customer billing and payment. It contains
    common information from the various types of customer agreements to create billings
    (invoices) for a customer and receive payment."""

    __slots__ = (
        "_account_notification",
        "_customer",
        "_customer_agreements",
        "_customer_billing_infos",
        "_erp_invoicees",
        "_meter_read_schedule",
        "_payment_transactions",
        "_work_billing_infos",
        "billing_cycle",
        "budget_bill",
        "last_bill_amount",
    )

    billing_cycle: str | None
    budget_bill: str | None
    last_bill_amount: _decimal.Decimal | None  # Money

    payment_transactions: Many[Transaction] = Many(
        EndMeta(
            name="payment_transactions",
            cim_role="PaymentTransactions",
            target="cim_python_sdk.model.iec61968.payment_metering.transaction:Transaction",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_account",
            aggregation="none",
        )
    )
    customer_billing_infos: Many[CustomerBillingInfo] = Many(
        EndMeta(
            name="customer_billing_infos",
            cim_role="CustomerBillingInfos",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.customer_billing_info:CustomerBillingInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_account",
            aggregation="none",
        )
    )
    customer_agreements: Many[CustomerAgreement] = Many(
        EndMeta(
            name="customer_agreements",
            cim_role="CustomerAgreements",
            target="cim_python_sdk.model.iec61968.customers.customer_agreement:CustomerAgreement",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_account",
            aggregation="none",
        )
    )
    customer: One[Customer] = One(
        EndMeta(
            name="customer",
            cim_role="Customer",
            target="cim_python_sdk.model.iec61968.customers.customer:Customer",
            many=False,
            lower=1,
            upper=1,
            inverse="customer_accounts",
            aggregation="none",
        )
    )
    work_billing_infos: Many[WorkBillingInfo] = Many(
        EndMeta(
            name="work_billing_infos",
            cim_role="WorkBillingInfos",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_customers.work_billing_info:WorkBillingInfo",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_account",
            aggregation="none",
        )
    )
    meter_read_schedule: One[MeterReadSchedule] = One(
        EndMeta(
            name="meter_read_schedule",
            cim_role="MeterReadSchedule",
            target="cim_python_sdk.model.iec61968.metering.meter_read_schedule:MeterReadSchedule",
            many=False,
            lower=0,
            upper=1,
            inverse="customer_account",
            aggregation="none",
        )
    )
    erp_invoicees: Many[ErpInvoice] = Many(
        EndMeta(
            name="erp_invoicees",
            cim_role="ErpInvoicees",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_invoice:ErpInvoice",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_account",
            aggregation="none",
        )
    )
    account_notification: Many[AccountNotification] = Many(
        EndMeta(
            name="account_notification",
            cim_role="AccountNotification",
            target="cim_python_sdk.model.iec61968.customers.account_notification:AccountNotification",
            many=True,
            lower=0,
            upper=None,
            inverse="customer_account",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CustomerAccount",
        package="TC57CIM/IEC61968/Customers",
        guid="{FCC72824-DB71-49ff-A5B7-BF1675CDA0A5}",
        attributes=(
            AttrMeta("billing_cycle", "billingCycle", "str", 0, 1, "primitive"),
            AttrMeta("budget_bill", "budgetBill", "str", 0, 1, "primitive"),
            AttrMeta("last_bill_amount", "lastBillAmount", "Money", 0, 1, "cimdatatype"),
        ),
        ends=(
            payment_transactions.meta,
            customer_billing_infos.meta,
            customer_agreements.meta,
            customer.meta,
            work_billing_infos.meta,
            meter_read_schedule.meta,
            erp_invoicees.meta,
            account_notification.meta,
        ),
    )

    def __init__(
        self,
        *,
        billing_cycle: str | None = None,
        budget_bill: str | None = None,
        last_bill_amount: _decimal.Decimal | None = None,
        payment_transactions: Iterable[Transaction] | None = None,
        customer_billing_infos: Iterable[CustomerBillingInfo] | None = None,
        customer_agreements: Iterable[CustomerAgreement] | None = None,
        customer: Customer | None = None,
        work_billing_infos: Iterable[WorkBillingInfo] | None = None,
        meter_read_schedule: MeterReadSchedule | None = None,
        erp_invoicees: Iterable[ErpInvoice] | None = None,
        account_notification: Iterable[AccountNotification] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.billing_cycle = billing_cycle
        self.budget_bill = budget_bill
        self.last_bill_amount = last_bill_amount
        if payment_transactions is not None:
            CustomerAccount.payment_transactions.extend(self, payment_transactions)
        if customer_billing_infos is not None:
            CustomerAccount.customer_billing_infos.extend(self, customer_billing_infos)
        if customer_agreements is not None:
            CustomerAccount.customer_agreements.extend(self, customer_agreements)
        if customer is not None:
            self.customer = customer
        if work_billing_infos is not None:
            CustomerAccount.work_billing_infos.extend(self, work_billing_infos)
        if meter_read_schedule is not None:
            self.meter_read_schedule = meter_read_schedule
        if erp_invoicees is not None:
            CustomerAccount.erp_invoicees.extend(self, erp_invoicees)
        if account_notification is not None:
            CustomerAccount.account_notification.extend(self, account_notification)

    def add_payment_transaction(self, payment_transaction: Transaction) -> Self:
        return CustomerAccount.payment_transactions.add(self, payment_transaction)

    def remove_payment_transaction(self, payment_transaction: Transaction) -> Self:
        return CustomerAccount.payment_transactions.remove(self, payment_transaction)

    def clear_payment_transactions(self) -> Self:
        return CustomerAccount.payment_transactions.clear(self)

    def num_payment_transaction(self) -> int:
        return CustomerAccount.payment_transactions.count(self)

    def get_payment_transaction_by_mrid(self, mrid: str) -> Transaction | None:
        return CustomerAccount.payment_transactions.get_by_mrid(self, mrid)

    def add_customer_billing_info(self, customer_billing_info: CustomerBillingInfo) -> Self:
        return CustomerAccount.customer_billing_infos.add(self, customer_billing_info)

    def remove_customer_billing_info(self, customer_billing_info: CustomerBillingInfo) -> Self:
        return CustomerAccount.customer_billing_infos.remove(self, customer_billing_info)

    def clear_customer_billing_infos(self) -> Self:
        return CustomerAccount.customer_billing_infos.clear(self)

    def num_customer_billing_info(self) -> int:
        return CustomerAccount.customer_billing_infos.count(self)

    def get_customer_billing_info_by_mrid(self, mrid: str) -> CustomerBillingInfo | None:
        return CustomerAccount.customer_billing_infos.get_by_mrid(self, mrid)

    def add_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return CustomerAccount.customer_agreements.add(self, customer_agreement)

    def remove_customer_agreement(self, customer_agreement: CustomerAgreement) -> Self:
        return CustomerAccount.customer_agreements.remove(self, customer_agreement)

    def clear_customer_agreements(self) -> Self:
        return CustomerAccount.customer_agreements.clear(self)

    def num_customer_agreement(self) -> int:
        return CustomerAccount.customer_agreements.count(self)

    def get_customer_agreement_by_mrid(self, mrid: str) -> CustomerAgreement | None:
        return CustomerAccount.customer_agreements.get_by_mrid(self, mrid)

    def add_work_billing_info(self, work_billing_info: WorkBillingInfo) -> Self:
        return CustomerAccount.work_billing_infos.add(self, work_billing_info)

    def remove_work_billing_info(self, work_billing_info: WorkBillingInfo) -> Self:
        return CustomerAccount.work_billing_infos.remove(self, work_billing_info)

    def clear_work_billing_infos(self) -> Self:
        return CustomerAccount.work_billing_infos.clear(self)

    def num_work_billing_info(self) -> int:
        return CustomerAccount.work_billing_infos.count(self)

    def get_work_billing_info_by_mrid(self, mrid: str) -> WorkBillingInfo | None:
        return CustomerAccount.work_billing_infos.get_by_mrid(self, mrid)

    def add_erp_invoicee(self, erp_invoicee: ErpInvoice) -> Self:
        return CustomerAccount.erp_invoicees.add(self, erp_invoicee)

    def remove_erp_invoicee(self, erp_invoicee: ErpInvoice) -> Self:
        return CustomerAccount.erp_invoicees.remove(self, erp_invoicee)

    def clear_erp_invoicees(self) -> Self:
        return CustomerAccount.erp_invoicees.clear(self)

    def num_erp_invoicee(self) -> int:
        return CustomerAccount.erp_invoicees.count(self)

    def get_erp_invoicee_by_mrid(self, mrid: str) -> ErpInvoice | None:
        return CustomerAccount.erp_invoicees.get_by_mrid(self, mrid)

    def add_account_notification(self, account_notification: AccountNotification) -> Self:
        return CustomerAccount.account_notification.add(self, account_notification)

    def remove_account_notification(self, account_notification: AccountNotification) -> Self:
        return CustomerAccount.account_notification.remove(self, account_notification)

    def clear_account_notification(self) -> Self:
        return CustomerAccount.account_notification.clear(self)

    def num_account_notification(self) -> int:
        return CustomerAccount.account_notification.count(self)

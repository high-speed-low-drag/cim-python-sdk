"""CIM class BankAccount (TC57CIM/IEC61968/InfIEC61968/InfCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.bank import Bank
    from cim_python_sdk.model.iec61968.payment_metering.service_supplier import ServiceSupplier


class BankAccount(Document):
    """Bank account."""

    __slots__ = ("_bank", "_service_supplier", "account_number")

    account_number: str | None

    bank: One[Bank] = One(
        EndMeta(
            name="bank",
            cim_role="Bank",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.bank:Bank",
            many=False,
            lower=0,
            upper=1,
            inverse="bank_accounts",
            aggregation="none",
        )
    )
    service_supplier: One[ServiceSupplier] = One(
        EndMeta(
            name="service_supplier",
            cim_role="ServiceSupplier",
            target="cim_python_sdk.model.iec61968.payment_metering.service_supplier:ServiceSupplier",
            many=False,
            lower=0,
            upper=1,
            inverse="bank_accounts",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="BankAccount",
        package="TC57CIM/IEC61968/InfIEC61968/InfCommon",
        guid="{AF7F22F5-7DB8-42b2-8676-0F9B9F9E9C05}",
        attributes=(AttrMeta("account_number", "accountNumber", "str", 0, 1, "primitive"),),
        ends=(
            bank.meta,
            service_supplier.meta,
        ),
    )

    def __init__(
        self,
        *,
        account_number: str | None = None,
        bank: Bank | None = None,
        service_supplier: ServiceSupplier | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.account_number = account_number
        if bank is not None:
            self.bank = bank
        if service_supplier is not None:
            self.service_supplier = service_supplier

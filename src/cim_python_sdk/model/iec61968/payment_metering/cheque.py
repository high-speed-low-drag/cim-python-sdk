"""CIM class Cheque (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.payment_metering.bank_account_detail import BankAccountDetail
    from cim_python_sdk.model.iec61968.payment_metering.cheque_kind import ChequeKind
    from cim_python_sdk.model.iec61968.payment_metering.tender import Tender


class Cheque(CimObject):
    """The actual tender when it is a type of cheque."""

    __slots__ = ("_tender", "bank_account_detail", "cheque_number", "date", "kind", "micr_number")

    kind: ChequeKind | None
    date: _dt.date | None
    micr_number: str | None
    cheque_number: str | None
    bank_account_detail: BankAccountDetail | None

    tender: One[Tender] = One(
        EndMeta(
            name="tender",
            cim_role="Tender",
            target="cim_python_sdk.model.iec61968.payment_metering.tender:Tender",
            many=False,
            lower=1,
            upper=1,
            inverse="cheque",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Cheque",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{DA6DAAA3-BB3B-40e1-B6B2-9FF3523D01A5}",
        attributes=(
            AttrMeta("kind", "kind", "ChequeKind", 0, 1, "enumeration"),
            AttrMeta("date", "date", "date", 0, 1, "primitive"),
            AttrMeta("micr_number", "micrNumber", "str", 0, 1, "primitive"),
            AttrMeta("cheque_number", "chequeNumber", "str", 0, 1, "primitive"),
            AttrMeta(
                "bank_account_detail", "bankAccountDetail", "BankAccountDetail", 0, 1, "compound"
            ),
        ),
        ends=(tender.meta,),
    )

    def __init__(
        self,
        *,
        kind: ChequeKind | None = None,
        date: _dt.date | None = None,
        micr_number: str | None = None,
        cheque_number: str | None = None,
        bank_account_detail: BankAccountDetail | None = None,
        tender: Tender | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.date = date
        self.micr_number = micr_number
        self.cheque_number = cheque_number
        self.bank_account_detail = bank_account_detail
        if tender is not None:
            self.tender = tender

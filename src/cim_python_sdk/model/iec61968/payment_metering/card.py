"""CIM class Card (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.payment_metering.tender import Tender


class Card(CimObject):
    """Documentation of the tender when it is a type of card (credit, debit, etc)."""

    __slots__ = ("_tender", "account_holder_name", "cv_number", "expiry_date", "pan")

    cv_number: str | None
    expiry_date: _dt.date | None
    pan: str | None
    account_holder_name: str | None

    tender: One[Tender] = One(
        EndMeta(
            name="tender",
            cim_role="Tender",
            target="cim_python_sdk.model.iec61968.payment_metering.tender:Tender",
            many=False,
            lower=1,
            upper=1,
            inverse="card",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Card",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{1AD7DFBB-5985-4510-9DDA-B0F019A8C24F}",
        attributes=(
            AttrMeta("cv_number", "cvNumber", "str", 0, 1, "primitive"),
            AttrMeta("expiry_date", "expiryDate", "date", 0, 1, "primitive"),
            AttrMeta("pan", "pan", "str", 0, 1, "primitive"),
            AttrMeta("account_holder_name", "accountHolderName", "str", 0, 1, "primitive"),
        ),
        ends=(tender.meta,),
    )

    def __init__(
        self,
        *,
        cv_number: str | None = None,
        expiry_date: _dt.date | None = None,
        pan: str | None = None,
        account_holder_name: str | None = None,
        tender: Tender | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cv_number = cv_number
        self.expiry_date = expiry_date
        self.pan = pan
        self.account_holder_name = account_holder_name
        if tender is not None:
            self.tender = tender

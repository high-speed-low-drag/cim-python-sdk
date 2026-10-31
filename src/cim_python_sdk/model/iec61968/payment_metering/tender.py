"""CIM class Tender (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from typing import Any

    from cim_python_sdk.model.iec61968.payment_metering.card import Card
    from cim_python_sdk.model.iec61968.payment_metering.cheque import Cheque
    from cim_python_sdk.model.iec61968.payment_metering.receipt import Receipt
    from cim_python_sdk.model.iec61968.payment_metering.tender_kind import TenderKind


class Tender(IdentifiedObject):
    """Tender is what is "offered" by the customer towards making a payment and is often more
    than the required payment (hence the need for 'change'). The payment is thus that part
    of the Tender that goes towards settlement of a particular transaction.

    Tender is modelled as an aggregation of Cheque and Card. Both these tender types can
    exist in a single tender bid thus 'accountHolderName' has to exist separately in each of
    Cheque and Card as each could have a different account holder name."""

    __slots__ = ("_card", "_cheque", "_receipt", "amount", "change", "kind")

    kind: TenderKind | None
    amount: _decimal.Decimal | None  # Money
    change: _decimal.Decimal | None  # Money

    card: One[Card] = One(
        EndMeta(
            name="card",
            cim_role="Card",
            target="cim_python_sdk.model.iec61968.payment_metering.card:Card",
            many=False,
            lower=0,
            upper=1,
            inverse="tender",
            aggregation="none",
        )
    )
    receipt: One[Receipt] = One(
        EndMeta(
            name="receipt",
            cim_role="Receipt",
            target="cim_python_sdk.model.iec61968.payment_metering.receipt:Receipt",
            many=False,
            lower=1,
            upper=1,
            inverse="tenders",
            aggregation="none",
        )
    )
    cheque: One[Cheque] = One(
        EndMeta(
            name="cheque",
            cim_role="Cheque",
            target="cim_python_sdk.model.iec61968.payment_metering.cheque:Cheque",
            many=False,
            lower=0,
            upper=1,
            inverse="tender",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Tender",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{3937B337-1AFD-4c5b-832F-0C13C893EE41}",
        attributes=(
            AttrMeta("kind", "kind", "TenderKind", 0, 1, "enumeration"),
            AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("change", "change", "Money", 0, 1, "cimdatatype"),
        ),
        ends=(
            card.meta,
            receipt.meta,
            cheque.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: TenderKind | None = None,
        amount: _decimal.Decimal | None = None,
        change: _decimal.Decimal | None = None,
        card: Card | None = None,
        receipt: Receipt | None = None,
        cheque: Cheque | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.amount = amount
        self.change = change
        if card is not None:
            self.card = card
        if receipt is not None:
            self.receipt = receipt
        if cheque is not None:
            self.cheque = cheque

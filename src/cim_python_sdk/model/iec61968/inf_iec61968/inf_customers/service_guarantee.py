"""CIM class ServiceGuarantee (TC57CIM/IEC61968/InfIEC61968/InfCustomers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from typing import Any

    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval


class ServiceGuarantee(Document):
    """A service guarantee, often imposed by a regulator, defines conditions that, if not
    satisfied, will result in the utility making a monetary payment to the customer. Note
    that guarantee's identifier is in the 'name' attribute and the status of the guarantee
    is in the 'Status.status' attribute.

    Example service requirements include:

    1) If power is not restored within 24 hours, customers can claim $50 for residential
    customers or $100 for commercial and industrial customers. In addition for each extra
    period of 12 hours the customer's supply has not been activated, the customer can claim
    $25.

    2) If a customer has a question about their electricity bill, the utility will
    investigate and respond to the inquiry within 15 working days. If utility fails to meet
    its guarantee, utility will automatically pay the customer $50."""

    __slots__ = ("application_period", "automatic_pay", "pay_amount", "service_requirement")

    service_requirement: str | None
    pay_amount: _decimal.Decimal | None  # Money
    automatic_pay: bool | None
    application_period: DateTimeInterval | None

    _cim_meta = ClassMeta(
        cim_name="ServiceGuarantee",
        package="TC57CIM/IEC61968/InfIEC61968/InfCustomers",
        guid="{21F81CF0-10CF-4a60-94FC-CEB045927D7E}",
        attributes=(
            AttrMeta("service_requirement", "serviceRequirement", "str", 0, 1, "primitive"),
            AttrMeta("pay_amount", "payAmount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("automatic_pay", "automaticPay", "bool", 0, 1, "primitive"),
            AttrMeta(
                "application_period", "applicationPeriod", "DateTimeInterval", 0, 1, "compound"
            ),
        ),
    )

    def __init__(
        self,
        *,
        service_requirement: str | None = None,
        pay_amount: _decimal.Decimal | None = None,
        automatic_pay: bool | None = None,
        application_period: DateTimeInterval | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.service_requirement = service_requirement
        self.pay_amount = pay_amount
        self.automatic_pay = automatic_pay
        self.application_period = application_period

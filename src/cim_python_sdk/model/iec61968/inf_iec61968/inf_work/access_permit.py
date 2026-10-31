"""CIM class AccessPermit (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal
    from typing import Any


class AccessPermit(WorkDocument):
    """A permit is sometimes needed to provide legal access to land or equipment. For example,
    local authority permission for road works."""

    __slots__ = ("application_number", "effective_date", "expiration_date", "payment", "permit_id")

    permit_id: str | None
    application_number: str | None
    effective_date: _dt.date | None
    expiration_date: _dt.date | None
    payment: _decimal.Decimal | None  # Money

    _cim_meta = ClassMeta(
        cim_name="AccessPermit",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{2EF3EB23-CD98-4c1f-9666-C99E392E8140}",
        attributes=(
            AttrMeta("permit_id", "permitID", "str", 0, 1, "primitive"),
            AttrMeta("application_number", "applicationNumber", "str", 0, 1, "primitive"),
            AttrMeta("effective_date", "effectiveDate", "date", 0, 1, "primitive"),
            AttrMeta("expiration_date", "expirationDate", "date", 0, 1, "primitive"),
            AttrMeta("payment", "payment", "Money", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        permit_id: str | None = None,
        application_number: str | None = None,
        effective_date: _dt.date | None = None,
        expiration_date: _dt.date | None = None,
        payment: _decimal.Decimal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.permit_id = permit_id
        self.application_number = application_number
        self.effective_date = effective_date
        self.expiration_date = expiration_date
        self.payment = payment

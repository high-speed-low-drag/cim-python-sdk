"""CIM compound AccountMovement (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal


class AccountMovement(CimCompound):
    """Credit/debit movements for an account."""

    __slots__ = ("amount", "date_time", "reason")

    amount: _decimal.Decimal | None  # Money
    reason: str | None
    date_time: _dt.datetime | None

    _cim_meta = ClassMeta(
        cim_name="AccountMovement",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{7E314D6D-4B83-48e8-86C9-CCE6BCAB6BFE}",
        kind="compound",
        attributes=(
            AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("reason", "reason", "str", 0, 1, "primitive"),
            AttrMeta("date_time", "dateTime", "datetime", 0, 1, "primitive"),
        ),
    )

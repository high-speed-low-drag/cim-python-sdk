"""CIM compound LineDetail (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    import decimal as _decimal


class LineDetail(CimCompound):
    """Details on an amount line, with rounding, date and note."""

    __slots__ = ("amount", "date_time", "note", "rounding")

    amount: _decimal.Decimal | None  # Money
    rounding: _decimal.Decimal | None  # Money
    date_time: _dt.datetime | None
    note: str | None

    _cim_meta = ClassMeta(
        cim_name="LineDetail",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{5BE14CC8-F5D1-4677-8239-955933CCC630}",
        kind="compound",
        attributes=(
            AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),
            AttrMeta("rounding", "rounding", "Money", 0, 1, "cimdatatype"),
            AttrMeta("date_time", "dateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("note", "note", "str", 0, 1, "primitive"),
        ),
    )

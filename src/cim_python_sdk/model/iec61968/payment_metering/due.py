"""CIM compound Due (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal


class Due(CimCompound):
    """Details on amounts due for an account."""

    __slots__ = ("arrears", "charges", "current", "interest", "principle")

    current: _decimal.Decimal | None  # Money
    principle: _decimal.Decimal | None  # Money
    arrears: _decimal.Decimal | None  # Money
    interest: _decimal.Decimal | None  # Money
    charges: _decimal.Decimal | None  # Money

    _cim_meta = ClassMeta(
        cim_name="Due",
        package="TC57CIM/IEC61968/PaymentMetering",
        guid="{33ADB344-ACC2-443a-AE02-258AD2AA6C72}",
        kind="compound",
        attributes=(
            AttrMeta("current", "current", "Money", 0, 1, "cimdatatype"),
            AttrMeta("principle", "principle", "Money", 0, 1, "cimdatatype"),
            AttrMeta("arrears", "arrears", "Money", 0, 1, "cimdatatype"),
            AttrMeta("interest", "interest", "Money", 0, 1, "cimdatatype"),
            AttrMeta("charges", "charges", "Money", 0, 1, "cimdatatype"),
        ),
    )

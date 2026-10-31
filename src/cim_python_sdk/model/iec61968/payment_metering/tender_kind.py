"""CIM enumeration TenderKind (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TenderKind(CimEnum):
    """Kind of tender."""

    cheque = "cheque"
    card = "card"
    cash = "cash"
    unspecified = "unspecified"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TenderKind",
            package="TC57CIM/IEC61968/PaymentMetering",
            guid="{E0FD3999-B4C6-4dd3-AB75-9A2CD71DE95C}",
            kind="enumeration",
        )
    )

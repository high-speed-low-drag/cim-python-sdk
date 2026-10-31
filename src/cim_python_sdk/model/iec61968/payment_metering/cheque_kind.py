"""CIM enumeration ChequeKind (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ChequeKind(CimEnum):
    """Kind of cheque."""

    postalOrder = "postalOrder"
    bankOrder = "bankOrder"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ChequeKind",
            package="TC57CIM/IEC61968/PaymentMetering",
            guid="{7EA8BC38-802A-4015-AB68-17869B5D1ACB}",
            kind="enumeration",
        )
    )

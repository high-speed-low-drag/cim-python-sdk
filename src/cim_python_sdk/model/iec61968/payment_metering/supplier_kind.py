"""CIM enumeration SupplierKind (TC57CIM/IEC61968/PaymentMetering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SupplierKind(CimEnum):
    """Kind of supplier."""

    utility = "utility"
    retailer = "retailer"
    lse = "lse"
    mdma = "mdma"
    msp = "msp"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SupplierKind",
            package="TC57CIM/IEC61968/PaymentMetering",
            guid="{03BF74FB-B448-4112-8394-9E1EC7D2BAA7}",
            kind="enumeration",
        )
    )

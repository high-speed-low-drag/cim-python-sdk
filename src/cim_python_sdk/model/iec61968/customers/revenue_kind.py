"""CIM enumeration RevenueKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RevenueKind(CimEnum):
    """Accounting classification of the type of revenue collected for the customer agreement,
    typically used to break down accounts for revenue accounting."""

    residential = "residential"
    nonResidential = "nonResidential"
    commercial = "commercial"
    industrial = "industrial"
    irrigation = "irrigation"
    streetLight = "streetLight"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RevenueKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{FE40851C-B2FA-41ae-AE39-30A6E441A293}",
            kind="enumeration",
        )
    )

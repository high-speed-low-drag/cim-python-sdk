"""CIM enumeration MktInvoiceLineItemKind (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MktInvoiceLineItemKind(CimEnum):
    """Kind of invoice line item."""

    initial = "initial"
    recalculation = "recalculation"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MktInvoiceLineItemKind",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{30CBD890-6578-48b4-BA4E-4C563A77103A}",
            kind="enumeration",
        )
    )

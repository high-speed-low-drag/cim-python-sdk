"""CIM enumeration ErpInvoiceLineItemKind (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ErpInvoiceLineItemKind(CimEnum):
    """Kind of invoice line item."""

    initial = "initial"
    recalculation = "recalculation"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ErpInvoiceLineItemKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
            guid="{F22B0623-851B-43f7-A35C-F4771F4813F9}",
            kind="enumeration",
        )
    )

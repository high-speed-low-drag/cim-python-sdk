"""CIM enumeration ErpInvoiceKind (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ErpInvoiceKind(CimEnum):
    """Kind of ERP invoice."""

    sale = "sale"
    purchase = "purchase"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ErpInvoiceKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
            guid="{613C1258-4E8D-4c2c-A23A-AC9C0D812876}",
            kind="enumeration",
        )
    )

"""CIM enumeration ErpAccountKind (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ErpAccountKind(CimEnum):
    """Kind of ERP account."""

    normal = "normal"
    reversal = "reversal"
    statistical = "statistical"
    estimate = "estimate"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ErpAccountKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
            guid="{AE794AC8-10DB-40b8-BDBF-F5B708D9AD33}",
            kind="enumeration",
        )
    )

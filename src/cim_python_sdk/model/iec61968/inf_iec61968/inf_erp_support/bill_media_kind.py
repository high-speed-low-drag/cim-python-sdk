"""CIM enumeration BillMediaKind (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BillMediaKind(CimEnum):
    """Kind of bill media."""

    paper = "paper"
    electronic = "electronic"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BillMediaKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
            guid="{F3D3FF79-2E14-4bc1-989F-2F0471139227}",
            kind="enumeration",
        )
    )

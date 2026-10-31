"""CIM enumeration TroubleReportingKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TroubleReportingKind(CimEnum):
    """Kind of trouble reporting."""

    call = "call"
    email = "email"
    letter = "letter"
    other = "other"
    ivr = "ivr"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TroubleReportingKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{69FC5C51-2840-4e50-A456-690D9026C079}",
            kind="enumeration",
        )
    )

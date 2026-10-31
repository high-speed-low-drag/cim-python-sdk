"""CIM enumeration TroubleReportingKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TroubleReportingKind_2(CimEnum):
    """Kind of trouble reporting."""

    call = "call"
    email = "email"
    letter = "letter"
    other = "other"
    ivr = "ivr"
    app = "app"
    sms = "sms"
    web = "web"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TroubleReportingKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{CBCADF0E-A59B-4a75-B085-16E23F8D0229}",
            kind="enumeration",
        )
    )

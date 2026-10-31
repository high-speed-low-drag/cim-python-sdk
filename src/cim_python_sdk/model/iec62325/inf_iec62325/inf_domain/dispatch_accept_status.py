"""CIM enumeration DispatchAcceptStatus (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DispatchAcceptStatus(CimEnum):
    """CIM enumeration DispatchAcceptStatus."""

    NON_RESPONSE = "NON_RESPONSE"
    OK = "OK"
    CANNOT = "CANNOT"
    ACCEPT = "ACCEPT"
    DECLINE = "DECLINE"
    PARTIAL = "PARTIAL"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DispatchAcceptStatus",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{C7810608-5927-439f-822F-A028FC453FB5}",
            kind="enumeration",
        )
    )

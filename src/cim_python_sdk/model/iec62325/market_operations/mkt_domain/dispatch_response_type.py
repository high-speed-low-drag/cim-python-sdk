"""CIM enumeration DispatchResponseType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DispatchResponseType(CimEnum):
    """For example:

    NON_RESPONSE

    ACCEPT

    DECLINE

    PARTIAL"""

    NON_RESPONSE = "NON_RESPONSE"
    ACCEPT = "ACCEPT"
    DECLINE = "DECLINE"
    PARTIAL = "PARTIAL"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DispatchResponseType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{CD7CD960-8FA3-4c76-88A9-2C51DC013799}",
            kind="enumeration",
        )
    )

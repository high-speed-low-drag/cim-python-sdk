"""CIM enumeration BidStatusType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BidStatusType(CimEnum):
    """Status indication for bids

    CV - Conditionally Valid Bid

    CM - Conditionally Modified Bid

    V - Valid Bid

    M - Modified Bid

    RJ - Rejected Bid

    I - Invalid Bid

    CX - Cancelled Bid

    O - Obsolete Bid

    CL - Clean Bid

    RP - Replicated Bid"""

    CL = "CL"
    RP = "RP"
    RJ = "RJ"
    I = "I"
    CV = "CV"
    CM = "CM"
    V = "V"
    M = "M"
    CX = "CX"
    O = "O"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BidStatusType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{899191A0-41EC-4106-9EDF-0A97D7509159}",
            kind="enumeration",
        )
    )

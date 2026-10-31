"""CIM enumeration TradeStatusType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TradeStatusType(CimEnum):
    """RJ - Rejected Trade

    I - Invalid Trade

    V - Valid Trade

    M - Modified Trade

    CV - Conditionally Valid Trade

    CM - Conditionally Modified Trade

    CI - Conditionally Invalid Trade

    CX - Cancelled Trade

    O - Obsolete Trade

    MT - Matched Trade

    U - Unmatched Trade"""

    RJ = "RJ"
    I = "I"
    V = "V"
    M = "M"
    CV = "CV"
    CM = "CM"
    CI = "CI"
    CX = "CX"
    O = "O"
    MT = "MT"
    U = "U"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TradeStatusType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{3184AF14-7AE7-44dd-A246-B1F365768661}",
            kind="enumeration",
        )
    )

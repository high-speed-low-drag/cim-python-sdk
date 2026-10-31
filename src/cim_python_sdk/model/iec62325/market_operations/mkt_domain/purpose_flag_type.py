"""CIM enumeration PurposeFlagType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PurposeFlagType(CimEnum):
    """MPM Purpose Flag, for example:

    Nature of threshold data:

    'M' - Mitigation threshold

    'R' - Reporting threshold"""

    M = "M"
    R = "R"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PurposeFlagType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{46820D5A-7D62-4874-9C53-818A6A3AC0D0}",
            kind="enumeration",
        )
    )

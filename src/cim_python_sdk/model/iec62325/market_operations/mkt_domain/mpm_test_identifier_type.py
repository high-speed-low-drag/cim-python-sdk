"""CIM enumeration MPMTestIdentifierType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MPMTestIdentifierType(CimEnum):
    """Market power mitigation test identifier type, for example:

    1 - Global Price Test

    2 - Global Conduct Test

    3 - Global Impact Test

    4 - Local Price Test

    5 - Local Conduct Test

    6 - Local Impact Test"""

    v1 = "1"
    v2 = "2"
    v3 = "3"
    v4 = "4"
    v5 = "5"
    v6 = "6"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MPMTestIdentifierType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{B4D946D6-6691-43e0-AEEB-7CEFBA38B30E}",
            kind="enumeration",
        )
    )

"""CIM enumeration TRType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TRType(CimEnum):
    """Transmission Contract Right type -for example:

    individual or chain of contract rights"""

    CHAIN = "CHAIN"
    INDIVIDUAL = "INDIVIDUAL"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TRType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{F787B721-AD7D-49a0-8C10-2A3720CC437A}",
            kind="enumeration",
        )
    )

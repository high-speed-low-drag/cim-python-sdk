"""CIM enumeration InterTieDirection (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class InterTieDirection(CimEnum):
    """Direction of an intertie."""

    E = "E"
    I = "I"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="InterTieDirection",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{B0936608-F625-4f4d-962D-43AE70AA685C}",
            kind="enumeration",
        )
    )

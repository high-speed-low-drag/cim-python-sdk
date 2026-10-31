"""CIM enumeration BidType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BidType(CimEnum):
    """For example:

    DEFAULT_ENERGY_BID

    DEFAULT_STARTUP_BID

    DEFAULT_MINIMUM_LOAD_BID"""

    DEFAULT_ENERGY_BID = "DEFAULT_ENERGY_BID"
    DEFAULT_STARTUP_BID = "DEFAULT_STARTUP_BID"
    DEFAULT_MINIMUM_LOAD_BID = "DEFAULT_MINIMUM_LOAD_BID"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BidType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{75B5BC02-B0BB-4fc3-8502-EAC3A27977C7}",
            kind="enumeration",
        )
    )

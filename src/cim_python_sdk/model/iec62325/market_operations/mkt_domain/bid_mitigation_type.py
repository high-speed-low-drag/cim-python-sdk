"""CIM enumeration BidMitigationType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BidMitigationType(CimEnum):
    """For example:

    Initial

    Final"""

    I = "I"
    F = "F"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BidMitigationType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{D6924D44-26E3-4a20-938D-DFEF4D64E6C4}",
            kind="enumeration",
        )
    )

"""CIM enumeration CommitmentType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CommitmentType(CimEnum):
    """For example:

    SELF - Self commitment

    ISO - New commitment for this market period

    UC - Existing commitment that was a hold over from a previous market"""

    SELF = "SELF"
    ISO = "ISO"
    UC = "UC"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CommitmentType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{27ACD4AD-8EB7-4ce3-9632-9659A310A907}",
            kind="enumeration",
        )
    )

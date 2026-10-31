"""CIM enumeration CRRRoleType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CRRRoleType(CimEnum):
    """Role types an organisation can play with respect to a congestion revenue right."""

    SELLER = "SELLER"
    BUYER = "BUYER"
    OWNER = "OWNER"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CRRRoleType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{AFECA684-2442-4d80-B528-D26ABA629D5D}",
            kind="enumeration",
        )
    )

"""CIM enumeration CostBasis (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CostBasis(CimEnum):
    """For example:

    Bid Cost

    Proxy Cost

    Registered Cost"""

    BIDC = "BIDC"
    PRXC = "PRXC"
    REGC = "REGC"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CostBasis",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{43DD0511-E369-4fb5-A330-FCB1FA53C08F}",
            kind="enumeration",
        )
    )

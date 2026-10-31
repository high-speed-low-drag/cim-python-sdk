"""CIM enumeration EnergyPriceIndexType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EnergyPriceIndexType(CimEnum):
    """For example:

    WHOLESALE

    RETAIL

    BOTH"""

    WHOLESALE = "WHOLESALE"
    RETAIL = "RETAIL"
    BOTH = "BOTH"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EnergyPriceIndexType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{BC4A9076-4E86-4c95-A64D-D2981C6E1DED}",
            kind="enumeration",
        )
    )

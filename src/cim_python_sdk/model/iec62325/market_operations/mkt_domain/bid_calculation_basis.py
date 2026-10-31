"""CIM enumeration BidCalculationBasis (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BidCalculationBasis(CimEnum):
    """The basis used to calculate the bid price curve for an energy default bid."""

    LMP_BASED = "LMP_BASED"
    COST_BASED = "COST_BASED"
    NEGOTIATED = "NEGOTIATED"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BidCalculationBasis",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{1F88ACBA-D9D3-4060-8FE6-69ED252CE0EF}",
            kind="enumeration",
        )
    )

"""CIM enumeration RampRateType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RampRateType(CimEnum):
    """Ramp rate curve type."""

    OP = "OP"
    REG = "REG"
    OP_RES = "OP_RES"
    LD_DROP = "LD_DROP"
    LD_PICKUP = "LD_PICKUP"
    INTERTIE = "INTERTIE"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RampRateType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{45A50DBB-81E1-4287-B563-BD58851D11BB}",
            kind="enumeration",
        )
    )

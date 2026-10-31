"""CIM enumeration RampRateCondition (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RampRateCondition(CimEnum):
    """Ramp rate condition."""

    WORST = "WORST"
    BEST = "BEST"
    NORMAL = "NORMAL"
    NA = "NA"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RampRateCondition",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{FF13A48D-7F4C-4c39-BE56-FAB8AFE530A3}",
            kind="enumeration",
        )
    )

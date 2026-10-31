"""CIM enumeration PassIndicatorType (TC57CIM/IEC62325/MarketOperations/MktDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PassIndicatorType(CimEnum):
    """Defines the individual passes that produce results per execution type/market type."""

    MPM_1 = "MPM-1"
    MPM_2 = "MPM-2"
    MPM_3 = "MPM-3"
    MPM_4 = "MPM-4"
    RUC = "RUC"
    RTPD = "RTPD"
    RTED = "RTED"
    HA_SCUC = "HA-SCUC"
    DA = "DA"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PassIndicatorType",
            package="TC57CIM/IEC62325/MarketOperations/MktDomain",
            guid="{48EA8E65-07ED-4bb2-BD0F-5A8B9AADD331}",
            kind="enumeration",
        )
    )

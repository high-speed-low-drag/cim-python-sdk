"""CIM enumeration MarketScheduleServices (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MarketScheduleServices(CimEnum):
    """CIM enumeration MarketScheduleServices."""

    retrieveDefaultBidCurves = "retrieveDefaultBidCurves"
    retrieveMarketAwards = "retrieveMarketAwards"
    retrieveMPMResults = "retrieveMPMResults"
    retrieveSchedulePrices = "retrieveSchedulePrices"
    retrieveStartUpShutDownInstructions = "retrieveStartUpShutDownInstructions"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MarketScheduleServices",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{7BFB094E-5E4C-4b25-ADBE-94BF15F4A323}",
            kind="enumeration",
        )
    )

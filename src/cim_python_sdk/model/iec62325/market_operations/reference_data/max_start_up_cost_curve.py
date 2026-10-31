"""CIM class MaxStartUpCostCurve (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.base.core.curve import Curve


class MaxStartUpCostCurve(Curve):
    """The maximum Startup costs and time as a function of down time. Relationship between unit
    startup cost (Y1-axis) vs. unit elapsed down time (X-axis). This is used to validate the
    information provided in the Bid."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="MaxStartUpCostCurve",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{ECBD3F6B-2F34-4850-9BD0-146A8827E42F}",
    )

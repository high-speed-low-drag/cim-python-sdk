"""CIM enumeration MacroPeriodKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MacroPeriodKind(CimEnum):
    """Kind of macro period for calculations on read / measured values."""

    none = "none"
    billingPeriod = "billingPeriod"
    daily = "daily"
    monthly = "monthly"
    seasonal = "seasonal"
    weekly = "weekly"
    specifiedPeriod = "specifiedPeriod"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MacroPeriodKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{244D847D-1CAB-4bbe-9F4A-A63C52FE273D}",
            kind="enumeration",
        )
    )

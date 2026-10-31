"""CIM enumeration ProtectiveActionAdjustmentKind (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ProtectiveActionAdjustmentKind(CimEnum):
    """Categorisation of different protective action adjustments that can be performed on
    equipment."""

    byPercentage = "byPercentage"
    byValue = "byValue"
    setValue = "setValue"
    measurement = "measurement"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ProtectiveActionAdjustmentKind",
            package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
            guid="{D8125BC3-EC60-4d67-B5C3-5A579997BDC4}",
            kind="enumeration",
        )
    )

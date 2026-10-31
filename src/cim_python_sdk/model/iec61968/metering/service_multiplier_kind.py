"""CIM enumeration ServiceMultiplierKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ServiceMultiplierKind(CimEnum):
    """Kind of service multiplier."""

    ctRatio = "ctRatio"
    ptRatio = "ptRatio"
    transformerRatio = "transformerRatio"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ServiceMultiplierKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{621E7C20-0F73-4bf2-A294-9FCD3F4C6B93}",
            kind="enumeration",
        )
    )

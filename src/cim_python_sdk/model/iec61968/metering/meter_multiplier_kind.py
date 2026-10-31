"""CIM enumeration MeterMultiplierKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class MeterMultiplierKind(CimEnum):
    """Kind of meter multiplier."""

    kH = "kH"
    kR = "kR"
    kE = "kE"
    ctRatio = "ctRatio"
    ptRatio = "ptRatio"
    transformerRatio = "transformerRatio"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="MeterMultiplierKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{DE169701-1595-4706-BE8D-544BCD71F7C8}",
            kind="enumeration",
        )
    )

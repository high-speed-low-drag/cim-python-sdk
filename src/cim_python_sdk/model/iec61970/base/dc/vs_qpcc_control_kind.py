"""CIM enumeration VsQpccControlKind (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class VsQpccControlKind(CimEnum):
    """Kind of reactive power control at point of common coupling for a voltage source
    converter."""

    reactivePcc = "reactivePcc"
    voltagePcc = "voltagePcc"
    powerFactorPcc = "powerFactorPcc"
    pulseWidthModulation = "pulseWidthModulation"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="VsQpccControlKind",
            package="TC57CIM/IEC61970/Base/DC",
            guid="{082505D6-AAE1-42a4-9E62-70710BAF79D6}",
            kind="enumeration",
        )
    )

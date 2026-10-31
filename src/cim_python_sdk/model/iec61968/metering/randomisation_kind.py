"""CIM enumeration RandomisationKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RandomisationKind(CimEnum):
    """Kind of randomisation to be applied to control the timing of end device control commands
    and/or the definition of demand response and load control events. Value other than
    'none' is typically used to mitigate potential deleterious effects of simultaneous
    operation of multiple devices."""

    start = "start"
    end = "end"
    startAndEnd = "startAndEnd"
    default = "default"
    none = "none"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RandomisationKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{3A872CA2-ED74-4716-B472-08117E428527}",
            kind="enumeration",
        )
    )

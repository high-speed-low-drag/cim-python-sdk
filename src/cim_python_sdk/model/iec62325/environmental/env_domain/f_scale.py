"""CIM enumeration FScale (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class FScale(CimEnum):
    """Fujita scale (referred to as EF-scale starting in 2007) for tornado damage. A set of
    wind estimates (not measurements) based on damage. It uses three-second gusts estimated
    at the point of damage based on a judgment of 8 levels of damage to 28 indicators. These
    estimates vary with height and exposure.

    The 3 second gust is not the same wind as in standard surface observations.

    Enumerations based on NOAA conventions."""

    zero = "zero"
    one = "one"
    two = "two"
    three = "three"
    four = "four"
    five = "five"
    minusNine = "minusNine"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="FScale",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{399B2769-2649-4d03-81E7-9AB64348C110}",
            kind="enumeration",
        )
    )

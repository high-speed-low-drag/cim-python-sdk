"""CIM enumeration IntensityCodeKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class IntensityCodeKind(CimEnum):
    """Kinds of weather condition intensity."""

    heavy = "heavy"
    light = "light"
    veryHeavy = "veryHeavy"
    veryLight = "veryLight"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="IntensityCodeKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{F6A7E1AE-2170-4169-8D09-2417631E55D2}",
            kind="enumeration",
        )
    )

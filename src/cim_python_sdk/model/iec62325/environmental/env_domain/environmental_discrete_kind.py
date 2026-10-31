"""CIM enumeration EnvironmentalDiscreteKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class EnvironmentalDiscreteKind(CimEnum):
    """Discrete (integer) measuring an environmental condition."""

    cloudCover = "cloudCover"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="EnvironmentalDiscreteKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{6C16F9CE-689B-420d-91CE-DB256FBACF80}",
            kind="enumeration",
        )
    )

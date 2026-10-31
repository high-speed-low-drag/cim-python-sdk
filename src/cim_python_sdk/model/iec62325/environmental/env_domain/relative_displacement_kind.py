"""CIM enumeration RelativeDisplacementKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RelativeDisplacementKind(CimEnum):
    """The types of relative displacement"""

    seaLevel = "seaLevel"
    ground = "ground"
    centreEarth = "centreEarth"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RelativeDisplacementKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{D4F6C390-4C62-4e58-8230-E830916A4AE2}",
            kind="enumeration",
        )
    )

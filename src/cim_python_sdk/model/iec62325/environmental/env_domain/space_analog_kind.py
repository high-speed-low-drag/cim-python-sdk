"""CIM enumeration SpaceAnalogKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SpaceAnalogKind(CimEnum):
    """Kinds of analogs (floats) measuring a space condition."""

    magneticFieldDirection = "magneticFieldDirection"
    magneticFieldStrength = "magneticFieldStrength"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SpaceAnalogKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{B54762BE-B4CE-4841-A0E6-C2ED3C921661}",
            kind="enumeration",
        )
    )

"""CIM enumeration GeosphericAnalogKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class GeosphericAnalogKind(CimEnum):
    """Kinds of analogs (floats) measuring a geospheric condition."""

    lightningDensity = "lightningDensity"
    seismicEastWest = "seismicEastWest"
    seismicNorthSouth = "seismicNorthSouth"
    seismicVertical = "seismicVertical"
    snowPackDepth = "snowPackDepth"
    temperature = "temperature"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="GeosphericAnalogKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{A5FECA26-89F5-4c54-8C7E-70AB5982880D}",
            kind="enumeration",
        )
    )

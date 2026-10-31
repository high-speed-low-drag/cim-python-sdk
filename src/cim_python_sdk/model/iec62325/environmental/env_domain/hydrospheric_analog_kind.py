"""CIM enumeration HydrosphericAnalogKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class HydrosphericAnalogKind(CimEnum):
    """Kinds of analogs (floats) measuring a hydrospheric condition."""

    floodLevel = "floodLevel"
    stormSurgeHeight = "stormSurgeHeight"
    waveHeight = "waveHeight"
    surfaceTemperature = "surfaceTemperature"
    waterTemperature = "waterTemperature"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="HydrosphericAnalogKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{6D4D68B2-CD2F-4660-A5F2-EDA22D2F057E}",
            kind="enumeration",
        )
    )

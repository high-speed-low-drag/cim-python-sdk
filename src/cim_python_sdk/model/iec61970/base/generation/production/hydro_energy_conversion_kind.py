"""CIM enumeration HydroEnergyConversionKind (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class HydroEnergyConversionKind(CimEnum):
    """Specifies the capability of the hydro generating unit to convert energy as a generator
    or pump."""

    generator = "generator"
    pumpAndGenerator = "pumpAndGenerator"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="HydroEnergyConversionKind",
            package="TC57CIM/IEC61970/Base/Generation/Production",
            guid="{4CBE71BD-F7EC-4313-B5DF-F828931C7234}",
            kind="enumeration",
        )
    )

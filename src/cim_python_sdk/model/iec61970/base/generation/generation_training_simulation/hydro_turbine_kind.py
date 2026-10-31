"""CIM enumeration HydroTurbineKind (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class HydroTurbineKind(CimEnum):
    """Type of turbine."""

    francis = "francis"
    pelton = "pelton"
    kaplan = "kaplan"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="HydroTurbineKind",
            package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
            guid="{099C5D06-8AE4-4e91-85DF-6142C7DABBE2}",
            kind="enumeration",
        )
    )

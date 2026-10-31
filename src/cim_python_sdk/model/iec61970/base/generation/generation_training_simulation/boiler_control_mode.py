"""CIM enumeration BoilerControlMode (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BoilerControlMode(CimEnum):
    """Boiler control mode."""

    following = "following"
    coordinated = "coordinated"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BoilerControlMode",
            package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
            guid="{08E2F3C4-C40B-44d5-8D63-CF26F9E72DB8}",
            kind="enumeration",
        )
    )

"""CIM enumeration OperatingMechanismKind (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OperatingMechanismKind(CimEnum):
    """Kinds of operating mechanisms."""

    capacitorTrip = "capacitorTrip"
    hydraulic = "hydraulic"
    pneudraulic = "pneudraulic"
    pneumatic = "pneumatic"
    solenoid = "solenoid"
    spring = "spring"
    springHandCrank = "springHandCrank"
    springHydraulic = "springHydraulic"
    springMotor = "springMotor"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OperatingMechanismKind",
            package="TC57CIM/IEC61968/AssetInfo",
            guid="{2D0C0B24-30F4-4484-8774-E91D00289E08}",
            kind="enumeration",
        )
    )

"""CIM enumeration RotorKind (TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RotorKind(CimEnum):
    """Type of rotor on physical machine."""

    roundRotor = "roundRotor"
    salientPole = "salientPole"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RotorKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics",
            guid="{B784D340-A930-49c4-AF7C-23CB2D9C8E4D}",
            kind="enumeration",
        )
    )

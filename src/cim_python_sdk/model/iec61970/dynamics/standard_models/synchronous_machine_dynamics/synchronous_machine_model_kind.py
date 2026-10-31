"""CIM enumeration SynchronousMachineModelKind (TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SynchronousMachineModelKind(CimEnum):
    """Type of synchronous machine model used in dynamic simulation applications."""

    subtransient = "subtransient"
    subtransientTypeF = "subtransientTypeF"
    subtransientTypeJ = "subtransientTypeJ"
    subtransientSimplified = "subtransientSimplified"
    subtransientSimplifiedDirectAxis = "subtransientSimplifiedDirectAxis"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SynchronousMachineModelKind",
            package="TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics",
            guid="{EE3419FE-0A7A-4b84-9D7B-AB4A48EE501D}",
            kind="enumeration",
        )
    )

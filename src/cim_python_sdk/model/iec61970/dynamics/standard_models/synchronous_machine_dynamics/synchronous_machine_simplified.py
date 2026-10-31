"""CIM class SynchronousMachineSimplified (TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_dynamics import (
    SynchronousMachineDynamics,
)


class SynchronousMachineSimplified(SynchronousMachineDynamics):
    """The simplified model represents a synchronous generator as a constant internal voltage
    behind an impedance (Rs + jXp) as shown in the Simplified diagram.

    Since internal voltage is held constant, there is no Efd input and any excitation system
    model will be ignored. There is also no Ifd output.

    This model should not be used for representing a real generator except, perhaps, small
    generators whose response is insignificant.

    The parameters used for the simplified model include:

    - RotatingMachineDynamics.damping (D);

    - RotatingMachineDynamics.inertia (H);

    - RotatingMachineDynamics.statorLeakageReactance (used to exchange jXp for
    SynchronousMachineSimplified);

    - RotatingMachineDynamics.statorResistance (Rs)."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="SynchronousMachineSimplified",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics",
        guid="{2D12C865-F0DB-43fa-9172-C08BDBE68790}",
    )

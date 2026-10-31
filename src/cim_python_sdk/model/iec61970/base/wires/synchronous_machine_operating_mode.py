"""CIM enumeration SynchronousMachineOperatingMode (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SynchronousMachineOperatingMode(CimEnum):
    """Synchronous machine operating mode."""

    generator = "generator"
    condenser = "condenser"
    motor = "motor"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SynchronousMachineOperatingMode",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{2A28E29E-8761-4008-AAD2-FDA8D5889F29}",
            kind="enumeration",
        )
    )

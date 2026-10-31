"""CIM enumeration SynchronousMachineKind (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SynchronousMachineKind(CimEnum):
    """Synchronous machine type."""

    generator = "generator"
    condenser = "condenser"
    generatorOrCondenser = "generatorOrCondenser"
    motor = "motor"
    generatorOrMotor = "generatorOrMotor"
    motorOrCondenser = "motorOrCondenser"
    generatorOrCondenserOrMotor = "generatorOrCondenserOrMotor"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SynchronousMachineKind",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{DC90E008-CE3C-4415-960F-D7BFC4EB4693}",
            kind="enumeration",
        )
    )

"""CIM enumeration AsynchronousMachineKind (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AsynchronousMachineKind(CimEnum):
    """Kind of Asynchronous Machine."""

    generator = "generator"
    motor = "motor"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AsynchronousMachineKind",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{03C06AF1-0AFA-4b28-8911-9258B630BBA4}",
            kind="enumeration",
        )
    )

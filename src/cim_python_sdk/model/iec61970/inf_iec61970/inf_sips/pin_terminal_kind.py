"""CIM enumeration PinTerminalKind (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PinTerminalKind(CimEnum):
    """Categorisation of type of compare done on Terminal."""

    activePower = "activePower"
    apparentPower = "apparentPower"
    reactivePower = "reactivePower"
    voltage = "voltage"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PinTerminalKind",
            package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
            guid="{2BB5947C-26F1-4258-9FEA-805D176CA90E}",
            kind="enumeration",
        )
    )

"""CIM enumeration SVCControlMode (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SVCControlMode(CimEnum):
    """Static VAr Compensator control mode."""

    reactivePower = "reactivePower"
    voltage = "voltage"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SVCControlMode",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{269933B9-3FD0-433d-B360-86FF6CDCDDC8}",
            kind="enumeration",
            deprecated=True,
        )
    )

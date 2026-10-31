"""CIM enumeration ShuntImpedanceLocalControlKind (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ShuntImpedanceLocalControlKind(CimEnum):
    """Kind of local control for shunt impedance."""

    none = "none"
    powerFactor = "powerFactor"
    time = "time"
    temperature = "temperature"
    reactivePower = "reactivePower"
    current = "current"
    voltage = "voltage"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ShuntImpedanceLocalControlKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
            guid="{1DF1339E-9D7C-4d81-A2FE-6E08BC99C021}",
            kind="enumeration",
        )
    )

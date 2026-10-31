"""CIM enumeration ShortCircuitRotorKind (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ShortCircuitRotorKind(CimEnum):
    """Type of rotor, used by short circuit applications."""

    salientPole1 = "salientPole1"
    salientPole2 = "salientPole2"
    turboSeries1 = "turboSeries1"
    turboSeries2 = "turboSeries2"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ShortCircuitRotorKind",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{FD4BEA47-D945-4bc1-A574-5C0618B5C429}",
            kind="enumeration",
        )
    )

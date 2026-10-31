"""CIM enumeration PinEquipmentKind (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PinEquipmentKind(CimEnum):
    """Categorisation of type of compare done on Equipment."""

    inService = "inService"
    ratedCurrent = "ratedCurrent"
    voltageLimit = "voltageLimit"
    currentLimit = "currentLimit"
    activePowerLimit = "activePowerLimit"
    apparentPowerLimit = "apparentPowerLimit"
    connected = "connected"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PinEquipmentKind",
            package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
            guid="{3AA04BCC-27D2-4ff4-BFF6-1A811B466A22}",
            kind="enumeration",
        )
    )

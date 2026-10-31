"""CIM enumeration VsPpccControlKind (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class VsPpccControlKind(CimEnum):
    """Types applicable to the control of real power and/or DC voltage by voltage source
    converter."""

    pPcc = "pPcc"
    udc = "udc"
    pPccAndUdcDroop = "pPccAndUdcDroop"
    pPccAndUdcDroopWithCompensation = "pPccAndUdcDroopWithCompensation"
    pPccAndUdcDroopPilot = "pPccAndUdcDroopPilot"
    phasePcc = "phasePcc"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="VsPpccControlKind",
            package="TC57CIM/IEC61970/Base/DC",
            guid="{AE461FFC-B580-42ce-8520-39C15BCA721F}",
            kind="enumeration",
        )
    )

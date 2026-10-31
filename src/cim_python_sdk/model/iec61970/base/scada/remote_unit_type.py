"""CIM enumeration RemoteUnitType (TC57CIM/IEC61970/Base/SCADA). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RemoteUnitType(CimEnum):
    """Type of remote unit."""

    RTU = "RTU"
    SubstationControlSystem = "SubstationControlSystem"
    ControlCenter = "ControlCenter"
    IED = "IED"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RemoteUnitType",
            package="TC57CIM/IEC61970/Base/SCADA",
            guid="{C956444A-A2E6-4f96-B6F0-DCCF81B934BF}",
            kind="enumeration",
        )
    )

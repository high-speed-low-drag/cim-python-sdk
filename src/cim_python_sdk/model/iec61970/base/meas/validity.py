"""CIM enumeration Validity (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class Validity(CimEnum):
    """Validity for MeasurementValue."""

    GOOD = "GOOD"
    QUESTIONABLE = "QUESTIONABLE"
    INVALID = "INVALID"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="Validity",
            package="TC57CIM/IEC61970/Base/Meas",
            guid="{79E0E8FE-0F93-4fa3-B38F-9A8CA893F785}",
            kind="enumeration",
        )
    )

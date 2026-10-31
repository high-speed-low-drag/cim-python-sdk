"""CIM enumeration CloudKind (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CloudKind(CimEnum):
    """Kind of cloud."""

    altoCumulus = "altoCumulus"
    altoStratus = "altoStratus"
    cirroCumulus = "cirroCumulus"
    cirroStratus = "cirroStratus"
    cirrus = "cirrus"
    cumuloNimbus = "cumuloNimbus"
    cumulus = "cumulus"
    nimboStratus = "nimboStratus"
    stratoCumulus = "stratoCumulus"
    stratus = "stratus"
    toweringCumulus = "toweringCumulus"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CloudKind",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{DC50D0DC-713E-4bb2-9917-0BE1A4014100}",
            kind="enumeration",
        )
    )

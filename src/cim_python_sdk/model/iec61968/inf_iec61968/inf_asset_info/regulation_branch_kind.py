"""CIM enumeration RegulationBranchKind (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RegulationBranchKind(CimEnum):
    """Kind of regulation branch for shunt impedance."""

    line = "line"
    transformer = "transformer"
    switch = "switch"
    breaker = "breaker"
    recloser = "recloser"
    fuse = "fuse"
    sectionner = "sectionner"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RegulationBranchKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
            guid="{0765D2AB-8A32-4676-9233-5C0D221A9CF4}",
            kind="enumeration",
        )
    )

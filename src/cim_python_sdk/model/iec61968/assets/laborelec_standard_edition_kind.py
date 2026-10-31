"""CIM enumeration LaborelecStandardEditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class LaborelecStandardEditionKind(CimEnum):
    """List of editions for Laborelec standards."""

    none = "none"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="LaborelecStandardEditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{CBA804C3-86D7-4ac0-9F4B-6E5D60458089}",
            kind="enumeration",
        )
    )

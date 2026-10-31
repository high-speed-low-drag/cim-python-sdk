"""CIM enumeration LaborelecStandardKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class LaborelecStandardKind(CimEnum):
    """List of Laborelec standards."""

    methanol = "methanol"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="LaborelecStandardKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{1122E9CD-8BF5-48b0-9A0D-C7D0C87ABC69}",
            kind="enumeration",
        )
    )

"""CIM enumeration DobleStandardEditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DobleStandardEditionKind(CimEnum):
    """List of editions for Doble standards."""

    none = "none"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DobleStandardEditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{2021EF35-E613-44a8-9609-BE05BB5A5AF8}",
            kind="enumeration",
        )
    )

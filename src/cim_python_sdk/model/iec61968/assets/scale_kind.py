"""CIM enumeration ScaleKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ScaleKind(CimEnum):
    """Kinds of scaling."""

    linear = "linear"
    exponential = "exponential"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ScaleKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{DA55F75E-AED7-4b4a-9B0C-2ED718D620D7}",
            kind="enumeration",
        )
    )

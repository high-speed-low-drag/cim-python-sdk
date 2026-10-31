"""CIM enumeration SampleContainerType (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SampleContainerType(CimEnum):
    """Types of sample containers."""

    glassCan = "glassCan"
    metalCan = "metalCan"
    syringe = "syringe"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SampleContainerType",
            package="TC57CIM/IEC61968/Assets",
            guid="{73A622F5-63A5-4c8d-BD09-F0A3997811EA}",
            kind="enumeration",
        )
    )

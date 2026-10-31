"""CIM enumeration PoleTreatmentKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PoleTreatmentKind(CimEnum):
    """Kind of treatment for poles."""

    full = "full"
    butt = "butt"
    natural = "natural"
    grayStain = "grayStain"
    greenStain = "greenStain"
    penta = "penta"
    unknown = "unknown"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PoleTreatmentKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{FE3FF735-23CD-42ac-888E-B379DC6C585D}",
            kind="enumeration",
        )
    )

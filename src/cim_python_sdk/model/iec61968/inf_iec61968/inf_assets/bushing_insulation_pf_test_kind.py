"""CIM enumeration BushingInsulationPfTestKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BushingInsulationPfTestKind(CimEnum):
    """Kind of PF test for bushing insulation."""

    c1 = "c1"
    c2 = "c2"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BushingInsulationPfTestKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{F97CAA3B-0ADC-48a7-8683-B16A6F49F13C}",
            kind="enumeration",
        )
    )

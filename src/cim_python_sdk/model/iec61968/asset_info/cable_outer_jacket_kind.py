"""CIM enumeration CableOuterJacketKind (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CableOuterJacketKind(CimEnum):
    """Kind of cable outer jacket."""

    none = "none"
    linearLowDensityPolyethylene = "linearLowDensityPolyethylene"
    pvc = "pvc"
    polyethylene = "polyethylene"
    insulating = "insulating"
    semiconducting = "semiconducting"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CableOuterJacketKind",
            package="TC57CIM/IEC61968/AssetInfo",
            guid="{BAC4240E-5616-4e2c-8A6F-9F8689390E2E}",
            kind="enumeration",
        )
    )

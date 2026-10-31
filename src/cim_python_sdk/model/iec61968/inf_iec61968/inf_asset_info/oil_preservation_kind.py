"""CIM enumeration OilPreservationKind (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilPreservationKind(CimEnum):
    """Kind of oil preservation."""

    freeBreathing = "freeBreathing"
    nitrogenBlanket = "nitrogenBlanket"
    conservator = "conservator"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilPreservationKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
            guid="{DDAC92E2-14E4-4e0c-A384-BC5596BC9520}",
            kind="enumeration",
        )
    )

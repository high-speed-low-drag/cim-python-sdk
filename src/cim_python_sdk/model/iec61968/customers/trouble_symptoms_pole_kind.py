"""CIM enumeration TroubleSymptomsPoleKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TroubleSymptomsPoleKind(CimEnum):
    """The list of values that define the Pole problem."""

    ok = "ok"
    down = "down"
    leaning = "leaning"
    hit = "hit"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TroubleSymptomsPoleKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{C310B957-5274-4257-BA62-B73CE7A34B36}",
            kind="enumeration",
        )
    )

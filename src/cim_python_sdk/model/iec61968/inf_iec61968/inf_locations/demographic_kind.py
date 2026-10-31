"""CIM enumeration DemographicKind (TC57CIM/IEC61968/InfIEC61968/InfLocations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DemographicKind(CimEnum):
    """Demographic kind of a land property."""

    urban = "urban"
    rural = "rural"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DemographicKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfLocations",
            guid="{5728CCB3-280B-44d7-BCCB-906AA5369F62}",
            kind="enumeration",
        )
    )

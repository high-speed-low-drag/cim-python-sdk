"""CIM enumeration OrientationKind (TC57CIM/IEC61970/Base/DiagramLayout). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OrientationKind(CimEnum):
    """The orientation of the coordinate system with respect to top, left, and the coordinate
    number system."""

    positive = "positive"
    negative = "negative"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OrientationKind",
            package="TC57CIM/IEC61970/Base/DiagramLayout",
            guid="{A91C1953-7D39-41d4-B0E8-C88B80E11D26}",
            kind="enumeration",
        )
    )

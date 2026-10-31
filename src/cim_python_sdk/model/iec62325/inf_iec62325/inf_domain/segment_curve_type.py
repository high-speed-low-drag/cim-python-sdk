"""CIM enumeration SegmentCurveType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SegmentCurveType(CimEnum):
    """CIM enumeration SegmentCurveType."""

    COST = "COST"
    CONSULTATIVE = "CONSULTATIVE"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SegmentCurveType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{1833DF1C-00AA-4bde-9F9E-85E31CE07503}",
            kind="enumeration",
        )
    )

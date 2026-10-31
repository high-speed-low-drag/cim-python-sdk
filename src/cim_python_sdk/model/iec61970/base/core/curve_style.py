"""CIM enumeration CurveStyle (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CurveStyle(CimEnum):
    """Style or shape of curve."""

    constantYValue = "constantYValue"
    straightLineYValues = "straightLineYValues"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CurveStyle",
            package="TC57CIM/IEC61970/Base/Core",
            guid="{36FD838A-90B0-4634-A4F2-B6E431D246D7}",
            kind="enumeration",
        )
    )

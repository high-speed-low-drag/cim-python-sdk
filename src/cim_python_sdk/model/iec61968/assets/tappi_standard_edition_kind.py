"""CIM enumeration TAPPIStandardEditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TAPPIStandardEditionKind(CimEnum):
    """List of editions for TAPPI standards."""

    v2009 = "2009"
    none = "none"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TAPPIStandardEditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{E1D1B979-F3C4-4daa-96A3-346147E991AC}",
            kind="enumeration",
        )
    )

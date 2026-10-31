"""CIM enumeration TroubleCallKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TroubleCallKind(CimEnum):
    """Describes the type of Trouble, based on customer input."""

    powerOut = "powerOut"
    lineDown = "lineDown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TroubleCallKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{39F12B89-BCAB-47cf-BF3C-D19717A5B4DC}",
            kind="enumeration",
        )
    )

"""CIM enumeration OperationalLimitDirectionKind (TC57CIM/IEC61970/Base/OperationalLimits). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OperationalLimitDirectionKind(CimEnum):
    """The direction attribute describes the side of a limit that is a violation."""

    high = "high"
    low = "low"
    absoluteValue = "absoluteValue"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OperationalLimitDirectionKind",
            package="TC57CIM/IEC61970/Base/OperationalLimits",
            guid="{2C9E3AFE-268D-41c7-9BC9-29548EF57F5E}",
            kind="enumeration",
        )
    )

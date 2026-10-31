"""CIM enumeration FaultIndicatorResetKind (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class FaultIndicatorResetKind(CimEnum):
    """Kind of resetting the fault indicators."""

    automatic = "automatic"
    manual = "manual"
    remote = "remote"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="FaultIndicatorResetKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
            guid="{7BB32092-FB77-4ead-B49C-569B73F25CA0}",
            kind="enumeration",
        )
    )

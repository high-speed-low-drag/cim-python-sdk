"""CIM enumeration AssetFailureMode (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AssetFailureMode(CimEnum):
    """What asset has failed to be able to do.

    Reason for breaker failure.

    Note: This enumeration provides essential information to asset health analytics. The
    existing list is a starting point and is anticipated to be fleshed out further as
    requirements are better understood (PAB 2016/01/09)."""

    failToCarryLoad = "failToCarryLoad"
    failToClose = "failToClose"
    failToInterrupt = "failToInterrupt"
    failToOpen = "failToOpen"
    failToProvideInsulationLevel = "failToProvideInsulationLevel"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AssetFailureMode",
            package="TC57CIM/IEC61968/Assets",
            guid="{45CFD460-7584-4b41-BFBA-619BB3A992CE}",
            kind="enumeration",
        )
    )

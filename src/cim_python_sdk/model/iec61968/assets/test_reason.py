"""CIM enumeration TestReason (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TestReason(CimEnum):
    """Reason for test."""

    postOperationFault = "postOperationFault"
    postRepair = "postRepair"
    postOilTreatment = "postOilTreatment"
    routine = "routine"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TestReason",
            package="TC57CIM/IEC61968/Assets",
            guid="{4B7FBB8C-99D2-47c2-95A6-74079F8F9AC4}",
            kind="enumeration",
        )
    )

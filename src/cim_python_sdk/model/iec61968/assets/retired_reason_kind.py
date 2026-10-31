"""CIM enumeration RetiredReasonKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class RetiredReasonKind(CimEnum):
    """Reason asset retired."""

    environmental = "environmental"
    excessiveMaintenance = "excessiveMaintenance"
    facilitiesUpgrade = "facilitiesUpgrade"
    failed = "failed"
    obsolescence = "obsolescence"
    other = "other"
    sold = "sold"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="RetiredReasonKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{2D035DD5-C66F-421d-9339-31C7D7205A44}",
            kind="enumeration",
        )
    )

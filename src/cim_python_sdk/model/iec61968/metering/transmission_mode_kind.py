"""CIM enumeration TransmissionModeKind (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TransmissionModeKind(CimEnum):
    """Transmission mode for end device display controls, applicable to premises area network
    (PAN) devices."""

    normal = "normal"
    anonymous = "anonymous"
    both = "both"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TransmissionModeKind",
            package="TC57CIM/IEC61968/Metering",
            guid="{CAB1E8F9-F646-4cd8-BF07-FD26D4021CCF}",
            kind="enumeration",
        )
    )

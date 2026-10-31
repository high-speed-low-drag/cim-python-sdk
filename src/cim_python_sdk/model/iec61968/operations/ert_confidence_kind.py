"""CIM enumeration ERTConfidenceKind (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ERTConfidenceKind(CimEnum):
    """The estimated restoration time (ERT) is the amount of time estimated to correct the
    outage and can have a confidence factor applied such as high or low confidence that the
    ERT will be accomplished. This confidence factor may be updated as needed during the
    outage period - just as the actual ERT can be updated."""

    high = "high"
    low = "low"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ERTConfidenceKind",
            package="TC57CIM/IEC61968/Operations",
            guid="{F71CD8B5-221E-4900-B9AF-51866AC236F1}",
            kind="enumeration",
        )
    )

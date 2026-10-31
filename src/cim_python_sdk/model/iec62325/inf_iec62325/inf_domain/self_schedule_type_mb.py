"""CIM enumeration SelfScheduleTypeMB (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SelfScheduleTypeMB(CimEnum):
    """Self Schedule Types applicable to Mitigated Bid"""

    RMR = "RMR"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SelfScheduleTypeMB",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{2E1723E0-276C-46a9-8910-823B9FDE6B9C}",
            kind="enumeration",
        )
    )

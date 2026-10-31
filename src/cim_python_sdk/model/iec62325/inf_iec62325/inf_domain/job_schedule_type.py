"""CIM enumeration JobScheduleType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class JobScheduleType(CimEnum):
    """CIM enumeration JobScheduleType."""

    CRITICAL = "CRITICAL"
    NONCRITICAL = "NONCRITICAL"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="JobScheduleType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{5C60DBB1-BEB2-4888-AD07-F511DA77253F}",
            kind="enumeration",
        )
    )

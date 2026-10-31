"""CIM enumeration TimePeriodUnit (TC57CIM/IEC62325/Environmental/EnvDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TimePeriodUnit(CimEnum):
    """Units in which reporting frequency is specified."""

    seconds = "seconds"
    minutes = "minutes"
    hours = "hours"
    days = "days"
    weeks = "weeks"
    months = "months"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TimePeriodUnit",
            package="TC57CIM/IEC62325/Environmental/EnvDomain",
            guid="{9768A0B6-3320-438b-902F-2ADAB9B19356}",
            kind="enumeration",
        )
    )

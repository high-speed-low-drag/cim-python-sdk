"""CIM enumeration AlarmDisplayType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AlarmDisplayType(CimEnum):
    """CIM enumeration AlarmDisplayType."""

    Disappear = "Disappear"
    Appear = "Appear"
    Fleeting = "Fleeting"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AlarmDisplayType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{F5077EC7-2BDC-4bc7-A2EA-652BBFFBA879}",
            kind="enumeration",
        )
    )

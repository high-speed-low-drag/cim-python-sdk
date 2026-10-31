"""CIM enumeration OASISIntervalType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OASISIntervalType(CimEnum):
    """CIM enumeration OASISIntervalType."""

    BEGINNING = "BEGINNING"
    ENDING = "ENDING"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OASISIntervalType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{7AF449CC-A336-4e0c-B910-4B4736786526}",
            kind="enumeration",
        )
    )

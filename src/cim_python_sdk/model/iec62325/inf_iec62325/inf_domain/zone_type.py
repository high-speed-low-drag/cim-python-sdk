"""CIM enumeration ZoneType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ZoneType(CimEnum):
    """zone type"""

    LOADZONE = "LOADZONE"
    TRADINGHUB = "TRADINGHUB"
    RUCZONE = "RUCZONE"
    ASREGION = "ASREGION"
    DCA = "DCA"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ZoneType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{31C02A52-C9D6-4f4f-A0CD-DC7072BFD643}",
            kind="enumeration",
        )
    )

"""CIM enumeration UnitTypeEMS (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class UnitTypeEMS(CimEnum):
    """MW

    FLAG"""

    MW = "MW"
    FLAG = "FLAG"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="UnitTypeEMS",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{C94C3321-078D-4827-9FF7-C68971BF0294}",
            kind="enumeration",
        )
    )

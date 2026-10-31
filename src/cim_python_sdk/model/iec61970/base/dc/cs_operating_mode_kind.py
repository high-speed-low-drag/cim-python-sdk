"""CIM enumeration CsOperatingModeKind (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CsOperatingModeKind(CimEnum):
    """Operating mode for HVDC line operating as Current Source Converter."""

    inverter = "inverter"
    rectifier = "rectifier"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CsOperatingModeKind",
            package="TC57CIM/IEC61970/Base/DC",
            guid="{2B29A5B8-7C9E-458b-A8D7-897FE0BF52C8}",
            kind="enumeration",
        )
    )

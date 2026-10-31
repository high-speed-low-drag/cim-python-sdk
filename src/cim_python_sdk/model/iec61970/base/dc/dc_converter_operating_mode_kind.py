"""CIM enumeration DCConverterOperatingModeKind (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DCConverterOperatingModeKind(CimEnum):
    """The operating mode of an HVDC bipole."""

    bipolar = "bipolar"
    monopolarMetallicReturn = "monopolarMetallicReturn"
    monopolarGroundReturn = "monopolarGroundReturn"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DCConverterOperatingModeKind",
            package="TC57CIM/IEC61970/Base/DC",
            guid="{C8B0DDAD-5080-46ea-85B9-C23A0FA34DE8}",
            kind="enumeration",
        )
    )

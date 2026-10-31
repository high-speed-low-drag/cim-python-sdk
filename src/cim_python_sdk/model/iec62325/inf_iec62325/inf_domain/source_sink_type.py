"""CIM enumeration SourceSinkType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SourceSinkType(CimEnum):
    """CIM enumeration SourceSinkType."""

    Source = "Source"
    Sink = "Sink"
    Neither = "Neither"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SourceSinkType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{9026EE61-8E4B-4e3d-AFF8-92D284407A05}",
            kind="enumeration",
        )
    )

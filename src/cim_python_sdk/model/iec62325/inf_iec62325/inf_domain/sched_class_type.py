"""CIM enumeration SchedClassType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class SchedClassType(CimEnum):
    """CIM enumeration SchedClassType."""

    P = "P"
    R = "R"
    F = "F"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="SchedClassType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{83A7FC09-5452-49bb-91E2-91B193DFFE96}",
            kind="enumeration",
        )
    )

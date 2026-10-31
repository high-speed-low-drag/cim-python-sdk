"""CIM enumeration DesignKind (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DesignKind(CimEnum):
    """Kind of design."""

    estimated = "estimated"
    asBuilt = "asBuilt"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DesignKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfWork",
            guid="{90CA1FD5-6E7B-4e77-AD7C-F20383CA6CED}",
            kind="enumeration",
        )
    )

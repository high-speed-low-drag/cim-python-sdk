"""CIM enumeration JointConfigurationKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class JointConfigurationKind(CimEnum):
    """Kind of configuration for joints."""

    wires3to1 = "wires3to1"
    wires2to1 = "wires2to1"
    wires1to1 = "wires1to1"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="JointConfigurationKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{4025A5DE-B03E-4d90-87F7-1BD696834393}",
            kind="enumeration",
        )
    )

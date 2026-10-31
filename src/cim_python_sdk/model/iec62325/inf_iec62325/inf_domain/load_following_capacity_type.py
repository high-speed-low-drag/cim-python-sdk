"""CIM enumeration LoadFollowingCapacityType (TC57CIM/IEC62325/InfIEC62325/InfDomain). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class LoadFollowingCapacityType(CimEnum):
    """CIM enumeration LoadFollowingCapacityType."""

    UP = "UP"
    DOWN = "DOWN"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="LoadFollowingCapacityType",
            package="TC57CIM/IEC62325/InfIEC62325/InfDomain",
            guid="{ABC959DC-721F-4bc9-94BE-940B0844075A}",
            kind="enumeration",
        )
    )

"""CIM enumeration ShuntImpedanceControlKind (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ShuntImpedanceControlKind(CimEnum):
    """Kind of control for shunt impedance."""

    fixed = "fixed"
    localOnly = "localOnly"
    remoteOnly = "remoteOnly"
    remoteWithLocalOverride = "remoteWithLocalOverride"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ShuntImpedanceControlKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
            guid="{6F86F7A1-3B9B-4675-BFE8-7B47013B60A1}",
            kind="enumeration",
        )
    )

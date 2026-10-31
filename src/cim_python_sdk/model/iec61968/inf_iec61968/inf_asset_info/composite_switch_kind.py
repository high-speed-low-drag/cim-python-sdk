"""CIM enumeration CompositeSwitchKind (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CompositeSwitchKind(CimEnum):
    """Kind of composite switch."""

    throwOver = "throwOver"
    escoThrowOver = "escoThrowOver"
    ral = "ral"
    gral = "gral"
    regulatorBypass = "regulatorBypass"
    ugMultiSwitch = "ugMultiSwitch"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CompositeSwitchKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
            guid="{718854EE-F86E-4308-A11D-8D179DA07DED}",
            kind="enumeration",
        )
    )

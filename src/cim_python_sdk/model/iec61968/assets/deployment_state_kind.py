"""CIM enumeration DeploymentStateKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DeploymentStateKind(CimEnum):
    """Possible states of asset deployment."""

    notYetInstalled = "notYetInstalled"
    installed = "installed"
    inService = "inService"
    outOfService = "outOfService"
    removed = "removed"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DeploymentStateKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{5503A06C-B46F-43f9-9BC7-A9B9D4C113EC}",
            kind="enumeration",
        )
    )

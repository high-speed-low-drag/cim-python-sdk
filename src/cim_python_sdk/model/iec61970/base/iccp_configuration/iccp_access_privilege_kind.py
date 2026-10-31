"""CIM enumeration ICCPAccessPrivilegeKind (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ICCPAccessPrivilegeKind(CimEnum):
    """Provides access privilege information regarding an ICCP point."""

    readOnly = "readOnly"
    readWrite = "readWrite"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ICCPAccessPrivilegeKind",
            package="TC57CIM/IEC61970/Base/ICCPConfiguration",
            guid="{D336341F-ED1A-4fcb-9152-78BC95E89F18}",
            kind="enumeration",
        )
    )

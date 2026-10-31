"""CIM enumeration ICCPScopeKind (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ICCPScopeKind(CimEnum):
    """Specifies the control centre scope."""

    vCC = "vCC"
    iCC = "iCC"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ICCPScopeKind",
            package="TC57CIM/IEC61970/Base/ICCPConfiguration",
            guid="{222D3D35-C731-46a4-9157-4AB6623E7F29}",
            kind="enumeration",
        )
    )

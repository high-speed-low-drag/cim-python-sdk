"""CIM enumeration WindingConnection (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WindingConnection(CimEnum):
    """Winding connection type."""

    D = "D"
    Y = "Y"
    Z = "Z"
    Yn = "Yn"
    Zn = "Zn"
    A = "A"
    I = "I"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WindingConnection",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{FF3816E1-1CFE-4051-9F75-0F3E94DABAFB}",
            kind="enumeration",
        )
    )

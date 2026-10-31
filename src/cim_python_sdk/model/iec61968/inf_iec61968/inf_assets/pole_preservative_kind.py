"""CIM enumeration PolePreservativeKind (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class PolePreservativeKind(CimEnum):
    """Preservative kind for poles."""

    creosote = "creosote"
    cellon = "cellon"
    naphthena = "naphthena"
    penta = "penta"
    chemonite = "chemonite"
    unknown = "unknown"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="PolePreservativeKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
            guid="{AB3FD322-F29E-4933-827B-EEE6C6AD3BF7}",
            kind="enumeration",
        )
    )

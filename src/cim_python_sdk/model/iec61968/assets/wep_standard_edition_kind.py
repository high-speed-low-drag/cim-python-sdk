"""CIM enumeration WEPStandardEditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WEPStandardEditionKind(CimEnum):
    """List of editions for WEP standards."""

    none = "none"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WEPStandardEditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{804116AA-E77C-415c-8854-717DB54778DA}",
            kind="enumeration",
        )
    )

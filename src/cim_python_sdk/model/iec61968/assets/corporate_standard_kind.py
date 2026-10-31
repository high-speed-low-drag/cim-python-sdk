"""CIM enumeration CorporateStandardKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CorporateStandardKind(CimEnum):
    """Kind of corporate standard."""

    standard = "standard"
    experimental = "experimental"
    underEvaluation = "underEvaluation"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CorporateStandardKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{A378DE43-41AA-4680-B481-A7C325C36EF4}",
            kind="enumeration",
        )
    )

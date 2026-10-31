"""CIM enumeration IEEEStandardEditionKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class IEEEStandardEditionKind(CimEnum):
    """List of editions for IEEE standards."""

    v1978 = "1978"
    v1995 = "1995"
    none = "none"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="IEEEStandardEditionKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{B4926170-C2FB-4da5-AA7B-7BFDE19A469A}",
            kind="enumeration",
        )
    )

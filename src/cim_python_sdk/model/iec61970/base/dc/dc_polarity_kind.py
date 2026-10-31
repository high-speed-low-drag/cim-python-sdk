"""CIM enumeration DCPolarityKind (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class DCPolarityKind(CimEnum):
    """Polarity for DC circuits."""

    positive = "positive"
    middle = "middle"
    negative = "negative"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="DCPolarityKind",
            package="TC57CIM/IEC61970/Base/DC",
            guid="{54D992DD-DA54-4e0b-81B3-263AF2896C50}",
            kind="enumeration",
        )
    )

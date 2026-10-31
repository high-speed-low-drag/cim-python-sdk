"""CIM enumeration TransformerControlMode (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TransformerControlMode(CimEnum):
    """Control modes for a transformer."""

    volt = "volt"
    reactive = "reactive"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TransformerControlMode",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{601E1E7A-46DB-4d07-95C8-4B61EBFC65C0}",
            kind="enumeration",
        )
    )

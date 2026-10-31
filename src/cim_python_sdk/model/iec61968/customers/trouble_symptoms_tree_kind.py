"""CIM enumeration TroubleSymptomsTree Kind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TroubleSymptomsTree_Kind(CimEnum):
    """The list of items that define the tree problem."""

    ok = "ok"
    limbOnWire = "limbOnWire"
    limbOnService = "limbOnService"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TroubleSymptomsTree Kind",
            package="TC57CIM/IEC61968/Customers",
            guid="{BEF03A8E-4F6E-4403-9290-D06DAE614669}",
            kind="enumeration",
        )
    )

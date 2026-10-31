"""CIM enumeration TroubleSymptomsWireKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TroubleSymptomsWireKind(CimEnum):
    """The list of items that define the wire problem."""

    serviceDown = "serviceDown"
    wireDown = "wireDown"
    wireburning = "wireburning"
    other = "other"
    ok = "ok"
    digIn = "digIn"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TroubleSymptomsWireKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{7508F862-FB6B-4c11-87B8-33170F20ED82}",
            kind="enumeration",
        )
    )

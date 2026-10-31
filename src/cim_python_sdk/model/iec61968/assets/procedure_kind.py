"""CIM enumeration ProcedureKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class ProcedureKind(CimEnum):
    """Kind of procedure."""

    inspection = "inspection"
    diagnosis = "diagnosis"
    maintenance = "maintenance"
    test = "test"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="ProcedureKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{1516C9A8-910D-4b98-AAED-035828BF3B59}",
            kind="enumeration",
        )
    )

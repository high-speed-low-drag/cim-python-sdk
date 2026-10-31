"""CIM enumeration TroubleSymptomsExtentKind (TC57CIM/IEC61968/Customers). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TroubleSymptomsExtentKind(CimEnum):
    """The enumerated values that define the extent of the problem."""

    singleCustomer = "singleCustomer"
    ok = "ok"
    neighbour = "neighbour"
    other = "other"
    entireNeighbourhood = "entireNeighbourhood"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TroubleSymptomsExtentKind",
            package="TC57CIM/IEC61968/Customers",
            guid="{95B62B7B-A977-427f-802A-2CFE818274DB}",
            kind="enumeration",
        )
    )

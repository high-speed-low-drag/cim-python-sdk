"""CIM enumeration CoolantType (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class CoolantType(CimEnum):
    """Method of cooling a machine."""

    air = "air"
    hydrogenGas = "hydrogenGas"
    water = "water"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="CoolantType",
            package="TC57CIM/IEC61970/Base/Wires",
            guid="{B998EE6D-BC68-49d3-813C-F5AB11CF6CFD}",
            kind="enumeration",
        )
    )

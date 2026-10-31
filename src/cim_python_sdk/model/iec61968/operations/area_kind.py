"""CIM enumeration AreaKind (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class AreaKind(CimEnum):
    """Enumeration for the type of area defined; e.g., county, state, parish, zipcode, etc."""

    borough = "borough"
    county = "county"
    parish = "parish"
    serviceArea = "serviceArea"
    state = "state"
    township = "township"
    ward = "ward"
    zipcode = "zipcode"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="AreaKind",
            package="TC57CIM/IEC61968/Operations",
            guid="{F717AA93-4655-4e02-B8A8-1E4E0D83BB6D}",
            kind="enumeration",
        )
    )

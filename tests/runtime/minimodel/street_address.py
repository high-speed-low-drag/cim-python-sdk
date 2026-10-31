"""CIM compound StreetAddress (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class StreetAddress(CimCompound):
    """General purpose street and postal address information."""

    __slots__ = ("postal_code", "street", "town")

    postal_code: str | None
    street: str | None
    town: str | None

    _cim_meta = ClassMeta(
        cim_name="StreetAddress",
        package="TC57CIM/IEC61968/Common",
        guid="{00000000-0000-0000-0000-00000000B002}",
        kind="compound",
        attributes=(
            AttrMeta("postal_code", "postalCode", "str", 0, 1, "primitive"),
            AttrMeta("street", "street", "str", 0, 1, "primitive"),
            AttrMeta("town", "town", "str", 0, 1, "primitive"),
        ),
    )

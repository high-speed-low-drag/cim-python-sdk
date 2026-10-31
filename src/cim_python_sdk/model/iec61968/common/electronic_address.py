"""CIM compound ElectronicAddress (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class ElectronicAddress(CimCompound):
    """Electronic address information."""

    __slots__ = ("email1", "email2", "lan", "mac", "password", "radio", "user_id", "web")

    lan: str | None
    mac: str | None
    email1: str | None
    email2: str | None
    web: str | None
    radio: str | None
    user_id: str | None
    password: str | None

    _cim_meta = ClassMeta(
        cim_name="ElectronicAddress",
        package="TC57CIM/IEC61968/Common",
        guid="{77039F8D-76F9-4d56-8B1B-23F26D4CF355}",
        kind="compound",
        attributes=(
            AttrMeta("lan", "lan", "str", 0, 1, "primitive"),
            AttrMeta("mac", "mac", "str", 0, 1, "primitive"),
            AttrMeta("email1", "email1", "str", 0, 1, "primitive"),
            AttrMeta("email2", "email2", "str", 0, 1, "primitive"),
            AttrMeta("web", "web", "str", 0, 1, "primitive"),
            AttrMeta("radio", "radio", "str", 0, 1, "primitive"),
            AttrMeta("user_id", "userID", "str", 0, 1, "primitive"),
            AttrMeta("password", "password", "str", 0, 1, "primitive"),
        ),
    )

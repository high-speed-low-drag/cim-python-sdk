"""CIM compound TownDetail (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class TownDetail(CimCompound):
    """Town details, in the context of address."""

    __slots__ = ("code", "country", "name", "section", "state_or_province")

    code: str | None
    section: str | None
    name: str | None
    state_or_province: str | None
    country: str | None

    _cim_meta = ClassMeta(
        cim_name="TownDetail",
        package="TC57CIM/IEC61968/Common",
        guid="{26275F22-BDC6-4a76-ABE7-AC797CFE35D9}",
        kind="compound",
        attributes=(
            AttrMeta("code", "code", "str", 0, 1, "primitive"),
            AttrMeta("section", "section", "str", 0, 1, "primitive"),
            AttrMeta("name", "name", "str", 0, 1, "primitive"),
            AttrMeta("state_or_province", "stateOrProvince", "str", 0, 1, "primitive"),
            AttrMeta("country", "country", "str", 0, 1, "primitive"),
        ),
    )

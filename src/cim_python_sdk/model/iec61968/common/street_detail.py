"""CIM compound StreetDetail (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class StreetDetail(CimCompound):
    """Street details, in the context of address."""

    __slots__ = (
        "address_general",
        "address_general2",
        "address_general3",
        "building_name",
        "code",
        "floor_identification",
        "name",
        "number",
        "prefix",
        "suffix",
        "suite_number",
        "type",
        "within_town_limits",
    )

    number: str | None
    name: str | None
    suffix: str | None
    prefix: str | None
    type: str | None
    code: str | None
    building_name: str | None
    suite_number: str | None
    address_general: str | None
    address_general2: str | None
    address_general3: str | None
    within_town_limits: bool | None
    floor_identification: str | None

    _cim_meta = ClassMeta(
        cim_name="StreetDetail",
        package="TC57CIM/IEC61968/Common",
        guid="{A4198329-7F25-4e72-8E8D-C4B4D37288F8}",
        kind="compound",
        attributes=(
            AttrMeta("number", "number", "str", 0, 1, "primitive"),
            AttrMeta("name", "name", "str", 0, 1, "primitive"),
            AttrMeta("suffix", "suffix", "str", 0, 1, "primitive"),
            AttrMeta("prefix", "prefix", "str", 0, 1, "primitive"),
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("code", "code", "str", 0, 1, "primitive"),
            AttrMeta("building_name", "buildingName", "str", 0, 1, "primitive"),
            AttrMeta("suite_number", "suiteNumber", "str", 0, 1, "primitive"),
            AttrMeta("address_general", "addressGeneral", "str", 0, 1, "primitive"),
            AttrMeta("address_general2", "addressGeneral2", "str", 0, 1, "primitive"),
            AttrMeta("address_general3", "addressGeneral3", "str", 0, 1, "primitive"),
            AttrMeta("within_town_limits", "withinTownLimits", "bool", 0, 1, "primitive"),
            AttrMeta("floor_identification", "floorIdentification", "str", 0, 1, "primitive"),
        ),
    )

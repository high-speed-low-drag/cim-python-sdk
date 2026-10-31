"""CIM compound TelephoneNumber (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimCompound, ClassMeta


class TelephoneNumber(CimCompound):
    """Telephone number."""

    __slots__ = (
        "area_code",
        "city_code",
        "country_code",
        "dial_out",
        "extension",
        "international_prefix",
        "itu_phone",
        "local_number",
    )

    country_code: str | None
    area_code: str | None
    city_code: str | None
    local_number: str | None
    extension: str | None
    dial_out: str | None
    international_prefix: str | None
    itu_phone: str | None

    _cim_meta = ClassMeta(
        cim_name="TelephoneNumber",
        package="TC57CIM/IEC61968/Common",
        guid="{456C7633-96C3-448b-BF2D-8D6110084CC6}",
        kind="compound",
        attributes=(
            AttrMeta("country_code", "countryCode", "str", 0, 1, "primitive"),
            AttrMeta("area_code", "areaCode", "str", 0, 1, "primitive"),
            AttrMeta("city_code", "cityCode", "str", 0, 1, "primitive"),
            AttrMeta("local_number", "localNumber", "str", 0, 1, "primitive"),
            AttrMeta("extension", "extension", "str", 0, 1, "primitive"),
            AttrMeta("dial_out", "dialOut", "str", 0, 1, "primitive"),
            AttrMeta("international_prefix", "internationalPrefix", "str", 0, 1, "primitive"),
            AttrMeta("itu_phone", "ituPhone", "str", 0, 1, "primitive"),
        ),
    )

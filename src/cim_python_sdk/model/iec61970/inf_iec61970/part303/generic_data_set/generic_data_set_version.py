"""CIM class GenericDataSetVersion (TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any


class GenericDataSetVersion(CimObject):
    """CIM class GenericDataSetVersion."""

    __slots__ = ("major_version", "minor_version", "published")

    major_version: str | None
    minor_version: str | None
    published: _dt.date | None

    _cim_meta = ClassMeta(
        cim_name="GenericDataSetVersion",
        package="TC57CIM/IEC61970/InfIEC61970/Part303/GenericDataSet",
        guid="{87547DA2-F02C-4ffa-9CD3-F2A19B225127}",
        attributes=(
            AttrMeta("major_version", "majorVersion", "str", 0, 1, "primitive", "2016"),
            AttrMeta("minor_version", "minorVersion", "str", 0, 1, "primitive", "01"),
            AttrMeta("published", "published", "date", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        major_version: str | None = "2016",
        minor_version: str | None = "01",
        published: _dt.date | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.major_version = major_version
        self.minor_version = minor_version
        self.published = published

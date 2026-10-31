"""CIM class IdentifiedObject (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, new_mrid

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class IdentifiedObject(CimObject):
    """This is a root class to provide common identification for all classes needing
    identification and naming attributes."""

    __slots__ = ("description", "mrid", "name")

    description: str | None
    mrid: str | None
    name: str | None

    _cim_meta = ClassMeta(
        cim_name="IdentifiedObject",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{00000000-0000-0000-0000-00000000C001}",
        attributes=(
            AttrMeta("description", "description", "str", 0, 1, "primitive"),
            AttrMeta("mrid", "mRID", "str", 0, 1, "primitive"),
            AttrMeta("name", "name", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        description: str | None = None,
        mrid: str | None = None,
        name: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.description = description
        self.mrid = new_mrid() if mrid is None else mrid
        self.name = name

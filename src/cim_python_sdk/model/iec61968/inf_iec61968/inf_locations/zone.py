"""CIM class Zone (TC57CIM/IEC61968/InfIEC61968/InfLocations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.common.location import Location

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_locations.zone_kind import ZoneKind


class Zone(Location):
    """Area divided off from other areas. It may be part of the electrical network, a land area
    where special restrictions apply, weather areas, etc. For weather, it is an area where a
    set of relatively homogenous weather measurements apply."""

    __slots__ = ("kind",)

    kind: ZoneKind | None

    _cim_meta = ClassMeta(
        cim_name="Zone",
        package="TC57CIM/IEC61968/InfIEC61968/InfLocations",
        guid="{23655D84-D21F-4411-9083-8AE7916DDA1F}",
        attributes=(AttrMeta("kind", "kind", "ZoneKind", 0, 1, "enumeration"),),
    )

    def __init__(
        self,
        *,
        kind: ZoneKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind

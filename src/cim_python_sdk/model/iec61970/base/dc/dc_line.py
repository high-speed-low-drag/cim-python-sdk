"""CIM class DCLine (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.dc.dc_equipment_container import DCEquipmentContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.sub_geographical_region import (
        SubGeographicalRegion,
    )


class DCLine(DCEquipmentContainer):
    """Overhead lines and/or cables connecting two or more HVDC substations."""

    __slots__ = ("_region",)

    region: One[SubGeographicalRegion] = One(
        EndMeta(
            name="region",
            cim_role="Region",
            target="cim_python_sdk.model.iec61970.base.core.sub_geographical_region:SubGeographicalRegion",
            many=False,
            lower=0,
            upper=1,
            inverse="dc_lines",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DCLine",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{4C5447F8-6789-47ec-9729-6B7DB3330C1D}",
        ends=(region.meta,),
    )

    def __init__(
        self,
        *,
        region: SubGeographicalRegion | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if region is not None:
            self.region = region

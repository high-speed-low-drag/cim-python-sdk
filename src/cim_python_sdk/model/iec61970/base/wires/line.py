"""CIM class Line (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.equipment_container import EquipmentContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.sub_geographical_region import (
        SubGeographicalRegion,
    )


class Line(EquipmentContainer):
    """Contains equipment beyond a substation belonging to a power transmission line."""

    __slots__ = ("_region",)

    region: One[SubGeographicalRegion] = One(
        EndMeta(
            name="region",
            cim_role="Region",
            target="cim_python_sdk.model.iec61970.base.core.sub_geographical_region:SubGeographicalRegion",
            many=False,
            lower=0,
            upper=1,
            inverse="lines",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Line",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{43D9D2B8-DA1E-45c4-B99D-EC28FCAB742B}",
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

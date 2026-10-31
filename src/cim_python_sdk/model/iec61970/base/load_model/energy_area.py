"""CIM class EnergyArea (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.control_area.control_area import ControlArea


class EnergyArea(IdentifiedObject):
    """Describes an area having energy production or consumption. Specializations are intended
    to support the load allocation function as typically required in energy management
    systems or planning studies to allocate hypothesized load levels to individual load
    points for power flow analysis. Often the energy area can be linked to both measured and
    forecast load levels."""

    __slots__ = ("_control_area",)

    control_area: One[ControlArea] = One(
        EndMeta(
            name="control_area",
            cim_role="ControlArea",
            target="cim_python_sdk.model.iec61970.base.control_area.control_area:ControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_area",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyArea",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{EBAF7081-971E-4960-A0AB-B38C20682FE7}",
        ends=(control_area.meta,),
    )

    def __init__(
        self,
        *,
        control_area: ControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if control_area is not None:
            self.control_area = control_area

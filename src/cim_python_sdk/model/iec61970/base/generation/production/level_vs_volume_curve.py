"""CIM class LevelVsVolumeCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.reservoir import Reservoir


class LevelVsVolumeCurve(Curve):
    """Relationship between reservoir volume and reservoir level. The volume is at the Y-axis
    and the reservoir level at the X-axis."""

    __slots__ = ("_reservoir",)

    reservoir: One[Reservoir] = One(
        EndMeta(
            name="reservoir",
            cim_role="Reservoir",
            target="cim_python_sdk.model.iec61970.base.generation.production.reservoir:Reservoir",
            many=False,
            lower=1,
            upper=1,
            inverse="level_vs_volume_curves",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LevelVsVolumeCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{F9F1E0C3-9A25-4e46-8E17-91ED55579473}",
        ends=(reservoir.meta,),
    )

    def __init__(
        self,
        *,
        reservoir: Reservoir | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if reservoir is not None:
            self.reservoir = reservoir

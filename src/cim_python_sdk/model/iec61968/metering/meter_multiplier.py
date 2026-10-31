"""CIM class MeterMultiplier (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.meter import Meter
    from cim_python_sdk.model.iec61968.metering.meter_multiplier_kind import MeterMultiplierKind


class MeterMultiplier(IdentifiedObject):
    """Multiplier applied at the meter."""

    __slots__ = ("_meter", "kind", "value")

    kind: MeterMultiplierKind | None
    value: float | None

    meter: One[Meter] = One(
        EndMeta(
            name="meter",
            cim_role="Meter",
            target="cim_python_sdk.model.iec61968.metering.meter:Meter",
            many=False,
            lower=0,
            upper=1,
            inverse="meter_multipliers",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MeterMultiplier",
        package="TC57CIM/IEC61968/Metering",
        guid="{8A9D442B-3BA0-4165-8ABA-EF2D8A351B51}",
        attributes=(
            AttrMeta("kind", "kind", "MeterMultiplierKind", 0, 1, "enumeration"),
            AttrMeta("value", "value", "float", 0, 1, "primitive"),
        ),
        ends=(meter.meta,),
    )

    def __init__(
        self,
        *,
        kind: MeterMultiplierKind | None = None,
        value: float | None = None,
        meter: Meter | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.value = value
        if meter is not None:
            self.meter = meter

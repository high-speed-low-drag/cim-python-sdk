"""CIM class MeasurementAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.measurement import Measurement


class MeasurementAction(SwitchingAction):
    """Measurement taken as a switching step."""

    __slots__ = ("_measurement",)

    measurement: One[Measurement] = One(
        EndMeta(
            name="measurement",
            cim_role="Measurement",
            target="cim_python_sdk.model.iec61970.base.meas.measurement:Measurement",
            many=False,
            lower=0,
            upper=1,
            inverse="measurement_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MeasurementAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{D2A8F7F3-5902-40b2-9A33-6873CB46EAAD}",
        ends=(measurement.meta,),
    )

    def __init__(
        self,
        *,
        measurement: Measurement | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if measurement is not None:
            self.measurement = measurement

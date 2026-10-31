"""CIM class DiscreteValue (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.measurement_value import MeasurementValue

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.meas.command import Command
    from cim_python_sdk.model.iec61970.base.meas.discrete import Discrete


class DiscreteValue(MeasurementValue):
    """DiscreteValue represents a discrete MeasurementValue."""

    __slots__ = ("_command", "_discrete", "value")

    value: int | None

    discrete: One[Discrete] = One(
        EndMeta(
            name="discrete",
            cim_role="Discrete",
            target="cim_python_sdk.model.iec61970.base.meas.discrete:Discrete",
            many=False,
            lower=1,
            upper=1,
            inverse="discrete_values",
            aggregation="none",
        )
    )
    command: One[Command] = One(
        EndMeta(
            name="command",
            cim_role="Command",
            target="cim_python_sdk.model.iec61970.base.meas.command:Command",
            many=False,
            lower=0,
            upper=1,
            inverse="discrete_value",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DiscreteValue",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{11E52FB7-7CC9-486d-BDA1-A069F388E930}",
        attributes=(AttrMeta("value", "value", "int", 0, 1, "primitive"),),
        ends=(
            discrete.meta,
            command.meta,
        ),
    )

    def __init__(
        self,
        *,
        value: int | None = None,
        discrete: Discrete | None = None,
        command: Command | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.value = value
        if discrete is not None:
            self.discrete = discrete
        if command is not None:
            self.command = command

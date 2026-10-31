"""CIM class LoadAggregate (TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_dynamics import (
    LoadDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_motor import (
        LoadMotor,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_static import (
        LoadStatic,
    )


class LoadAggregate(LoadDynamics):
    """Aggregate loads are used to represent all or part of the real and reactive load from one
    or more loads in the static (power flow) data. This load is usually the aggregation of
    many individual load devices and the load model is an approximate representation of the
    aggregate response of the load devices to system disturbances.

    Standard aggregate load model comprised of static and/or dynamic components. A static
    load model represents the sensitivity of the real and reactive power consumed by the
    load to the amplitude and frequency of the bus voltage. A dynamic load model can be used
    to represent the aggregate response of the motor components of the load."""

    __slots__ = ("_load_motor", "_load_static")

    load_motor: One[LoadMotor] = One(
        EndMeta(
            name="load_motor",
            cim_role="LoadMotor",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_motor:LoadMotor",
            many=False,
            lower=0,
            upper=1,
            inverse="load_aggregate",
            aggregation="none",
        )
    )
    load_static: One[LoadStatic] = One(
        EndMeta(
            name="load_static",
            cim_role="LoadStatic",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_static:LoadStatic",
            many=False,
            lower=0,
            upper=1,
            inverse="load_aggregate",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LoadAggregate",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics",
        guid="{EE06C0E9-A1EE-4b3f-AD4D-D225DFE10EEF}",
        ends=(
            load_motor.meta,
            load_static.meta,
        ),
    )

    def __init__(
        self,
        *,
        load_motor: LoadMotor | None = None,
        load_static: LoadStatic | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if load_motor is not None:
            self.load_motor = load_motor
        if load_static is not None:
            self.load_static = load_static

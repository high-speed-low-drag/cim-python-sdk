"""CIM class StaticVarCompensator (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.regulating_cond_eq import RegulatingCondEq

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.svc_control_mode import SVCControlMode
    from cim_python_sdk.model.iec61970.dynamics.standard_models.static_var_compensator_dynamics.static_var_compensator_dynamics import (
        StaticVarCompensatorDynamics,
    )


class StaticVarCompensator(RegulatingCondEq):
    """A facility for providing variable and controllable shunt reactive power. The SVC
    typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and
    thyristor-switched capacitor arms.

    The SVC may operate in fixed MVar output mode or in voltage control mode. When in
    voltage control mode, the output of the SVC will be proportional to the deviation of
    voltage at the controlled bus from the voltage setpoint. The SVC characteristic slope
    defines the proportion. If the voltage at the controlled bus is equal to the voltage
    setpoint, the SVC MVar output is zero."""

    __slots__ = (
        "_static_var_compensator_dynamics",
        "capacitive_rating",
        "inductive_rating",
        "q",
        "s_vc_control_mode",
        "slope",
        "voltage_set_point",
    )

    capacitive_rating: float | None  # Reactance
    inductive_rating: float | None  # Reactance
    slope: float | None  # VoltagePerReactivePower
    q: float | None  # ReactivePower
    s_vc_control_mode: SVCControlMode | None
    voltage_set_point: float | None  # Voltage

    static_var_compensator_dynamics: One[StaticVarCompensatorDynamics] = One(
        EndMeta(
            name="static_var_compensator_dynamics",
            cim_role="StaticVarCompensatorDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.static_var_compensator_dynamics.static_var_compensator_dynamics:StaticVarCompensatorDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="static_var_compensator",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StaticVarCompensator",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{B540EF99-8CE4-4da6-9E4D-D22E867F8BAE}",
        attributes=(
            AttrMeta("capacitive_rating", "capacitiveRating", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("inductive_rating", "inductiveRating", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("slope", "slope", "VoltagePerReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("q", "q", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta(
                "s_vc_control_mode",
                "sVCControlMode",
                "SVCControlMode",
                0,
                1,
                "enumeration",
                deprecated=True,
            ),
            AttrMeta(
                "voltage_set_point",
                "voltageSetPoint",
                "Voltage",
                0,
                1,
                "cimdatatype",
                deprecated=True,
            ),
        ),
        ends=(static_var_compensator_dynamics.meta,),
    )

    def __init__(
        self,
        *,
        capacitive_rating: float | None = None,
        inductive_rating: float | None = None,
        slope: float | None = None,
        q: float | None = None,
        s_vc_control_mode: SVCControlMode | None = None,
        voltage_set_point: float | None = None,
        static_var_compensator_dynamics: StaticVarCompensatorDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.capacitive_rating = capacitive_rating
        self.inductive_rating = inductive_rating
        self.slope = slope
        self.q = q
        self.s_vc_control_mode = s_vc_control_mode
        self.voltage_set_point = voltage_set_point
        if static_var_compensator_dynamics is not None:
            self.static_var_compensator_dynamics = static_var_compensator_dynamics

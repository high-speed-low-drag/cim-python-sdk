"""CIM class ShuntCompensatorDynamicData (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_shunt_compensator import (
        MktShuntCompensator,
    )


class ShuntCompensatorDynamicData(CimObject):
    """Optimal Power Flow or State Estimator Filter Bank Data for OTS. This is used for
    RealTime, Study and Maintenance Users."""

    __slots__ = (
        "_mkt_shunt_compensator",
        "connection_status",
        "desired_voltage",
        "m_var_injection",
        "step_position",
        "voltage_regulation_status",
    )

    m_var_injection: float | None
    connection_status: int | None
    desired_voltage: float | None
    voltage_regulation_status: bool | None
    step_position: int | None

    mkt_shunt_compensator: One[MktShuntCompensator] = One(
        EndMeta(
            name="mkt_shunt_compensator",
            cim_role="MktShuntCompensator",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_shunt_compensator:MktShuntCompensator",
            many=False,
            lower=1,
            upper=1,
            inverse="shunt_compensator_dynamic_data",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ShuntCompensatorDynamicData",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{0D14F688-E1B1-414a-8268-543060FFAE9A}",
        attributes=(
            AttrMeta("m_var_injection", "mVARInjection", "float", 0, 1, "primitive"),
            AttrMeta("connection_status", "connectionStatus", "int", 0, 1, "primitive"),
            AttrMeta("desired_voltage", "desiredVoltage", "float", 0, 1, "primitive"),
            AttrMeta(
                "voltage_regulation_status", "voltageRegulationStatus", "bool", 0, 1, "primitive"
            ),
            AttrMeta("step_position", "stepPosition", "int", 0, 1, "primitive"),
        ),
        ends=(mkt_shunt_compensator.meta,),
    )

    def __init__(
        self,
        *,
        m_var_injection: float | None = None,
        connection_status: int | None = None,
        desired_voltage: float | None = None,
        voltage_regulation_status: bool | None = None,
        step_position: int | None = None,
        mkt_shunt_compensator: MktShuntCompensator | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.m_var_injection = m_var_injection
        self.connection_status = connection_status
        self.desired_voltage = desired_voltage
        self.voltage_regulation_status = voltage_regulation_status
        self.step_position = step_position
        if mkt_shunt_compensator is not None:
            self.mkt_shunt_compensator = mkt_shunt_compensator

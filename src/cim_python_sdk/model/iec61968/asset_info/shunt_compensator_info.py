"""CIM class ShuntCompensatorInfo (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_wires_ext.shunt_compensator_control import (
        ShuntCompensatorControl,
    )


class ShuntCompensatorInfo(AssetInfo):
    """Properties of shunt capacitor, shunt reactor or switchable bank of shunt capacitor or
    reactor assets."""

    __slots__ = (
        "_shunt_compensator_control",
        "max_power_loss",
        "rated_current",
        "rated_reactive_power",
        "rated_voltage",
    )

    rated_voltage: float | None  # Voltage
    rated_current: float | None  # CurrentFlow
    rated_reactive_power: float | None  # ReactivePower
    max_power_loss: float | None  # ApparentPower

    shunt_compensator_control: One[ShuntCompensatorControl] = One(
        EndMeta(
            name="shunt_compensator_control",
            cim_role="ShuntCompensatorControl",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_wires_ext.shunt_compensator_control:ShuntCompensatorControl",
            many=False,
            lower=0,
            upper=1,
            inverse="shunt_compensator_info",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ShuntCompensatorInfo",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{3E9CFB82-B958-4601-9FE4-F334F40FA838}",
        attributes=(
            AttrMeta("rated_voltage", "ratedVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("rated_current", "ratedCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta(
                "rated_reactive_power", "ratedReactivePower", "ReactivePower", 0, 1, "cimdatatype"
            ),
            AttrMeta("max_power_loss", "maxPowerLoss", "ApparentPower", 0, 1, "cimdatatype"),
        ),
        ends=(shunt_compensator_control.meta,),
    )

    def __init__(
        self,
        *,
        rated_voltage: float | None = None,
        rated_current: float | None = None,
        rated_reactive_power: float | None = None,
        max_power_loss: float | None = None,
        shunt_compensator_control: ShuntCompensatorControl | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rated_voltage = rated_voltage
        self.rated_current = rated_current
        self.rated_reactive_power = rated_reactive_power
        self.max_power_loss = max_power_loss
        if shunt_compensator_control is not None:
            self.shunt_compensator_control = shunt_compensator_control

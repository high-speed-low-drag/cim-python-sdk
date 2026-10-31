"""CIM class RatioTapChanger (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.tap_changer import TapChanger

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.ratio_tap_changer_table import (
        RatioTapChangerTable,
    )
    from cim_python_sdk.model.iec61970.base.wires.transformer_control_mode import (
        TransformerControlMode,
    )
    from cim_python_sdk.model.iec61970.base.wires.transformer_end import TransformerEnd


class RatioTapChanger(TapChanger):
    """A tap changer that changes the voltage ratio impacting the voltage magnitude but not the
    phase angle across the transformer.

    Angle sign convention (general): Positive value indicates a positive phase shift from
    the winding where the tap is located to the other winding (for a two-winding
    transformer)."""

    __slots__ = (
        "_ratio_tap_changer_table",
        "_transformer_end",
        "step_voltage_increment",
        "tcul_control_mode",
    )

    step_voltage_increment: float | None  # PerCent
    tcul_control_mode: TransformerControlMode | None

    ratio_tap_changer_table: One[RatioTapChangerTable] = One(
        EndMeta(
            name="ratio_tap_changer_table",
            cim_role="RatioTapChangerTable",
            target="cim_python_sdk.model.iec61970.base.wires.ratio_tap_changer_table:RatioTapChangerTable",
            many=False,
            lower=0,
            upper=1,
            inverse="ratio_tap_changer",
            aggregation="none",
        )
    )
    transformer_end: One[TransformerEnd] = One(
        EndMeta(
            name="transformer_end",
            cim_role="TransformerEnd",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_end:TransformerEnd",
            many=False,
            lower=1,
            upper=1,
            inverse="ratio_tap_changer",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RatioTapChanger",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{09909286-00A6-451c-B420-2E52ABEB2667}",
        attributes=(
            AttrMeta(
                "step_voltage_increment", "stepVoltageIncrement", "PerCent", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "tcul_control_mode",
                "tculControlMode",
                "TransformerControlMode",
                0,
                1,
                "enumeration",
                deprecated=True,
            ),
        ),
        ends=(
            ratio_tap_changer_table.meta,
            transformer_end.meta,
        ),
    )

    def __init__(
        self,
        *,
        step_voltage_increment: float | None = None,
        tcul_control_mode: TransformerControlMode | None = None,
        ratio_tap_changer_table: RatioTapChangerTable | None = None,
        transformer_end: TransformerEnd | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.step_voltage_increment = step_voltage_increment
        self.tcul_control_mode = tcul_control_mode
        if ratio_tap_changer_table is not None:
            self.ratio_tap_changer_table = ratio_tap_changer_table
        if transformer_end is not None:
            self.transformer_end = transformer_end

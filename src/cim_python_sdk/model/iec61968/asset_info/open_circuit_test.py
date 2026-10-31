"""CIM class OpenCircuitTest (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.asset_info.transformer_test import TransformerTest

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.asset_info.transformer_end_info import TransformerEndInfo


class OpenCircuitTest(TransformerTest):
    """Open-circuit test results verify winding turn ratios and phase shifts. They include
    induced voltage and phase shift measurements on open-circuit windings, with voltage
    applied to the energised end. For three-phase windings, the excitation can be a positive
    sequence (the default) or a zero sequence."""

    __slots__ = (
        "_energised_end",
        "_open_end",
        "energised_end_step",
        "energised_end_voltage",
        "open_end_step",
        "open_end_voltage",
        "phase_shift",
    )

    energised_end_step: int | None
    open_end_step: int | None
    energised_end_voltage: float | None  # Voltage
    open_end_voltage: float | None  # Voltage
    phase_shift: float | None  # AngleDegrees

    energised_end: One[TransformerEndInfo] = One(
        EndMeta(
            name="energised_end",
            cim_role="EnergisedEnd",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_end_info:TransformerEndInfo",
            many=False,
            lower=1,
            upper=1,
            inverse="energised_end_open_circuit_tests",
            aggregation="none",
        )
    )
    open_end: One[TransformerEndInfo] = One(
        EndMeta(
            name="open_end",
            cim_role="OpenEnd",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_end_info:TransformerEndInfo",
            many=False,
            lower=1,
            upper=1,
            inverse="open_end_open_circuit_tests",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OpenCircuitTest",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{9D68E211-F604-4c71-BC1C-0F6D43E2F882}",
        attributes=(
            AttrMeta("energised_end_step", "energisedEndStep", "int", 0, 1, "primitive"),
            AttrMeta("open_end_step", "openEndStep", "int", 0, 1, "primitive"),
            AttrMeta(
                "energised_end_voltage", "energisedEndVoltage", "Voltage", 0, 1, "cimdatatype"
            ),
            AttrMeta("open_end_voltage", "openEndVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("phase_shift", "phaseShift", "AngleDegrees", 0, 1, "cimdatatype"),
        ),
        ends=(
            energised_end.meta,
            open_end.meta,
        ),
    )

    def __init__(
        self,
        *,
        energised_end_step: int | None = None,
        open_end_step: int | None = None,
        energised_end_voltage: float | None = None,
        open_end_voltage: float | None = None,
        phase_shift: float | None = None,
        energised_end: TransformerEndInfo | None = None,
        open_end: TransformerEndInfo | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.energised_end_step = energised_end_step
        self.open_end_step = open_end_step
        self.energised_end_voltage = energised_end_voltage
        self.open_end_voltage = open_end_voltage
        self.phase_shift = phase_shift
        if energised_end is not None:
            self.energised_end = energised_end
        if open_end is not None:
            self.open_end = open_end

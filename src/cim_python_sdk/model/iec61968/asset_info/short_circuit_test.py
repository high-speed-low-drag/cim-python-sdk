"""CIM class ShortCircuitTest (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.asset_info.transformer_test import TransformerTest

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.transformer_end_info import TransformerEndInfo


class ShortCircuitTest(TransformerTest):
    """Short-circuit test results determine mesh impedance parameters. They include load losses
    and leakage impedances. For three-phase windings, the excitation can be a positive
    sequence (the default) or a zero sequence. There shall be at least one grounded winding."""

    __slots__ = (
        "_energised_end",
        "_grounded_ends",
        "current",
        "energised_end_step",
        "grounded_end_step",
        "leakage_impedance",
        "leakage_impedance_zero",
        "loss",
        "loss_zero",
        "power",
        "voltage",
    )

    energised_end_step: int | None
    grounded_end_step: int | None
    leakage_impedance: float | None  # Impedance
    leakage_impedance_zero: float | None  # Impedance
    loss: float | None  # KiloActivePower
    loss_zero: float | None  # KiloActivePower
    voltage: float | None  # PerCent
    current: float | None  # CurrentFlow
    power: float | None  # ApparentPower

    energised_end: One[TransformerEndInfo] = One(
        EndMeta(
            name="energised_end",
            cim_role="EnergisedEnd",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_end_info:TransformerEndInfo",
            many=False,
            lower=1,
            upper=1,
            inverse="energised_end_short_circuit_tests",
            aggregation="none",
        )
    )
    grounded_ends: Many[TransformerEndInfo] = Many(
        EndMeta(
            name="grounded_ends",
            cim_role="GroundedEnds",
            target="cim_python_sdk.model.iec61968.asset_info.transformer_end_info:TransformerEndInfo",
            many=True,
            lower=1,
            upper=None,
            inverse="grounded_end_short_circuit_tests",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ShortCircuitTest",
        package="TC57CIM/IEC61968/AssetInfo",
        guid="{B753F4F1-9D09-406e-990B-790FC16EFA5A}",
        attributes=(
            AttrMeta("energised_end_step", "energisedEndStep", "int", 0, 1, "primitive"),
            AttrMeta("grounded_end_step", "groundedEndStep", "int", 0, 1, "primitive"),
            AttrMeta("leakage_impedance", "leakageImpedance", "Impedance", 0, 1, "cimdatatype"),
            AttrMeta(
                "leakage_impedance_zero", "leakageImpedanceZero", "Impedance", 0, 1, "cimdatatype"
            ),
            AttrMeta("loss", "loss", "KiloActivePower", 0, 1, "cimdatatype"),
            AttrMeta("loss_zero", "lossZero", "KiloActivePower", 0, 1, "cimdatatype"),
            AttrMeta("voltage", "voltage", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("current", "current", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("power", "power", "ApparentPower", 0, 1, "cimdatatype"),
        ),
        ends=(
            energised_end.meta,
            grounded_ends.meta,
        ),
    )

    def __init__(
        self,
        *,
        energised_end_step: int | None = None,
        grounded_end_step: int | None = None,
        leakage_impedance: float | None = None,
        leakage_impedance_zero: float | None = None,
        loss: float | None = None,
        loss_zero: float | None = None,
        voltage: float | None = None,
        current: float | None = None,
        power: float | None = None,
        energised_end: TransformerEndInfo | None = None,
        grounded_ends: Iterable[TransformerEndInfo] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.energised_end_step = energised_end_step
        self.grounded_end_step = grounded_end_step
        self.leakage_impedance = leakage_impedance
        self.leakage_impedance_zero = leakage_impedance_zero
        self.loss = loss
        self.loss_zero = loss_zero
        self.voltage = voltage
        self.current = current
        self.power = power
        if energised_end is not None:
            self.energised_end = energised_end
        if grounded_ends is not None:
            ShortCircuitTest.grounded_ends.extend(self, grounded_ends)

    def add_grounded_end(self, grounded_end: TransformerEndInfo) -> Self:
        return ShortCircuitTest.grounded_ends.add(self, grounded_end)

    def remove_grounded_end(self, grounded_end: TransformerEndInfo) -> Self:
        return ShortCircuitTest.grounded_ends.remove(self, grounded_end)

    def clear_grounded_ends(self) -> Self:
        return ShortCircuitTest.grounded_ends.clear(self)

    def num_grounded_end(self) -> int:
        return ShortCircuitTest.grounded_ends.count(self)

    def get_grounded_end_by_mrid(self, mrid: str) -> TransformerEndInfo | None:
        return ShortCircuitTest.grounded_ends.get_by_mrid(self, mrid)

"""CIM class ACLineSegment (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.wires.conductor import Conductor

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_info.wire_spacing_info import WireSpacingInfo
    from cim_python_sdk.model.iec61968.operations.ground_action import GroundAction
    from cim_python_sdk.model.iec61968.operations.jumper_action import JumperAction
    from cim_python_sdk.model.iec61970.base.faults.line_fault import LineFault
    from cim_python_sdk.model.iec61970.base.wires.ac_line_segment_phase import ACLineSegmentPhase
    from cim_python_sdk.model.iec61970.base.wires.clamp import Clamp
    from cim_python_sdk.model.iec61970.base.wires.cut import Cut
    from cim_python_sdk.model.iec61970.base.wires.per_length_impedance import PerLengthImpedance


class ACLineSegment(Conductor):
    """A wire or combination of wires, with consistent electrical characteristics, building a
    single electrical system, used to carry alternating current between points in the power
    system.

    For symmetrical, transposed three phase lines, it is sufficient to use attributes of the
    line segment, which describe impedances and admittances for the entire length of the
    segment. Additionally impedances can be computed by using length and associated per
    length impedances.

    The BaseVoltage at the two ends of ACLineSegments in a Line shall have the same
    BaseVoltage.nominalVoltage. However, boundary lines may have slightly different
    BaseVoltage.nominalVoltages and variation is allowed. Larger voltage difference in
    general requires use of an equivalent branch."""

    __slots__ = (
        "_ac_line_segment_phases",
        "_clamp",
        "_cut",
        "_line_faults",
        "_line_grounding_action",
        "_line_jumping_action",
        "_per_length_impedance",
        "_wire_spacing_info",
        "b0ch",
        "bch",
        "g0ch",
        "gch",
        "r",
        "r0",
        "short_circuit_end_temperature",
        "x",
        "x0",
    )

    b0ch: float | None  # Susceptance
    bch: float | None  # Susceptance
    g0ch: float | None  # Conductance
    gch: float | None  # Conductance
    r: float | None  # Resistance
    r0: float | None  # Resistance
    short_circuit_end_temperature: float | None  # Temperature
    x: float | None  # Reactance
    x0: float | None  # Reactance

    line_grounding_action: One[GroundAction] = One(
        EndMeta(
            name="line_grounding_action",
            cim_role="LineGroundingAction",
            target="cim_python_sdk.model.iec61968.operations.ground_action:GroundAction",
            many=False,
            lower=0,
            upper=1,
            inverse="along_ac_line_segment",
            aggregation="none",
        )
    )
    clamp: Many[Clamp] = Many(
        EndMeta(
            name="clamp",
            cim_role="Clamp",
            target="cim_python_sdk.model.iec61970.base.wires.clamp:Clamp",
            many=True,
            lower=0,
            upper=None,
            inverse="ac_line_segment",
            aggregation="none",
        )
    )
    ac_line_segment_phases: Many[ACLineSegmentPhase] = Many(
        EndMeta(
            name="ac_line_segment_phases",
            cim_role="ACLineSegmentPhases",
            target="cim_python_sdk.model.iec61970.base.wires.ac_line_segment_phase:ACLineSegmentPhase",
            many=True,
            lower=0,
            upper=None,
            inverse="ac_line_segment",
            aggregation="none",
        )
    )
    cut: Many[Cut] = Many(
        EndMeta(
            name="cut",
            cim_role="Cut",
            target="cim_python_sdk.model.iec61970.base.wires.cut:Cut",
            many=True,
            lower=0,
            upper=None,
            inverse="ac_line_segment",
            aggregation="none",
        )
    )
    per_length_impedance: One[PerLengthImpedance] = One(
        EndMeta(
            name="per_length_impedance",
            cim_role="PerLengthImpedance",
            target="cim_python_sdk.model.iec61970.base.wires.per_length_impedance:PerLengthImpedance",
            many=False,
            lower=0,
            upper=1,
            inverse="ac_line_segments",
            aggregation="none",
        )
    )
    line_jumping_action: One[JumperAction] = One(
        EndMeta(
            name="line_jumping_action",
            cim_role="LineJumpingAction",
            target="cim_python_sdk.model.iec61968.operations.jumper_action:JumperAction",
            many=False,
            lower=0,
            upper=1,
            inverse="ac_line_segments",
            aggregation="none",
        )
    )
    line_faults: Many[LineFault] = Many(
        EndMeta(
            name="line_faults",
            cim_role="LineFaults",
            target="cim_python_sdk.model.iec61970.base.faults.line_fault:LineFault",
            many=True,
            lower=0,
            upper=None,
            inverse="ac_line_segment",
            aggregation="none",
        )
    )
    wire_spacing_info: One[WireSpacingInfo] = One(
        EndMeta(
            name="wire_spacing_info",
            cim_role="WireSpacingInfo",
            target="cim_python_sdk.model.iec61968.asset_info.wire_spacing_info:WireSpacingInfo",
            many=False,
            lower=0,
            upper=1,
            inverse="ac_line_segment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ACLineSegment",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{625BD764-3907-4d65-8497-7FD09708BD8E}",
        attributes=(
            AttrMeta("b0ch", "b0ch", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("bch", "bch", "Susceptance", 0, 1, "cimdatatype"),
            AttrMeta("g0ch", "g0ch", "Conductance", 0, 1, "cimdatatype"),
            AttrMeta("gch", "gch", "Conductance", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("r0", "r0", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta(
                "short_circuit_end_temperature",
                "shortCircuitEndTemperature",
                "Temperature",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("x", "x", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("x0", "x0", "Reactance", 0, 1, "cimdatatype"),
        ),
        ends=(
            line_grounding_action.meta,
            clamp.meta,
            ac_line_segment_phases.meta,
            cut.meta,
            per_length_impedance.meta,
            line_jumping_action.meta,
            line_faults.meta,
            wire_spacing_info.meta,
        ),
    )

    def __init__(
        self,
        *,
        b0ch: float | None = None,
        bch: float | None = None,
        g0ch: float | None = None,
        gch: float | None = None,
        r: float | None = None,
        r0: float | None = None,
        short_circuit_end_temperature: float | None = None,
        x: float | None = None,
        x0: float | None = None,
        line_grounding_action: GroundAction | None = None,
        clamp: Iterable[Clamp] | None = None,
        ac_line_segment_phases: Iterable[ACLineSegmentPhase] | None = None,
        cut: Iterable[Cut] | None = None,
        per_length_impedance: PerLengthImpedance | None = None,
        line_jumping_action: JumperAction | None = None,
        line_faults: Iterable[LineFault] | None = None,
        wire_spacing_info: WireSpacingInfo | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b0ch = b0ch
        self.bch = bch
        self.g0ch = g0ch
        self.gch = gch
        self.r = r
        self.r0 = r0
        self.short_circuit_end_temperature = short_circuit_end_temperature
        self.x = x
        self.x0 = x0
        if line_grounding_action is not None:
            self.line_grounding_action = line_grounding_action
        if clamp is not None:
            ACLineSegment.clamp.extend(self, clamp)
        if ac_line_segment_phases is not None:
            ACLineSegment.ac_line_segment_phases.extend(self, ac_line_segment_phases)
        if cut is not None:
            ACLineSegment.cut.extend(self, cut)
        if per_length_impedance is not None:
            self.per_length_impedance = per_length_impedance
        if line_jumping_action is not None:
            self.line_jumping_action = line_jumping_action
        if line_faults is not None:
            ACLineSegment.line_faults.extend(self, line_faults)
        if wire_spacing_info is not None:
            self.wire_spacing_info = wire_spacing_info

    def add_clamp(self, clamp: Clamp) -> Self:
        return ACLineSegment.clamp.add(self, clamp)

    def remove_clamp(self, clamp: Clamp) -> Self:
        return ACLineSegment.clamp.remove(self, clamp)

    def clear_clamp(self) -> Self:
        return ACLineSegment.clamp.clear(self)

    def num_clamp(self) -> int:
        return ACLineSegment.clamp.count(self)

    def get_clamp_by_mrid(self, mrid: str) -> Clamp | None:
        return ACLineSegment.clamp.get_by_mrid(self, mrid)

    def add_ac_line_segment_phase(self, ac_line_segment_phase: ACLineSegmentPhase) -> Self:
        return ACLineSegment.ac_line_segment_phases.add(self, ac_line_segment_phase)

    def remove_ac_line_segment_phase(self, ac_line_segment_phase: ACLineSegmentPhase) -> Self:
        return ACLineSegment.ac_line_segment_phases.remove(self, ac_line_segment_phase)

    def clear_ac_line_segment_phases(self) -> Self:
        return ACLineSegment.ac_line_segment_phases.clear(self)

    def num_ac_line_segment_phase(self) -> int:
        return ACLineSegment.ac_line_segment_phases.count(self)

    def get_ac_line_segment_phase_by_mrid(self, mrid: str) -> ACLineSegmentPhase | None:
        return ACLineSegment.ac_line_segment_phases.get_by_mrid(self, mrid)

    def add_cut(self, cut: Cut) -> Self:
        return ACLineSegment.cut.add(self, cut)

    def remove_cut(self, cut: Cut) -> Self:
        return ACLineSegment.cut.remove(self, cut)

    def clear_cut(self) -> Self:
        return ACLineSegment.cut.clear(self)

    def num_cut(self) -> int:
        return ACLineSegment.cut.count(self)

    def get_cut_by_mrid(self, mrid: str) -> Cut | None:
        return ACLineSegment.cut.get_by_mrid(self, mrid)

    def add_line_fault(self, line_fault: LineFault) -> Self:
        return ACLineSegment.line_faults.add(self, line_fault)

    def remove_line_fault(self, line_fault: LineFault) -> Self:
        return ACLineSegment.line_faults.remove(self, line_fault)

    def clear_line_faults(self) -> Self:
        return ACLineSegment.line_faults.clear(self)

    def num_line_fault(self) -> int:
        return ACLineSegment.line_faults.count(self)

    def get_line_fault_by_mrid(self, mrid: str) -> LineFault | None:
        return ACLineSegment.line_faults.get_by_mrid(self, mrid)

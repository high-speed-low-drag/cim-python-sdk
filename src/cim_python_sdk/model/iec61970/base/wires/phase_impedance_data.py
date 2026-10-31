"""CIM class PhaseImpedanceData (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.per_length_phase_impedance import (
        PerLengthPhaseImpedance,
    )
    from cim_python_sdk.model.iec61970.base.wires.single_phase_kind import SinglePhaseKind


class PhaseImpedanceData(CimObject):
    """Impedance and conductance matrix element values.

    The diagonal elements are described by the elements having the same toPhase and
    fromPhase value and the off diagonal elements have different toPhase and fromPhase
    values. The matrix can also be stored in symmetric lower triangular format using the row
    and column attributes, which map to ACLineSegmentPhase.sequenceNumber."""

    __slots__ = ("_phase_impedance", "b", "column", "from_phase", "g", "r", "row", "to_phase", "x")

    b: float | None  # SusceptancePerLength
    r: float | None  # ResistancePerLength
    g: float | None  # ConductancePerLength
    x: float | None  # ReactancePerLength
    from_phase: SinglePhaseKind | None
    to_phase: SinglePhaseKind | None
    row: int | None
    column: int | None

    phase_impedance: One[PerLengthPhaseImpedance] = One(
        EndMeta(
            name="phase_impedance",
            cim_role="PhaseImpedance",
            target="cim_python_sdk.model.iec61970.base.wires.per_length_phase_impedance:PerLengthPhaseImpedance",
            many=False,
            lower=1,
            upper=1,
            inverse="phase_impedance_data",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PhaseImpedanceData",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{8D8D03C8-6278-4397-9EFA-EDC98D359BBC}",
        attributes=(
            AttrMeta("b", "b", "SusceptancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("r", "r", "ResistancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("g", "g", "ConductancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("x", "x", "ReactancePerLength", 0, 1, "cimdatatype"),
            AttrMeta("from_phase", "fromPhase", "SinglePhaseKind", 0, 1, "enumeration"),
            AttrMeta("to_phase", "toPhase", "SinglePhaseKind", 0, 1, "enumeration"),
            AttrMeta("row", "row", "int", 0, 1, "primitive"),
            AttrMeta("column", "column", "int", 0, 1, "primitive"),
        ),
        ends=(phase_impedance.meta,),
    )

    def __init__(
        self,
        *,
        b: float | None = None,
        r: float | None = None,
        g: float | None = None,
        x: float | None = None,
        from_phase: SinglePhaseKind | None = None,
        to_phase: SinglePhaseKind | None = None,
        row: int | None = None,
        column: int | None = None,
        phase_impedance: PerLengthPhaseImpedance | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.b = b
        self.r = r
        self.g = g
        self.x = x
        self.from_phase = from_phase
        self.to_phase = to_phase
        self.row = row
        self.column = column
        if phase_impedance is not None:
            self.phase_impedance = phase_impedance

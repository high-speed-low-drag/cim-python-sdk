"""CIM class PhaseTapChangerTablePoint (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.tap_changer_table_point import TapChangerTablePoint

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.phase_tap_changer_table import (
        PhaseTapChangerTable,
    )


class PhaseTapChangerTablePoint(TapChangerTablePoint):
    """Describes each tap step in the phase tap changer tabular curve."""

    __slots__ = ("_phase_tap_changer_table", "angle")

    angle: float | None  # AngleDegrees

    phase_tap_changer_table: One[PhaseTapChangerTable] = One(
        EndMeta(
            name="phase_tap_changer_table",
            cim_role="PhaseTapChangerTable",
            target="cim_python_sdk.model.iec61970.base.wires.phase_tap_changer_table:PhaseTapChangerTable",
            many=False,
            lower=1,
            upper=1,
            inverse="phase_tap_changer_table_point",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PhaseTapChangerTablePoint",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{D2A2282D-3EBD-47ea-8339-B78FEC97977F}",
        attributes=(AttrMeta("angle", "angle", "AngleDegrees", 0, 1, "cimdatatype"),),
        ends=(phase_tap_changer_table.meta,),
    )

    def __init__(
        self,
        *,
        angle: float | None = None,
        phase_tap_changer_table: PhaseTapChangerTable | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.angle = angle
        if phase_tap_changer_table is not None:
            self.phase_tap_changer_table = phase_tap_changer_table

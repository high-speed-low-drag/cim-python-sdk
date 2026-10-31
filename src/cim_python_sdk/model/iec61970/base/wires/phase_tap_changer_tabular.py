"""CIM class PhaseTapChangerTabular (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.phase_tap_changer import PhaseTapChanger

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.phase_tap_changer_table import (
        PhaseTapChangerTable,
    )


class PhaseTapChangerTabular(PhaseTapChanger):
    """Describes a tap changer with a table defining the relation between the tap step and the
    phase angle difference across the transformer."""

    __slots__ = ("_phase_tap_changer_table",)

    phase_tap_changer_table: One[PhaseTapChangerTable] = One(
        EndMeta(
            name="phase_tap_changer_table",
            cim_role="PhaseTapChangerTable",
            target="cim_python_sdk.model.iec61970.base.wires.phase_tap_changer_table:PhaseTapChangerTable",
            many=False,
            lower=0,
            upper=1,
            inverse="phase_tap_changer_tabular",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PhaseTapChangerTabular",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{27778291-3EC1-429b-AD1C-2E9841406540}",
        ends=(phase_tap_changer_table.meta,),
    )

    def __init__(
        self,
        *,
        phase_tap_changer_table: PhaseTapChangerTable | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if phase_tap_changer_table is not None:
            self.phase_tap_changer_table = phase_tap_changer_table

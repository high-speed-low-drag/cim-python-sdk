"""CIM class PhaseTapChangerTable (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.phase_tap_changer_table_point import (
        PhaseTapChangerTablePoint,
    )
    from cim_python_sdk.model.iec61970.base.wires.phase_tap_changer_tabular import (
        PhaseTapChangerTabular,
    )


class PhaseTapChangerTable(IdentifiedObject):
    """Describes a tabular curve for how the phase angle difference and impedance varies with
    the tap step."""

    __slots__ = ("_phase_tap_changer_table_point", "_phase_tap_changer_tabular")

    phase_tap_changer_table_point: Many[PhaseTapChangerTablePoint] = Many(
        EndMeta(
            name="phase_tap_changer_table_point",
            cim_role="PhaseTapChangerTablePoint",
            target="cim_python_sdk.model.iec61970.base.wires.phase_tap_changer_table_point:PhaseTapChangerTablePoint",
            many=True,
            lower=1,
            upper=None,
            inverse="phase_tap_changer_table",
            aggregation="none",
        )
    )
    phase_tap_changer_tabular: Many[PhaseTapChangerTabular] = Many(
        EndMeta(
            name="phase_tap_changer_tabular",
            cim_role="PhaseTapChangerTabular",
            target="cim_python_sdk.model.iec61970.base.wires.phase_tap_changer_tabular:PhaseTapChangerTabular",
            many=True,
            lower=0,
            upper=None,
            inverse="phase_tap_changer_table",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PhaseTapChangerTable",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{350A69CE-A6C9-4967-9BB9-7BF7A361B5C8}",
        ends=(
            phase_tap_changer_table_point.meta,
            phase_tap_changer_tabular.meta,
        ),
    )

    def __init__(
        self,
        *,
        phase_tap_changer_table_point: Iterable[PhaseTapChangerTablePoint] | None = None,
        phase_tap_changer_tabular: Iterable[PhaseTapChangerTabular] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if phase_tap_changer_table_point is not None:
            PhaseTapChangerTable.phase_tap_changer_table_point.extend(
                self, phase_tap_changer_table_point
            )
        if phase_tap_changer_tabular is not None:
            PhaseTapChangerTable.phase_tap_changer_tabular.extend(self, phase_tap_changer_tabular)

    def add_phase_tap_changer_table_point(
        self, phase_tap_changer_table_point: PhaseTapChangerTablePoint
    ) -> Self:
        return PhaseTapChangerTable.phase_tap_changer_table_point.add(
            self, phase_tap_changer_table_point
        )

    def remove_phase_tap_changer_table_point(
        self, phase_tap_changer_table_point: PhaseTapChangerTablePoint
    ) -> Self:
        return PhaseTapChangerTable.phase_tap_changer_table_point.remove(
            self, phase_tap_changer_table_point
        )

    def clear_phase_tap_changer_table_point(self) -> Self:
        return PhaseTapChangerTable.phase_tap_changer_table_point.clear(self)

    def num_phase_tap_changer_table_point(self) -> int:
        return PhaseTapChangerTable.phase_tap_changer_table_point.count(self)

    def add_phase_tap_changer_tabular(
        self, phase_tap_changer_tabular: PhaseTapChangerTabular
    ) -> Self:
        return PhaseTapChangerTable.phase_tap_changer_tabular.add(self, phase_tap_changer_tabular)

    def remove_phase_tap_changer_tabular(
        self, phase_tap_changer_tabular: PhaseTapChangerTabular
    ) -> Self:
        return PhaseTapChangerTable.phase_tap_changer_tabular.remove(
            self, phase_tap_changer_tabular
        )

    def clear_phase_tap_changer_tabular(self) -> Self:
        return PhaseTapChangerTable.phase_tap_changer_tabular.clear(self)

    def num_phase_tap_changer_tabular(self) -> int:
        return PhaseTapChangerTable.phase_tap_changer_tabular.count(self)

    def get_phase_tap_changer_tabular_by_mrid(self, mrid: str) -> PhaseTapChangerTabular | None:
        return PhaseTapChangerTable.phase_tap_changer_tabular.get_by_mrid(self, mrid)

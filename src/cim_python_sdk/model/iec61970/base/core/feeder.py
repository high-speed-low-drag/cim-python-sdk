"""CIM class Feeder (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.equipment_container import EquipmentContainer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.substation import Substation
    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal


class Feeder(EquipmentContainer):
    """A collection of equipment for organizational purposes, used for grouping distribution
    resources.

    The organization a feeder does not necessarily reflect connectivity or current operation
    state."""

    __slots__ = (
        "_naming_secondary_substation",
        "_normal_energized_substation",
        "_normal_energizing_substation",
        "_normal_head_terminal",
    )

    normal_energized_substation: Many[Substation] = Many(
        EndMeta(
            name="normal_energized_substation",
            cim_role="NormalEnergizedSubstation",
            target="cim_python_sdk.model.iec61970.base.core.substation:Substation",
            many=True,
            lower=0,
            upper=None,
            inverse="normal_energizing_feeder",
            aggregation="none",
        )
    )
    normal_head_terminal: Many[Terminal] = Many(
        EndMeta(
            name="normal_head_terminal",
            cim_role="NormalHeadTerminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=True,
            lower=1,
            upper=None,
            inverse="normal_head_feeder",
            aggregation="none",
        )
    )
    naming_secondary_substation: Many[Substation] = Many(
        EndMeta(
            name="naming_secondary_substation",
            cim_role="NamingSecondarySubstation",
            target="cim_python_sdk.model.iec61970.base.core.substation:Substation",
            many=True,
            lower=0,
            upper=None,
            inverse="naming_feeder",
            aggregation="shared",
        )
    )
    normal_energizing_substation: One[Substation] = One(
        EndMeta(
            name="normal_energizing_substation",
            cim_role="NormalEnergizingSubstation",
            target="cim_python_sdk.model.iec61970.base.core.substation:Substation",
            many=False,
            lower=0,
            upper=1,
            inverse="normal_energized_feeder",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Feeder",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{FE6F802E-8B23-470b-B678-A29A27235CA8}",
        ends=(
            normal_energized_substation.meta,
            normal_head_terminal.meta,
            naming_secondary_substation.meta,
            normal_energizing_substation.meta,
        ),
    )

    def __init__(
        self,
        *,
        normal_energized_substation: Iterable[Substation] | None = None,
        normal_head_terminal: Iterable[Terminal] | None = None,
        naming_secondary_substation: Iterable[Substation] | None = None,
        normal_energizing_substation: Substation | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if normal_energized_substation is not None:
            Feeder.normal_energized_substation.extend(self, normal_energized_substation)
        if normal_head_terminal is not None:
            Feeder.normal_head_terminal.extend(self, normal_head_terminal)
        if naming_secondary_substation is not None:
            Feeder.naming_secondary_substation.extend(self, naming_secondary_substation)
        if normal_energizing_substation is not None:
            self.normal_energizing_substation = normal_energizing_substation

    def add_normal_energized_substation(self, normal_energized_substation: Substation) -> Self:
        return Feeder.normal_energized_substation.add(self, normal_energized_substation)

    def remove_normal_energized_substation(self, normal_energized_substation: Substation) -> Self:
        return Feeder.normal_energized_substation.remove(self, normal_energized_substation)

    def clear_normal_energized_substation(self) -> Self:
        return Feeder.normal_energized_substation.clear(self)

    def num_normal_energized_substation(self) -> int:
        return Feeder.normal_energized_substation.count(self)

    def get_normal_energized_substation_by_mrid(self, mrid: str) -> Substation | None:
        return Feeder.normal_energized_substation.get_by_mrid(self, mrid)

    def add_normal_head_terminal(self, normal_head_terminal: Terminal) -> Self:
        return Feeder.normal_head_terminal.add(self, normal_head_terminal)

    def remove_normal_head_terminal(self, normal_head_terminal: Terminal) -> Self:
        return Feeder.normal_head_terminal.remove(self, normal_head_terminal)

    def clear_normal_head_terminal(self) -> Self:
        return Feeder.normal_head_terminal.clear(self)

    def num_normal_head_terminal(self) -> int:
        return Feeder.normal_head_terminal.count(self)

    def get_normal_head_terminal_by_mrid(self, mrid: str) -> Terminal | None:
        return Feeder.normal_head_terminal.get_by_mrid(self, mrid)

    def add_naming_secondary_substation(self, naming_secondary_substation: Substation) -> Self:
        return Feeder.naming_secondary_substation.add(self, naming_secondary_substation)

    def remove_naming_secondary_substation(self, naming_secondary_substation: Substation) -> Self:
        return Feeder.naming_secondary_substation.remove(self, naming_secondary_substation)

    def clear_naming_secondary_substation(self) -> Self:
        return Feeder.naming_secondary_substation.clear(self)

    def num_naming_secondary_substation(self) -> int:
        return Feeder.naming_secondary_substation.count(self)

    def get_naming_secondary_substation_by_mrid(self, mrid: str) -> Substation | None:
        return Feeder.naming_secondary_substation.get_by_mrid(self, mrid)

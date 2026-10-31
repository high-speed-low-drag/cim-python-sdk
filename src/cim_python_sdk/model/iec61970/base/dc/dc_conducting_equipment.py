"""CIM class DCConductingEquipment (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.equipment import Equipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.dc.dc_terminal import DCTerminal
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_adjustment import (
        ProtectiveActionAdjustment,
    )


class DCConductingEquipment(Equipment):
    """The parts of the DC power system that are designed to carry current or that are
    conductively connected through DC terminals."""

    __slots__ = ("_dc_terminals", "_protective_action_adjustment", "rated_udc")

    rated_udc: float | None  # Voltage

    dc_terminals: Many[DCTerminal] = Many(
        EndMeta(
            name="dc_terminals",
            cim_role="DCTerminals",
            target="cim_python_sdk.model.iec61970.base.dc.dc_terminal:DCTerminal",
            many=True,
            lower=0,
            upper=None,
            inverse="dc_conducting_equipment",
            aggregation="none",
        )
    )
    protective_action_adjustment: Many[ProtectiveActionAdjustment] = Many(
        EndMeta(
            name="protective_action_adjustment",
            cim_role="ProtectiveActionAdjustment",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action_adjustment:ProtectiveActionAdjustment",
            many=True,
            lower=0,
            upper=None,
            inverse="dc_conducting_equipment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DCConductingEquipment",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{2D8739A1-0186-49f3-8C35-04EDE046E614}",
        attributes=(AttrMeta("rated_udc", "ratedUdc", "Voltage", 0, 1, "cimdatatype"),),
        ends=(
            dc_terminals.meta,
            protective_action_adjustment.meta,
        ),
    )

    def __init__(
        self,
        *,
        rated_udc: float | None = None,
        dc_terminals: Iterable[DCTerminal] | None = None,
        protective_action_adjustment: Iterable[ProtectiveActionAdjustment] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rated_udc = rated_udc
        if dc_terminals is not None:
            DCConductingEquipment.dc_terminals.extend(self, dc_terminals)
        if protective_action_adjustment is not None:
            DCConductingEquipment.protective_action_adjustment.extend(
                self, protective_action_adjustment
            )

    def add_dc_terminal(self, dc_terminal: DCTerminal) -> Self:
        return DCConductingEquipment.dc_terminals.add(self, dc_terminal)

    def remove_dc_terminal(self, dc_terminal: DCTerminal) -> Self:
        return DCConductingEquipment.dc_terminals.remove(self, dc_terminal)

    def clear_dc_terminals(self) -> Self:
        return DCConductingEquipment.dc_terminals.clear(self)

    def num_dc_terminal(self) -> int:
        return DCConductingEquipment.dc_terminals.count(self)

    def get_dc_terminal_by_mrid(self, mrid: str) -> DCTerminal | None:
        return DCConductingEquipment.dc_terminals.get_by_mrid(self, mrid)

    def add_protective_action_adjustment(
        self, protective_action_adjustment: ProtectiveActionAdjustment
    ) -> Self:
        return DCConductingEquipment.protective_action_adjustment.add(
            self, protective_action_adjustment
        )

    def remove_protective_action_adjustment(
        self, protective_action_adjustment: ProtectiveActionAdjustment
    ) -> Self:
        return DCConductingEquipment.protective_action_adjustment.remove(
            self, protective_action_adjustment
        )

    def clear_protective_action_adjustment(self) -> Self:
        return DCConductingEquipment.protective_action_adjustment.clear(self)

    def num_protective_action_adjustment(self) -> int:
        return DCConductingEquipment.protective_action_adjustment.count(self)

    def get_protective_action_adjustment_by_mrid(
        self, mrid: str
    ) -> ProtectiveActionAdjustment | None:
        return DCConductingEquipment.protective_action_adjustment.get_by_mrid(self, mrid)

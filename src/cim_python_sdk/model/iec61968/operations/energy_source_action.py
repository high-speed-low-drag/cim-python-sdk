"""CIM class EnergySourceAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.temp_equip_action_kind import TempEquipActionKind
    from cim_python_sdk.model.iec61970.base.wires.energy_source import EnergySource


class EnergySourceAction(SwitchingAction):
    """Action on energy source as a switching step."""

    __slots__ = ("_energy_source", "kind")

    kind: TempEquipActionKind | None

    energy_source: One[EnergySource] = One(
        EndMeta(
            name="energy_source",
            cim_role="EnergySource",
            target="cim_python_sdk.model.iec61970.base.wires.energy_source:EnergySource",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_source_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergySourceAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{6E3EDC0D-EE7D-4e40-89BC-859964F2834C}",
        attributes=(AttrMeta("kind", "kind", "TempEquipActionKind", 0, 1, "enumeration"),),
        ends=(energy_source.meta,),
    )

    def __init__(
        self,
        *,
        kind: TempEquipActionKind | None = None,
        energy_source: EnergySource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if energy_source is not None:
            self.energy_source = energy_source

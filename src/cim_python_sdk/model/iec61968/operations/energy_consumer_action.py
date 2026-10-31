"""CIM class EnergyConsumerAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.temp_equip_action_kind import TempEquipActionKind
    from cim_python_sdk.model.iec61970.base.wires.energy_consumer import EnergyConsumer


class EnergyConsumerAction(SwitchingAction):
    """Action to connect or disconnect the Energy Consumer from its Terminal"""

    __slots__ = ("_energy_consumer", "kind")

    kind: TempEquipActionKind | None

    energy_consumer: One[EnergyConsumer] = One(
        EndMeta(
            name="energy_consumer",
            cim_role="EnergyConsumer",
            target="cim_python_sdk.model.iec61970.base.wires.energy_consumer:EnergyConsumer",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_consumer_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnergyConsumerAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{1FCCA0EA-FB27-4e4e-9016-17E451BAAD4B}",
        attributes=(AttrMeta("kind", "kind", "TempEquipActionKind", 0, 1, "enumeration"),),
        ends=(energy_consumer.meta,),
    )

    def __init__(
        self,
        *,
        kind: TempEquipActionKind | None = None,
        energy_consumer: EnergyConsumer | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if energy_consumer is not None:
            self.energy_consumer = energy_consumer

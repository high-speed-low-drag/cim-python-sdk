"""CIM class ConformLoad (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.energy_consumer import EnergyConsumer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.load_model.conform_load_group import ConformLoadGroup


class ConformLoad(EnergyConsumer):
    """ConformLoad represent loads that follow a daily load change pattern where the pattern
    can be used to scale the load with a system load."""

    __slots__ = ("_load_group",)

    load_group: One[ConformLoadGroup] = One(
        EndMeta(
            name="load_group",
            cim_role="LoadGroup",
            target="cim_python_sdk.model.iec61970.base.load_model.conform_load_group:ConformLoadGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_consumers",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConformLoad",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{B47EB000-9FCB-4543-B706-90486C3CBDD9}",
        ends=(load_group.meta,),
    )

    def __init__(
        self,
        *,
        load_group: ConformLoadGroup | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if load_group is not None:
            self.load_group = load_group

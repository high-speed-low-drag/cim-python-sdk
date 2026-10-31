"""CIM class NonConformLoad (TC57CIM/IEC61970/Base/LoadModel). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.energy_consumer import EnergyConsumer

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.load_model.non_conform_load_group import (
        NonConformLoadGroup,
    )


class NonConformLoad(EnergyConsumer):
    """NonConformLoad represents loads that do not follow a daily load change pattern and whose
    changes are not correlated with the daily load change pattern."""

    __slots__ = ("_load_group",)

    load_group: One[NonConformLoadGroup] = One(
        EndMeta(
            name="load_group",
            cim_role="LoadGroup",
            target="cim_python_sdk.model.iec61970.base.load_model.non_conform_load_group:NonConformLoadGroup",
            many=False,
            lower=0,
            upper=1,
            inverse="energy_consumers",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="NonConformLoad",
        package="TC57CIM/IEC61970/Base/LoadModel",
        guid="{E1506289-85CA-4e5b-BD89-6E483BCE1C0F}",
        ends=(load_group.meta,),
    )

    def __init__(
        self,
        *,
        load_group: NonConformLoadGroup | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if load_group is not None:
            self.load_group = load_group

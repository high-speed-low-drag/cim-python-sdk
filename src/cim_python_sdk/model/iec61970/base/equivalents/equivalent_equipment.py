"""CIM class EquivalentEquipment (TC57CIM/IEC61970/Base/Equivalents). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.equivalents.equivalent_network import EquivalentNetwork


class EquivalentEquipment(ConductingEquipment):
    """The class represents equivalent objects that are the result of a network reduction. The
    class is the base for equivalent objects of different types."""

    __slots__ = ("_equivalent_network",)

    equivalent_network: One[EquivalentNetwork] = One(
        EndMeta(
            name="equivalent_network",
            cim_role="EquivalentNetwork",
            target="cim_python_sdk.model.iec61970.base.equivalents.equivalent_network:EquivalentNetwork",
            many=False,
            lower=0,
            upper=1,
            inverse="equivalent_equipments",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EquivalentEquipment",
        package="TC57CIM/IEC61970/Base/Equivalents",
        guid="{966D682F-CD37-4038-9739-3EEC0E6CB044}",
        ends=(equivalent_network.meta,),
    )

    def __init__(
        self,
        *,
        equivalent_network: EquivalentNetwork | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if equivalent_network is not None:
            self.equivalent_network = equivalent_network

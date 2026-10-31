"""CIM class InterrupterUnit (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.assets.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.bushing import Bushing
    from cim_python_sdk.model.iec61968.assets.operating_mechanism import OperatingMechanism


class InterrupterUnit(Asset):
    """Breaker interrupter.

    Some interrupters have one fixed and one moving contact, some have 2 fixed contacts,
    some 2 moving contacts. An interrupter will have relationships with 2 bushings and those
    relationships may be any combination of the FixedContact and MovingContact associations."""

    __slots__ = ("_bushing", "_bushing_fixed_contact", "_operating_mechanism")

    bushing: Many[Bushing] = Many(
        EndMeta(
            name="bushing",
            cim_role="Bushing",
            target="cim_python_sdk.model.iec61968.assets.bushing:Bushing",
            many=True,
            lower=0,
            upper=None,
            inverse="moving_contact",
            aggregation="none",
        )
    )
    bushing_fixed_contact: Many[Bushing] = Many(
        EndMeta(
            name="bushing_fixed_contact",
            cim_role="Bushing",
            target="cim_python_sdk.model.iec61968.assets.bushing:Bushing",
            many=True,
            lower=0,
            upper=None,
            inverse="fixed_contact",
            aggregation="none",
        )
    )
    operating_mechanism: One[OperatingMechanism] = One(
        EndMeta(
            name="operating_mechanism",
            cim_role="OperatingMechanism",
            target="cim_python_sdk.model.iec61968.assets.operating_mechanism:OperatingMechanism",
            many=False,
            lower=0,
            upper=1,
            inverse="interrupter_unit",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InterrupterUnit",
        package="TC57CIM/IEC61968/Assets",
        guid="{18E3DB60-03B9-47df-8914-232FFE326ED5}",
        ends=(
            bushing.meta,
            bushing_fixed_contact.meta,
            operating_mechanism.meta,
        ),
    )

    def __init__(
        self,
        *,
        bushing: Iterable[Bushing] | None = None,
        bushing_fixed_contact: Iterable[Bushing] | None = None,
        operating_mechanism: OperatingMechanism | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if bushing is not None:
            InterrupterUnit.bushing.extend(self, bushing)
        if bushing_fixed_contact is not None:
            InterrupterUnit.bushing_fixed_contact.extend(self, bushing_fixed_contact)
        if operating_mechanism is not None:
            self.operating_mechanism = operating_mechanism

    def add_bushing(self, bushing: Bushing) -> Self:
        return InterrupterUnit.bushing.add(self, bushing)

    def remove_bushing(self, bushing: Bushing) -> Self:
        return InterrupterUnit.bushing.remove(self, bushing)

    def clear_bushing(self) -> Self:
        return InterrupterUnit.bushing.clear(self)

    def num_bushing(self) -> int:
        return InterrupterUnit.bushing.count(self)

    def get_bushing_by_mrid(self, mrid: str) -> Bushing | None:
        return InterrupterUnit.bushing.get_by_mrid(self, mrid)

    def add_bushing_fixed_contact(self, bushing_fixed_contact: Bushing) -> Self:
        return InterrupterUnit.bushing_fixed_contact.add(self, bushing_fixed_contact)

    def remove_bushing_fixed_contact(self, bushing_fixed_contact: Bushing) -> Self:
        return InterrupterUnit.bushing_fixed_contact.remove(self, bushing_fixed_contact)

    def clear_bushing_fixed_contact(self) -> Self:
        return InterrupterUnit.bushing_fixed_contact.clear(self)

    def num_bushing_fixed_contact(self) -> int:
        return InterrupterUnit.bushing_fixed_contact.count(self)

    def get_bushing_fixed_contact_by_mrid(self, mrid: str) -> Bushing | None:
        return InterrupterUnit.bushing_fixed_contact.get_by_mrid(self, mrid)

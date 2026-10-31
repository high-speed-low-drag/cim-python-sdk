"""CIM class SVC (TC57CIM/IEC61968/InfIEC61968/InfWiresExt). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.shunt_compensator import ShuntCompensator

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class SVC(ShuntCompensator):
    """SVC asset allows the capacitive and inductive ratings for each phase to be specified
    individually if required."""

    __slots__ = ("capacitive_rating", "inductive_rating")

    capacitive_rating: float | None  # Reactance
    inductive_rating: float | None  # Reactance

    _cim_meta = ClassMeta(
        cim_name="SVC",
        package="TC57CIM/IEC61968/InfIEC61968/InfWiresExt",
        guid="{F35F78AD-2E5A-4b02-8563-66478EC5EE09}",
        attributes=(
            AttrMeta("capacitive_rating", "capacitiveRating", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("inductive_rating", "inductiveRating", "Reactance", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        capacitive_rating: float | None = None,
        inductive_rating: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.capacitive_rating = capacitive_rating
        self.inductive_rating = inductive_rating

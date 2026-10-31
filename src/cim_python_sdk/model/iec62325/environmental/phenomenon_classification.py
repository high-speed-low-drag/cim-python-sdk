"""CIM class PhenomenonClassification (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.environmental.classification_condition import (
        ClassificationCondition,
    )
    from cim_python_sdk.model.iec62325.environmental.environmental_data_authority import (
        EnvironmentalDataAuthority,
    )
    from cim_python_sdk.model.iec62325.environmental.environmental_phenomenon import (
        EnvironmentalPhenomenon,
    )


class PhenomenonClassification(IdentifiedObject):
    """A pre-defined phenomenon classification as defined by a particular authority."""

    __slots__ = (
        "_classification_condition",
        "_environmental_data_authority",
        "_environmental_phenomenon",
    )

    classification_condition: Many[ClassificationCondition] = Many(
        EndMeta(
            name="classification_condition",
            cim_role="ClassificationCondition",
            target="cim_python_sdk.model.iec62325.environmental.classification_condition:ClassificationCondition",
            many=True,
            lower=0,
            upper=None,
            inverse="phenomenon_classification",
            aggregation="none",
        )
    )
    environmental_data_authority: One[EnvironmentalDataAuthority] = One(
        EndMeta(
            name="environmental_data_authority",
            cim_role="EnvironmentalDataAuthority",
            target="cim_python_sdk.model.iec62325.environmental.environmental_data_authority:EnvironmentalDataAuthority",
            many=False,
            lower=0,
            upper=1,
            inverse="phenomenon_classification",
            aggregation="none",
        )
    )
    environmental_phenomenon: Many[EnvironmentalPhenomenon] = Many(
        EndMeta(
            name="environmental_phenomenon",
            cim_role="EnvironmentalPhenomenon",
            target="cim_python_sdk.model.iec62325.environmental.environmental_phenomenon:EnvironmentalPhenomenon",
            many=True,
            lower=0,
            upper=None,
            inverse="phenomenon_classification",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PhenomenonClassification",
        package="TC57CIM/IEC62325/Environmental",
        guid="{02B4C2EF-115A-4282-9AEE-51545B483B7A}",
        ends=(
            classification_condition.meta,
            environmental_data_authority.meta,
            environmental_phenomenon.meta,
        ),
    )

    def __init__(
        self,
        *,
        classification_condition: Iterable[ClassificationCondition] | None = None,
        environmental_data_authority: EnvironmentalDataAuthority | None = None,
        environmental_phenomenon: Iterable[EnvironmentalPhenomenon] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if classification_condition is not None:
            PhenomenonClassification.classification_condition.extend(self, classification_condition)
        if environmental_data_authority is not None:
            self.environmental_data_authority = environmental_data_authority
        if environmental_phenomenon is not None:
            PhenomenonClassification.environmental_phenomenon.extend(self, environmental_phenomenon)

    def add_classification_condition(
        self, classification_condition: ClassificationCondition
    ) -> Self:
        return PhenomenonClassification.classification_condition.add(self, classification_condition)

    def remove_classification_condition(
        self, classification_condition: ClassificationCondition
    ) -> Self:
        return PhenomenonClassification.classification_condition.remove(
            self, classification_condition
        )

    def clear_classification_condition(self) -> Self:
        return PhenomenonClassification.classification_condition.clear(self)

    def num_classification_condition(self) -> int:
        return PhenomenonClassification.classification_condition.count(self)

    def get_classification_condition_by_mrid(self, mrid: str) -> ClassificationCondition | None:
        return PhenomenonClassification.classification_condition.get_by_mrid(self, mrid)

    def add_environmental_phenomenon(
        self, environmental_phenomenon: EnvironmentalPhenomenon
    ) -> Self:
        return PhenomenonClassification.environmental_phenomenon.add(self, environmental_phenomenon)

    def remove_environmental_phenomenon(
        self, environmental_phenomenon: EnvironmentalPhenomenon
    ) -> Self:
        return PhenomenonClassification.environmental_phenomenon.remove(
            self, environmental_phenomenon
        )

    def clear_environmental_phenomenon(self) -> Self:
        return PhenomenonClassification.environmental_phenomenon.clear(self)

    def num_environmental_phenomenon(self) -> int:
        return PhenomenonClassification.environmental_phenomenon.count(self)

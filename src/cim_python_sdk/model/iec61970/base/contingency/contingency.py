"""CIM class Contingency (TC57CIM/IEC61970/Base/Contingency). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.contingency.contingency_element import (
        ContingencyElement,
    )


class Contingency(IdentifiedObject):
    """An event threatening system reliability, consisting of one or more contingency elements."""

    __slots__ = ("_contingency_element", "must_study")

    must_study: bool | None

    contingency_element: Many[ContingencyElement] = Many(
        EndMeta(
            name="contingency_element",
            cim_role="ContingencyElement",
            target="cim_python_sdk.model.iec61970.base.contingency.contingency_element:ContingencyElement",
            many=True,
            lower=0,
            upper=None,
            inverse="contingency",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Contingency",
        package="TC57CIM/IEC61970/Base/Contingency",
        guid="{59E66284-A133-41d8-908F-DC6F74DF6426}",
        attributes=(AttrMeta("must_study", "mustStudy", "bool", 0, 1, "primitive"),),
        ends=(contingency_element.meta,),
    )

    def __init__(
        self,
        *,
        must_study: bool | None = None,
        contingency_element: Iterable[ContingencyElement] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.must_study = must_study
        if contingency_element is not None:
            Contingency.contingency_element.extend(self, contingency_element)

    def add_contingency_element(self, contingency_element: ContingencyElement) -> Self:
        return Contingency.contingency_element.add(self, contingency_element)

    def remove_contingency_element(self, contingency_element: ContingencyElement) -> Self:
        return Contingency.contingency_element.remove(self, contingency_element)

    def clear_contingency_element(self) -> Self:
        return Contingency.contingency_element.clear(self)

    def num_contingency_element(self) -> int:
        return Contingency.contingency_element.count(self)

    def get_contingency_element_by_mrid(self, mrid: str) -> ContingencyElement | None:
        return Contingency.contingency_element.get_by_mrid(self, mrid)

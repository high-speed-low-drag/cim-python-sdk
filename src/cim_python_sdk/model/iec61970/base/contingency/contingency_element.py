"""CIM class ContingencyElement (TC57CIM/IEC61970/Base/Contingency). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.contingency.contingency import Contingency


class ContingencyElement(IdentifiedObject):
    """An element of a system event to be studied by contingency analysis, representing a
    change in status of a single piece of equipment."""

    __slots__ = ("_contingency",)

    contingency: One[Contingency] = One(
        EndMeta(
            name="contingency",
            cim_role="Contingency",
            target="cim_python_sdk.model.iec61970.base.contingency.contingency:Contingency",
            many=False,
            lower=1,
            upper=1,
            inverse="contingency_element",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ContingencyElement",
        package="TC57CIM/IEC61970/Base/Contingency",
        guid="{53A27FB9-542A-4e43-B614-65F89F3AAD6A}",
        ends=(contingency.meta,),
    )

    def __init__(
        self,
        *,
        contingency: Contingency | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if contingency is not None:
            self.contingency = contingency

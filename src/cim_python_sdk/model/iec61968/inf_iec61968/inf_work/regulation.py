"""CIM class Regulation (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class Regulation(WorkDocument):
    """Special requirements and/or regulations may pertain to certain types of assets or work.
    For example, fire protection and scaffolding."""

    __slots__ = ("reference_number",)

    reference_number: str | None

    _cim_meta = ClassMeta(
        cim_name="Regulation",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{74C4BFF0-26BA-4841-8B3C-3AB942F7B5C4}",
        attributes=(AttrMeta("reference_number", "referenceNumber", "str", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        reference_number: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.reference_number = reference_number

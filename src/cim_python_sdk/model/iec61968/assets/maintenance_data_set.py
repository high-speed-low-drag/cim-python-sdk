"""CIM class MaintenanceDataSet (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.procedure_data_set import ProcedureDataSet

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class MaintenanceDataSet(ProcedureDataSet):
    """The result of a maintenance activity, a type of Procedure, for a given attribute of an
    asset."""

    __slots__ = ("condition_after", "condition_before", "maint_code")

    maint_code: str | None
    condition_before: str | None
    condition_after: str | None

    _cim_meta = ClassMeta(
        cim_name="MaintenanceDataSet",
        package="TC57CIM/IEC61968/Assets",
        guid="{D7D486F8-5BBE-4985-B51A-6E86727929C3}",
        attributes=(
            AttrMeta("maint_code", "maintCode", "str", 0, 1, "primitive"),
            AttrMeta("condition_before", "conditionBefore", "str", 0, 1, "primitive"),
            AttrMeta("condition_after", "conditionAfter", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        maint_code: str | None = None,
        condition_before: str | None = None,
        condition_after: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.maint_code = maint_code
        self.condition_before = condition_before
        self.condition_after = condition_after

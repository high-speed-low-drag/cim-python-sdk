"""CIM class ComplianceEvent (TC57CIM/IEC61968/InfIEC61968/InfCustomers). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any


class ComplianceEvent(ActivityRecord):
    """Compliance events are used for reporting regulatory or contract compliance issues and/or
    variances. These might be created as a consequence of local business processes and
    associated rules. It is anticipated that this class will be customised extensively to
    meet local implementation needs.

    Use inherited 'type' to indicate that, for example, expected performance will not be met
    or reported as mandated."""

    __slots__ = ("deadline",)

    deadline: _dt.datetime | None

    _cim_meta = ClassMeta(
        cim_name="ComplianceEvent",
        package="TC57CIM/IEC61968/InfIEC61968/InfCustomers",
        guid="{A10D9E17-4A19-40d7-A558-0C11D35E0CC8}",
        attributes=(AttrMeta("deadline", "deadline", "datetime", 0, 1, "primitive"),),
    )

    def __init__(
        self,
        *,
        deadline: _dt.datetime | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.deadline = deadline

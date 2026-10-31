"""CIM class OperationalUpdatedRating (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.operational_restriction import OperationalRestriction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.planned_outage import PlannedOutage


class OperationalUpdatedRating(OperationalRestriction):
    """Lowered capability because of deterioration or inadequacy (sometimes referred to as
    derating or partial outage) or other kind of operational rating change."""

    __slots__ = ("_planned_outage", "change_type")

    change_type: str | None

    planned_outage: One[PlannedOutage] = One(
        EndMeta(
            name="planned_outage",
            cim_role="PlannedOutage",
            target="cim_python_sdk.model.iec61968.operations.planned_outage:PlannedOutage",
            many=False,
            lower=1,
            upper=1,
            inverse="updated_ratings",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OperationalUpdatedRating",
        package="TC57CIM/IEC61968/Operations",
        guid="{5C9A09CF-769C-44fe-99C6-461466362FF0}",
        attributes=(AttrMeta("change_type", "changeType", "str", 0, 1, "primitive"),),
        ends=(planned_outage.meta,),
    )

    def __init__(
        self,
        *,
        change_type: str | None = None,
        planned_outage: PlannedOutage | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.change_type = change_type
        if planned_outage is not None:
            self.planned_outage = planned_outage

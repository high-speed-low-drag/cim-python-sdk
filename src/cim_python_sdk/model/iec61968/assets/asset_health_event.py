"""CIM class AssetHealthEvent (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.analytic import Analytic


class AssetHealthEvent(ActivityRecord):
    """An asset health-related event that is created by an analytic. The event is a record of a
    change in asset health."""

    __slots__ = ("_analytic", "action_recommendation", "action_timeline", "effective_date_time")

    action_recommendation: str | None
    action_timeline: str | None
    effective_date_time: _dt.datetime | None

    analytic: One[Analytic] = One(
        EndMeta(
            name="analytic",
            cim_role="Analytic",
            target="cim_python_sdk.model.iec61968.assets.analytic:Analytic",
            many=False,
            lower=1,
            upper=1,
            inverse="asset_health_event",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetHealthEvent",
        package="TC57CIM/IEC61968/Assets",
        guid="{7F3BB06D-D6E2-42cc-B6ED-A298269A8889}",
        attributes=(
            AttrMeta("action_recommendation", "actionRecommendation", "str", 0, 1, "primitive"),
            AttrMeta("action_timeline", "actionTimeline", "str", 0, 1, "primitive"),
            AttrMeta("effective_date_time", "effectiveDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(analytic.meta,),
    )

    def __init__(
        self,
        *,
        action_recommendation: str | None = None,
        action_timeline: str | None = None,
        effective_date_time: _dt.datetime | None = None,
        analytic: Analytic | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.action_recommendation = action_recommendation
        self.action_timeline = action_timeline
        self.effective_date_time = effective_date_time
        if analytic is not None:
            self.analytic = analytic

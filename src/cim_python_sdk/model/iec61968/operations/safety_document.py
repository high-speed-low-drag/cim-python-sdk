"""CIM class SafetyDocument (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.field_safety_supervisor import (
        FieldSafetySupervisor,
    )
    from cim_python_sdk.model.iec61968.operations.operations_safety_supervisor import (
        OperationsSafetySupervisor,
    )
    from cim_python_sdk.model.iec61968.operations.switching_plan import SwitchingPlan


class SafetyDocument(Document):
    """Document restricting or authorising works on electrical equipment (for example a permit
    to work, sanction for test, limitation of access, or certificate of isolation), defined
    based upon organisational practices."""

    __slots__ = (
        "_issued_by_supervisor",
        "_issued_to_supervisor",
        "_released_by_supervisor",
        "_released_to_supervisor",
        "_switching_plan",
        "issued_date_time",
        "released_date_time",
    )

    issued_date_time: _dt.datetime | None
    released_date_time: _dt.datetime | None

    issued_by_supervisor: One[OperationsSafetySupervisor] = One(
        EndMeta(
            name="issued_by_supervisor",
            cim_role="IssuedBySupervisor",
            target="cim_python_sdk.model.iec61968.operations.operations_safety_supervisor:OperationsSafetySupervisor",
            many=False,
            lower=0,
            upper=1,
            inverse="issued_safety_documents",
            aggregation="none",
        )
    )
    switching_plan: One[SwitchingPlan] = One(
        EndMeta(
            name="switching_plan",
            cim_role="SwitchingPlan",
            target="cim_python_sdk.model.iec61968.operations.switching_plan:SwitchingPlan",
            many=False,
            lower=0,
            upper=1,
            inverse="safety_documents",
            aggregation="none",
        )
    )
    released_to_supervisor: One[OperationsSafetySupervisor] = One(
        EndMeta(
            name="released_to_supervisor",
            cim_role="ReleasedToSupervisor",
            target="cim_python_sdk.model.iec61968.operations.operations_safety_supervisor:OperationsSafetySupervisor",
            many=False,
            lower=0,
            upper=1,
            inverse="released_safety_documents",
            aggregation="none",
        )
    )
    issued_to_supervisor: One[FieldSafetySupervisor] = One(
        EndMeta(
            name="issued_to_supervisor",
            cim_role="IssuedToSupervisor",
            target="cim_python_sdk.model.iec61968.operations.field_safety_supervisor:FieldSafetySupervisor",
            many=False,
            lower=0,
            upper=1,
            inverse="issued_safety_documents",
            aggregation="none",
        )
    )
    released_by_supervisor: One[FieldSafetySupervisor] = One(
        EndMeta(
            name="released_by_supervisor",
            cim_role="ReleasedBySupervisor",
            target="cim_python_sdk.model.iec61968.operations.field_safety_supervisor:FieldSafetySupervisor",
            many=False,
            lower=0,
            upper=1,
            inverse="released_safety_documents",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SafetyDocument",
        package="TC57CIM/IEC61968/Operations",
        guid="{AC73635B-66D4-4451-B175-9206C19BA6A9}",
        attributes=(
            AttrMeta("issued_date_time", "issuedDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("released_date_time", "releasedDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            issued_by_supervisor.meta,
            switching_plan.meta,
            released_to_supervisor.meta,
            issued_to_supervisor.meta,
            released_by_supervisor.meta,
        ),
    )

    def __init__(
        self,
        *,
        issued_date_time: _dt.datetime | None = None,
        released_date_time: _dt.datetime | None = None,
        issued_by_supervisor: OperationsSafetySupervisor | None = None,
        switching_plan: SwitchingPlan | None = None,
        released_to_supervisor: OperationsSafetySupervisor | None = None,
        issued_to_supervisor: FieldSafetySupervisor | None = None,
        released_by_supervisor: FieldSafetySupervisor | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.issued_date_time = issued_date_time
        self.released_date_time = released_date_time
        if issued_by_supervisor is not None:
            self.issued_by_supervisor = issued_by_supervisor
        if switching_plan is not None:
            self.switching_plan = switching_plan
        if released_to_supervisor is not None:
            self.released_to_supervisor = released_to_supervisor
        if issued_to_supervisor is not None:
            self.issued_to_supervisor = issued_to_supervisor
        if released_by_supervisor is not None:
            self.released_by_supervisor = released_by_supervisor

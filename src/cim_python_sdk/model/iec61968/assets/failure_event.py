"""CIM class FailureEvent (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.common.activity_record import ActivityRecord

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.asset_failure_classification import (
        AssetFailureClassification,
    )
    from cim_python_sdk.model.iec61968.assets.asset_failure_mode import AssetFailureMode
    from cim_python_sdk.model.iec61968.assets.breaker_failure_reason_kind import (
        BreakerFailureReasonKind,
    )
    from cim_python_sdk.model.iec61968.assets.failure_isolation_method_kind import (
        FailureIsolationMethodKind,
    )
    from cim_python_sdk.model.iec61968.assets.transformer_failure_reason_kind import (
        TransformerFailureReasonKind,
    )


class FailureEvent(ActivityRecord):
    """An event where an asset has failed to perform its functions within specified parameters.
    This class is intended to reflect the failure itself. Additional information resulting
    from forensic analysis could be captured by a diagnosis data set."""

    __slots__ = (
        "breaker_failure_reason",
        "corporate_code",
        "failure_classification",
        "failure_date_time",
        "failure_isolation_method",
        "failure_mode",
        "fault_locating_method",
        "location",
        "root_cause",
        "transformer_failure_reason",
    )

    failure_date_time: _dt.datetime | None
    failure_classification: AssetFailureClassification | None
    corporate_code: str | None
    failure_mode: AssetFailureMode | None
    breaker_failure_reason: BreakerFailureReasonKind | None
    transformer_failure_reason: TransformerFailureReasonKind | None
    root_cause: str | None
    failure_isolation_method: FailureIsolationMethodKind | None
    fault_locating_method: str | None
    location: str | None

    _cim_meta = ClassMeta(
        cim_name="FailureEvent",
        package="TC57CIM/IEC61968/Assets",
        guid="{25FAD1AB-8885-4a72-9AD2-EFD361F4FFB2}",
        attributes=(
            AttrMeta("failure_date_time", "failureDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta(
                "failure_classification",
                "failureClassification",
                "AssetFailureClassification",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("corporate_code", "corporateCode", "str", 0, 1, "primitive"),
            AttrMeta("failure_mode", "failureMode", "AssetFailureMode", 1, 1, "enumeration"),
            AttrMeta(
                "breaker_failure_reason",
                "breakerFailureReason",
                "BreakerFailureReasonKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "transformer_failure_reason",
                "transformerFailureReason",
                "TransformerFailureReasonKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("root_cause", "rootCause", "str", 0, 1, "primitive"),
            AttrMeta(
                "failure_isolation_method",
                "failureIsolationMethod",
                "FailureIsolationMethodKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("fault_locating_method", "faultLocatingMethod", "str", 0, 1, "primitive"),
            AttrMeta("location", "location", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        failure_date_time: _dt.datetime | None = None,
        failure_classification: AssetFailureClassification | None = None,
        corporate_code: str | None = None,
        failure_mode: AssetFailureMode | None = None,
        breaker_failure_reason: BreakerFailureReasonKind | None = None,
        transformer_failure_reason: TransformerFailureReasonKind | None = None,
        root_cause: str | None = None,
        failure_isolation_method: FailureIsolationMethodKind | None = None,
        fault_locating_method: str | None = None,
        location: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.failure_date_time = failure_date_time
        self.failure_classification = failure_classification
        self.corporate_code = corporate_code
        self.failure_mode = failure_mode
        self.breaker_failure_reason = breaker_failure_reason
        self.transformer_failure_reason = transformer_failure_reason
        self.root_cause = root_cause
        self.failure_isolation_method = failure_isolation_method
        self.fault_locating_method = fault_locating_method
        self.location = location

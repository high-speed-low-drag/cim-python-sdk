"""CIM class DiagnosisDataSet (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.procedure_data_set import ProcedureDataSet

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61970.base.core.phase_code import PhaseCode


class DiagnosisDataSet(ProcedureDataSet):
    """The result of a problem (typically an asset failure) diagnosis. Contains complete
    information like what might be received from a lab doing forensic analysis of a failed
    asset."""

    __slots__ = (
        "effect",
        "failure_mode",
        "final_cause",
        "final_code",
        "final_origin",
        "final_remark",
        "phase_code",
        "preliminary_code",
        "preliminary_date_time",
        "preliminary_remark",
        "root_cause",
        "root_origin",
        "root_remark",
    )

    preliminary_code: str | None
    preliminary_remark: str | None
    preliminary_date_time: _dt.datetime | None
    final_code: str | None
    final_remark: str | None
    final_cause: str | None
    final_origin: str | None
    root_cause: str | None
    root_origin: str | None
    root_remark: str | None
    effect: str | None
    phase_code: PhaseCode | None
    failure_mode: str | None

    _cim_meta = ClassMeta(
        cim_name="DiagnosisDataSet",
        package="TC57CIM/IEC61968/Assets",
        guid="{F2EE22E4-D486-420a-9E8C-86C8CDFBFB08}",
        attributes=(
            AttrMeta("preliminary_code", "preliminaryCode", "str", 0, 1, "primitive"),
            AttrMeta("preliminary_remark", "preliminaryRemark", "str", 0, 1, "primitive"),
            AttrMeta("preliminary_date_time", "preliminaryDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("final_code", "finalCode", "str", 0, 1, "primitive"),
            AttrMeta("final_remark", "finalRemark", "str", 0, 1, "primitive"),
            AttrMeta("final_cause", "finalCause", "str", 0, 1, "primitive"),
            AttrMeta("final_origin", "finalOrigin", "str", 0, 1, "primitive"),
            AttrMeta("root_cause", "rootCause", "str", 0, 1, "primitive"),
            AttrMeta("root_origin", "rootOrigin", "str", 0, 1, "primitive"),
            AttrMeta("root_remark", "rootRemark", "str", 0, 1, "primitive"),
            AttrMeta("effect", "effect", "str", 0, 1, "primitive"),
            AttrMeta("phase_code", "phaseCode", "PhaseCode", 0, 1, "enumeration"),
            AttrMeta("failure_mode", "failureMode", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        preliminary_code: str | None = None,
        preliminary_remark: str | None = None,
        preliminary_date_time: _dt.datetime | None = None,
        final_code: str | None = None,
        final_remark: str | None = None,
        final_cause: str | None = None,
        final_origin: str | None = None,
        root_cause: str | None = None,
        root_origin: str | None = None,
        root_remark: str | None = None,
        effect: str | None = None,
        phase_code: PhaseCode | None = None,
        failure_mode: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.preliminary_code = preliminary_code
        self.preliminary_remark = preliminary_remark
        self.preliminary_date_time = preliminary_date_time
        self.final_code = final_code
        self.final_remark = final_remark
        self.final_cause = final_cause
        self.final_origin = final_origin
        self.root_cause = root_cause
        self.root_origin = root_origin
        self.root_remark = root_remark
        self.effect = effect
        self.phase_code = phase_code
        self.failure_mode = failure_mode

"""CIM class InfoQuestion (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any


class InfoQuestion(WorkDocument):
    """Questions and answers associated with a type of document for purposes of clarification.
    Questions may be predefined or ad hoc."""

    __slots__ = (
        "answer",
        "answer_date_time",
        "answer_remark",
        "question_code",
        "question_remark",
        "question_text",
        "question_type",
    )

    question_type: str | None
    question_code: str | None
    question_text: str | None
    question_remark: str | None
    answer: str | None
    answer_remark: str | None
    answer_date_time: _dt.datetime | None

    _cim_meta = ClassMeta(
        cim_name="InfoQuestion",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{A02C4C78-68EE-49cb-848C-C7E34BD60B45}",
        attributes=(
            AttrMeta("question_type", "questionType", "str", 0, 1, "primitive"),
            AttrMeta("question_code", "questionCode", "str", 0, 1, "primitive"),
            AttrMeta("question_text", "questionText", "str", 0, 1, "primitive"),
            AttrMeta("question_remark", "questionRemark", "str", 0, 1, "primitive"),
            AttrMeta("answer", "answer", "str", 0, 1, "primitive"),
            AttrMeta("answer_remark", "answerRemark", "str", 0, 1, "primitive"),
            AttrMeta("answer_date_time", "answerDateTime", "datetime", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        question_type: str | None = None,
        question_code: str | None = None,
        question_text: str | None = None,
        question_remark: str | None = None,
        answer: str | None = None,
        answer_remark: str | None = None,
        answer_date_time: _dt.datetime | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.question_type = question_type
        self.question_code = question_code
        self.question_text = question_text
        self.question_remark = question_remark
        self.answer = answer
        self.answer_remark = answer_remark
        self.answer_date_time = answer_date_time

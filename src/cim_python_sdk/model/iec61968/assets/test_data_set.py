"""CIM class TestDataSet (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.procedure_data_set import ProcedureDataSet

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any


class TestDataSet(ProcedureDataSet):
    """Test results, usually obtained by a lab or other independent organisation."""

    __slots__ = ("conclusion", "specimen_id", "specimen_to_lab_date_time")

    specimen_id: str | None
    specimen_to_lab_date_time: _dt.datetime | None
    conclusion: str | None

    _cim_meta = ClassMeta(
        cim_name="TestDataSet",
        package="TC57CIM/IEC61968/Assets",
        guid="{22F31D68-A247-4eb9-9388-56AAE86EB740}",
        attributes=(
            AttrMeta("specimen_id", "specimenID", "str", 0, 1, "primitive"),
            AttrMeta(
                "specimen_to_lab_date_time", "specimenToLabDateTime", "datetime", 0, 1, "primitive"
            ),
            AttrMeta("conclusion", "conclusion", "str", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        specimen_id: str | None = None,
        specimen_to_lab_date_time: _dt.datetime | None = None,
        conclusion: str | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.specimen_id = specimen_id
        self.specimen_to_lab_date_time = specimen_to_lab_date_time
        self.conclusion = conclusion

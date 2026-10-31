"""CIM class Tool (TC57CIM/IEC61968/Work). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.work.work_asset import WorkAsset

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any


class Tool(WorkAsset):
    """Tool asset."""

    __slots__ = ("last_calibration_date",)

    last_calibration_date: _dt.date | None

    _cim_meta = ClassMeta(
        cim_name="Tool",
        package="TC57CIM/IEC61968/Work",
        guid="{C7051DBE-5667-4bec-A88B-ABAFF00B1A5F}",
        attributes=(
            AttrMeta("last_calibration_date", "lastCalibrationDate", "date", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        last_calibration_date: _dt.date | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.last_calibration_date = last_calibration_date

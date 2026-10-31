"""CIM class ErpTimeSheet (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_time_entry import (
        ErpTimeEntry,
    )


class ErpTimeSheet(ErpDocument):
    """Time sheet for employees and contractors. Note that ErpTimeSheet inherits the
    relationship to ErpPerson from Document."""

    __slots__ = ("_erp_time_entries",)

    erp_time_entries: Many[ErpTimeEntry] = Many(
        EndMeta(
            name="erp_time_entries",
            cim_role="ErpTimeEntries",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_time_entry:ErpTimeEntry",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_time_sheet",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpTimeSheet",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{9725D15F-064E-4660-B4C1-359903B2B1C9}",
        ends=(erp_time_entries.meta,),
    )

    def __init__(
        self,
        *,
        erp_time_entries: Iterable[ErpTimeEntry] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if erp_time_entries is not None:
            ErpTimeSheet.erp_time_entries.extend(self, erp_time_entries)

    def add_erp_time_entry(self, erp_time_entry: ErpTimeEntry) -> Self:
        return ErpTimeSheet.erp_time_entries.add(self, erp_time_entry)

    def remove_erp_time_entry(self, erp_time_entry: ErpTimeEntry) -> Self:
        return ErpTimeSheet.erp_time_entries.remove(self, erp_time_entry)

    def clear_erp_time_entries(self) -> Self:
        return ErpTimeSheet.erp_time_entries.clear(self)

    def num_erp_time_entry(self) -> int:
        return ErpTimeSheet.erp_time_entries.count(self)

    def get_erp_time_entry_by_mrid(self, mrid: str) -> ErpTimeEntry | None:
        return ErpTimeSheet.erp_time_entries.get_by_mrid(self, mrid)

"""CIM class ErpTimeEntry (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_identified_object import (
    ErpIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_project_accounting import (
        ErpProjectAccounting,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_time_sheet import (
        ErpTimeSheet,
    )


class ErpTimeEntry(ErpIdentifiedObject):
    """An individual entry on an ErpTimeSheet."""

    __slots__ = ("_erp_project_accounting", "_erp_time_sheet", "status")

    status: Status | None

    erp_time_sheet: One[ErpTimeSheet] = One(
        EndMeta(
            name="erp_time_sheet",
            cim_role="ErpTimeSheet",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_time_sheet:ErpTimeSheet",
            many=False,
            lower=1,
            upper=1,
            inverse="erp_time_entries",
            aggregation="none",
        )
    )
    erp_project_accounting: One[ErpProjectAccounting] = One(
        EndMeta(
            name="erp_project_accounting",
            cim_role="ErpProjectAccounting",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_project_accounting:ErpProjectAccounting",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_time_entries",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpTimeEntry",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{FC84C591-8D30-4217-BA53-DB078BB684AA}",
        attributes=(AttrMeta("status", "status", "Status", 0, 1, "compound"),),
        ends=(
            erp_time_sheet.meta,
            erp_project_accounting.meta,
        ),
    )

    def __init__(
        self,
        *,
        status: Status | None = None,
        erp_time_sheet: ErpTimeSheet | None = None,
        erp_project_accounting: ErpProjectAccounting | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.status = status
        if erp_time_sheet is not None:
            self.erp_time_sheet = erp_time_sheet
        if erp_project_accounting is not None:
            self.erp_project_accounting = erp_project_accounting

"""CIM class ErpBOM (TC57CIM/IEC61968/InfIEC61968/InfERPSupport). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_document import ErpDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_bom_item_data import (
        ErpBomItemData,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design import Design


class ErpBOM(ErpDocument):
    """Information that generally describes the Bill of Material Structure and its contents for
    a utility.

    This is used by ERP systems to transfer Bill of Material information between two
    business applications."""

    __slots__ = ("_design", "_erp_bom_item_datas")

    design: One[Design] = One(
        EndMeta(
            name="design",
            cim_role="Design",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design:Design",
            many=False,
            lower=0,
            upper=1,
            inverse="erp_boms",
            aggregation="none",
        )
    )
    erp_bom_item_datas: Many[ErpBomItemData] = Many(
        EndMeta(
            name="erp_bom_item_datas",
            cim_role="ErpBomItemDatas",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_erp_support.erp_bom_item_data:ErpBomItemData",
            many=True,
            lower=0,
            upper=None,
            inverse="erp_bom",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ErpBOM",
        package="TC57CIM/IEC61968/InfIEC61968/InfERPSupport",
        guid="{338BF3FA-0E69-4e0a-9CE2-A99A98ADA226}",
        ends=(
            design.meta,
            erp_bom_item_datas.meta,
        ),
    )

    def __init__(
        self,
        *,
        design: Design | None = None,
        erp_bom_item_datas: Iterable[ErpBomItemData] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if design is not None:
            self.design = design
        if erp_bom_item_datas is not None:
            ErpBOM.erp_bom_item_datas.extend(self, erp_bom_item_datas)

    def add_erp_bom_item_data(self, erp_bom_item_data: ErpBomItemData) -> Self:
        return ErpBOM.erp_bom_item_datas.add(self, erp_bom_item_data)

    def remove_erp_bom_item_data(self, erp_bom_item_data: ErpBomItemData) -> Self:
        return ErpBOM.erp_bom_item_datas.remove(self, erp_bom_item_data)

    def clear_erp_bom_item_datas(self) -> Self:
        return ErpBOM.erp_bom_item_datas.clear(self)

    def num_erp_bom_item_data(self) -> int:
        return ErpBOM.erp_bom_item_datas.count(self)

    def get_erp_bom_item_data_by_mrid(self, mrid: str) -> ErpBomItemData | None:
        return ErpBOM.erp_bom_item_datas.get_by_mrid(self, mrid)

"""CIM class NonStandardItem (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_document import WorkDocument

TYPE_CHECKING = False
if TYPE_CHECKING:
    import decimal as _decimal
    from typing import Any


class NonStandardItem(WorkDocument):
    """This document provides information for non-standard items like customer contributions
    (e.g., customer digs trench), vouchers (e.g., credit), and contractor bids."""

    __slots__ = ("amount",)

    amount: _decimal.Decimal | None  # Money

    _cim_meta = ClassMeta(
        cim_name="NonStandardItem",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{2D51D3F2-0C51-48c2-B14F-277761C9644A}",
        attributes=(AttrMeta("amount", "amount", "Money", 0, 1, "cimdatatype"),),
    )

    def __init__(
        self,
        *,
        amount: _decimal.Decimal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.amount = amount

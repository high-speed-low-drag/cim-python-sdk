"""CIM class Process (TC57CIM/IEC62325/MarketManagement). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_management.market_document import MarketDocument


class Process(IdentifiedObject):
    """The formal specification of a set of business transactions having the same business
    goal."""

    __slots__ = ("_market_document", "classification_type", "process_type")

    classification_type: str | None
    process_type: str | None

    market_document: Many[MarketDocument] = Many(
        EndMeta(
            name="market_document",
            cim_role="MarketDocument",
            target="cim_python_sdk.model.iec62325.market_management.market_document:MarketDocument",
            many=True,
            lower=0,
            upper=None,
            inverse="process",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Process",
        package="TC57CIM/IEC62325/MarketManagement",
        guid="{2324D336-1F92-46ac-9F20-F4F58E8FFDF1}",
        attributes=(
            AttrMeta("classification_type", "classificationType", "str", 0, 1, "primitive"),
            AttrMeta("process_type", "processType", "str", 0, 1, "primitive"),
        ),
        ends=(market_document.meta,),
    )

    def __init__(
        self,
        *,
        classification_type: str | None = None,
        process_type: str | None = None,
        market_document: Iterable[MarketDocument] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.classification_type = classification_type
        self.process_type = process_type
        if market_document is not None:
            Process.market_document.extend(self, market_document)

    def add_market_document(self, market_document: MarketDocument) -> Self:
        return Process.market_document.add(self, market_document)

    def remove_market_document(self, market_document: MarketDocument) -> Self:
        return Process.market_document.remove(self, market_document)

    def clear_market_document(self) -> Self:
        return Process.market_document.clear(self)

    def num_market_document(self) -> int:
        return Process.market_document.count(self)

    def get_market_document_by_mrid(self, mrid: str) -> MarketDocument | None:
        return Process.market_document.get_by_mrid(self, mrid)

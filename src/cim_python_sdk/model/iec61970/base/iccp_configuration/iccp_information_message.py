"""CIM class ICCPInformationMessage (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.iccp_configuration.iccp_scope_kind import ICCPScopeKind
    from cim_python_sdk.model.iec61970.base.iccp_configuration.tase2_bilateral_table import (
        TASE2BilateralTable,
    )


class ICCPInformationMessage(IdentifiedObject):
    """This class represents the TASE.2 Information Message Object. The IdentifiedObject.name
    attribute must be non-null. The value of the attribute shall be used as the TASE.2
    Information Reference, as specified by 60870-6-503."""

    __slots__ = ("_tase2_bilateral_table", "local_reference", "scope")

    local_reference: str | None
    scope: ICCPScopeKind | None

    tase2_bilateral_table: Many[TASE2BilateralTable] = Many(
        EndMeta(
            name="tase2_bilateral_table",
            cim_role="TASE2BilateralTable",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.tase2_bilateral_table:TASE2BilateralTable",
            many=True,
            lower=0,
            upper=None,
            inverse="iccp_information_message",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ICCPInformationMessage",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{91E03624-A558-4c3f-84CA-1EB2E25826F7}",
        attributes=(
            AttrMeta("local_reference", "localReference", "str", 0, 1, "primitive"),
            AttrMeta("scope", "scope", "ICCPScopeKind", 0, 1, "enumeration"),
        ),
        ends=(tase2_bilateral_table.meta,),
    )

    def __init__(
        self,
        *,
        local_reference: str | None = None,
        scope: ICCPScopeKind | None = None,
        tase2_bilateral_table: Iterable[TASE2BilateralTable] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.local_reference = local_reference
        self.scope = scope
        if tase2_bilateral_table is not None:
            ICCPInformationMessage.tase2_bilateral_table.extend(self, tase2_bilateral_table)

    def add_tase2_bilateral_table(self, tase2_bilateral_table: TASE2BilateralTable) -> Self:
        return ICCPInformationMessage.tase2_bilateral_table.add(self, tase2_bilateral_table)

    def remove_tase2_bilateral_table(self, tase2_bilateral_table: TASE2BilateralTable) -> Self:
        return ICCPInformationMessage.tase2_bilateral_table.remove(self, tase2_bilateral_table)

    def clear_tase2_bilateral_table(self) -> Self:
        return ICCPInformationMessage.tase2_bilateral_table.clear(self)

    def num_tase2_bilateral_table(self) -> int:
        return ICCPInformationMessage.tase2_bilateral_table.count(self)

    def get_tase2_bilateral_table_by_mrid(self, mrid: str) -> TASE2BilateralTable | None:
        return ICCPInformationMessage.tase2_bilateral_table.get_by_mrid(self, mrid)

"""CIM class TASE2BilateralTable (TC57CIM/IEC61970/Base/ICCPConfiguration). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.iccp_configuration.bilateral_exchange_agreement import (
    BilateralExchangeAgreement,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.iccp_configuration.iccp_information_message import (
        ICCPInformationMessage,
    )


class TASE2BilateralTable(BilateralExchangeAgreement):
    """This class describe the sending (providing) side in a bilateral ICCP data exchange.
    Hence the ICCP bilateral (table) descriptions are created by exchanging ICCP Provider
    data between the parties."""

    __slots__ = (
        "_iccp_information_message",
        "bilateral_table_id",
        "bilateral_table_version",
        "tase2version",
    )

    bilateral_table_id: str | None
    tase2version: str | None
    bilateral_table_version: str | None

    iccp_information_message: Many[ICCPInformationMessage] = Many(
        EndMeta(
            name="iccp_information_message",
            cim_role="ICCPInformationMessage",
            target="cim_python_sdk.model.iec61970.base.iccp_configuration.iccp_information_message:ICCPInformationMessage",
            many=True,
            lower=0,
            upper=None,
            inverse="tase2_bilateral_table",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TASE2BilateralTable",
        package="TC57CIM/IEC61970/Base/ICCPConfiguration",
        guid="{EECBB158-724F-411e-ABE9-FF28E5DCE4B3}",
        attributes=(
            AttrMeta("bilateral_table_id", "bilateralTableID", "str", 0, 1, "primitive"),
            AttrMeta("tase2version", "tase2version", "str", 0, 1, "primitive"),
            AttrMeta("bilateral_table_version", "bilateralTableVersion", "str", 0, 1, "primitive"),
        ),
        ends=(iccp_information_message.meta,),
    )

    def __init__(
        self,
        *,
        bilateral_table_id: str | None = None,
        tase2version: str | None = None,
        bilateral_table_version: str | None = None,
        iccp_information_message: Iterable[ICCPInformationMessage] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bilateral_table_id = bilateral_table_id
        self.tase2version = tase2version
        self.bilateral_table_version = bilateral_table_version
        if iccp_information_message is not None:
            TASE2BilateralTable.iccp_information_message.extend(self, iccp_information_message)

    def add_iccp_information_message(
        self, iccp_information_message: ICCPInformationMessage
    ) -> Self:
        return TASE2BilateralTable.iccp_information_message.add(self, iccp_information_message)

    def remove_iccp_information_message(
        self, iccp_information_message: ICCPInformationMessage
    ) -> Self:
        return TASE2BilateralTable.iccp_information_message.remove(self, iccp_information_message)

    def clear_iccp_information_message(self) -> Self:
        return TASE2BilateralTable.iccp_information_message.clear(self)

    def num_iccp_information_message(self) -> int:
        return TASE2BilateralTable.iccp_information_message.count(self)

    def get_iccp_information_message_by_mrid(self, mrid: str) -> ICCPInformationMessage | None:
        return TASE2BilateralTable.iccp_information_message.get_by_mrid(self, mrid)

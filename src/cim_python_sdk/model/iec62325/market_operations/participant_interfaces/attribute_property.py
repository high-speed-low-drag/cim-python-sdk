"""CIM class AttributeProperty (TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_user_attribute import (
        MktUserAttribute,
    )


class AttributeProperty(CimObject):
    """Property for a particular attribute that contains name and value."""

    __slots__ = ("_mkt_user_attribute", "property_name", "property_value", "sequence")

    sequence: str | None
    property_name: str | None
    property_value: str | None

    mkt_user_attribute: One[MktUserAttribute] = One(
        EndMeta(
            name="mkt_user_attribute",
            cim_role="MktUserAttribute",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_user_attribute:MktUserAttribute",
            many=False,
            lower=1,
            upper=1,
            inverse="attribute_property",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AttributeProperty",
        package="TC57CIM/IEC62325/MarketOperations/ParticipantInterfaces",
        guid="{6DE808FB-62C0-428a-BBF9-A6FCC534EA34}",
        attributes=(
            AttrMeta("sequence", "sequence", "str", 0, 1, "primitive"),
            AttrMeta("property_name", "propertyName", "str", 0, 1, "primitive"),
            AttrMeta("property_value", "propertyValue", "str", 0, 1, "primitive"),
        ),
        ends=(mkt_user_attribute.meta,),
    )

    def __init__(
        self,
        *,
        sequence: str | None = None,
        property_name: str | None = None,
        property_value: str | None = None,
        mkt_user_attribute: MktUserAttribute | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.sequence = sequence
        self.property_name = property_name
        self.property_value = property_value
        if mkt_user_attribute is not None:
            self.mkt_user_attribute = mkt_user_attribute

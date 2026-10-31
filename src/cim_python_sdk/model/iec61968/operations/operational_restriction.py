"""CIM class OperationalRestriction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.product_asset_model import ProductAssetModel
    from cim_python_sdk.model.iec61970.base.core.equipment import Equipment
    from cim_python_sdk.model.iec61970.base.domain.date_time_interval import DateTimeInterval
    from cim_python_sdk.model.iec61970.base.domain.float_quantity import FloatQuantity


class OperationalRestriction(Document):
    """A document that can be associated with equipment to describe any sort of restrictions
    compared with the original manufacturer's specification or with the usual operational
    practice e.g. temporary maximum loadings, maximum switching current, do not operate if
    bus couplers are open, etc.

    In the UK, for example, if a breaker or switch ever mal-operates, this is reported
    centrally and utilities use their asset systems to identify all the installed devices of
    the same manufacturer's type. They then apply operational restrictions in the
    operational systems to warn operators of potential problems. After appropriate
    inspection and maintenance, the operational restrictions may be removed."""

    __slots__ = ("_equipments", "_product_asset_model", "active_period", "restricted_value")

    active_period: DateTimeInterval | None
    restricted_value: FloatQuantity | None

    product_asset_model: One[ProductAssetModel] = One(
        EndMeta(
            name="product_asset_model",
            cim_role="ProductAssetModel",
            target="cim_python_sdk.model.iec61968.assets.product_asset_model:ProductAssetModel",
            many=False,
            lower=0,
            upper=1,
            inverse="operational_restrictions",
            aggregation="none",
        )
    )
    equipments: Many[Equipment] = Many(
        EndMeta(
            name="equipments",
            cim_role="Equipments",
            target="cim_python_sdk.model.iec61970.base.core.equipment:Equipment",
            many=True,
            lower=0,
            upper=None,
            inverse="operational_restrictions",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OperationalRestriction",
        package="TC57CIM/IEC61968/Operations",
        guid="{0093960F-86E8-4b3c-AD90-C7777658369A}",
        attributes=(
            AttrMeta("active_period", "activePeriod", "DateTimeInterval", 0, 1, "compound"),
            AttrMeta("restricted_value", "restrictedValue", "FloatQuantity", 0, 1, "compound"),
        ),
        ends=(
            product_asset_model.meta,
            equipments.meta,
        ),
    )

    def __init__(
        self,
        *,
        active_period: DateTimeInterval | None = None,
        restricted_value: FloatQuantity | None = None,
        product_asset_model: ProductAssetModel | None = None,
        equipments: Iterable[Equipment] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.active_period = active_period
        self.restricted_value = restricted_value
        if product_asset_model is not None:
            self.product_asset_model = product_asset_model
        if equipments is not None:
            OperationalRestriction.equipments.extend(self, equipments)

    def add_equipment(self, equipment: Equipment) -> Self:
        return OperationalRestriction.equipments.add(self, equipment)

    def remove_equipment(self, equipment: Equipment) -> Self:
        return OperationalRestriction.equipments.remove(self, equipment)

    def clear_equipments(self) -> Self:
        return OperationalRestriction.equipments.clear(self)

    def num_equipment(self) -> int:
        return OperationalRestriction.equipments.count(self)

    def get_equipment_by_mrid(self, mrid: str) -> Equipment | None:
        return OperationalRestriction.equipments.get_by_mrid(self, mrid)

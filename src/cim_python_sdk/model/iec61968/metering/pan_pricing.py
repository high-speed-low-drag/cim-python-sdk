"""CIM class PanPricing (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.metering.end_device_action import EndDeviceAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.pan_pricing_detail import PanPricingDetail


class PanPricing(EndDeviceAction):
    """PAN action/command used to issue pricing information to a PAN device."""

    __slots__ = ("_pan_pricing_details", "provider_id")

    provider_id: int | None

    pan_pricing_details: Many[PanPricingDetail] = Many(
        EndMeta(
            name="pan_pricing_details",
            cim_role="PanPricingDetails",
            target="cim_python_sdk.model.iec61968.metering.pan_pricing_detail:PanPricingDetail",
            many=True,
            lower=0,
            upper=None,
            inverse="pan_pricing",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PanPricing",
        package="TC57CIM/IEC61968/Metering",
        guid="{2A41821C-8F9D-44f9-9FDF-AB4D0F06D327}",
        attributes=(AttrMeta("provider_id", "providerID", "int", 0, 1, "primitive"),),
        ends=(pan_pricing_details.meta,),
    )

    def __init__(
        self,
        *,
        provider_id: int | None = None,
        pan_pricing_details: Iterable[PanPricingDetail] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.provider_id = provider_id
        if pan_pricing_details is not None:
            PanPricing.pan_pricing_details.extend(self, pan_pricing_details)

    def add_pan_pricing_detail(self, pan_pricing_detail: PanPricingDetail) -> Self:
        return PanPricing.pan_pricing_details.add(self, pan_pricing_detail)

    def remove_pan_pricing_detail(self, pan_pricing_detail: PanPricingDetail) -> Self:
        return PanPricing.pan_pricing_details.remove(self, pan_pricing_detail)

    def clear_pan_pricing_details(self) -> Self:
        return PanPricing.pan_pricing_details.clear(self)

    def num_pan_pricing_detail(self) -> int:
        return PanPricing.pan_pricing_details.count(self)

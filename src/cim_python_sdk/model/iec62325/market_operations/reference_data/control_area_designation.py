"""CIM class ControlAreaDesignation (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, Many

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class ControlAreaDesignation(CimObject):
    """Indicates Control Area associated with self-schedule."""

    __slots__ = ("_registered_resource", "_sub_control_area", "attained", "native")

    attained: YesNo | None
    native: YesNo | None

    sub_control_area: Many[SubControlArea] = Many(
        EndMeta(
            name="sub_control_area",
            cim_role="SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=True,
            lower=0,
            upper=None,
            inverse="control_area_designation",
            aggregation="none",
        )
    )
    registered_resource: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=0,
            upper=None,
            inverse="control_area_designation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ControlAreaDesignation",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{9F672624-43B0-4b32-8BBE-9D9AE4479C53}",
        attributes=(
            AttrMeta("attained", "attained", "YesNo", 0, 1, "enumeration"),
            AttrMeta("native", "native", "YesNo", 0, 1, "enumeration"),
        ),
        ends=(
            sub_control_area.meta,
            registered_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        attained: YesNo | None = None,
        native: YesNo | None = None,
        sub_control_area: Iterable[SubControlArea] | None = None,
        registered_resource: Iterable[RegisteredResource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.attained = attained
        self.native = native
        if sub_control_area is not None:
            ControlAreaDesignation.sub_control_area.extend(self, sub_control_area)
        if registered_resource is not None:
            ControlAreaDesignation.registered_resource.extend(self, registered_resource)

    def add_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return ControlAreaDesignation.sub_control_area.add(self, sub_control_area)

    def remove_sub_control_area(self, sub_control_area: SubControlArea) -> Self:
        return ControlAreaDesignation.sub_control_area.remove(self, sub_control_area)

    def clear_sub_control_area(self) -> Self:
        return ControlAreaDesignation.sub_control_area.clear(self)

    def num_sub_control_area(self) -> int:
        return ControlAreaDesignation.sub_control_area.count(self)

    def get_sub_control_area_by_mrid(self, mrid: str) -> SubControlArea | None:
        return ControlAreaDesignation.sub_control_area.get_by_mrid(self, mrid)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return ControlAreaDesignation.registered_resource.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return ControlAreaDesignation.registered_resource.remove(self, registered_resource)

    def clear_registered_resource(self) -> Self:
        return ControlAreaDesignation.registered_resource.clear(self)

    def num_registered_resource(self) -> int:
        return ControlAreaDesignation.registered_resource.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return ControlAreaDesignation.registered_resource.get_by_mrid(self, mrid)

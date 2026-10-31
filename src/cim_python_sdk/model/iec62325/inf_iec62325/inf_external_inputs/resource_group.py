"""CIM class ResourceGroup (TC57CIM/IEC62325/InfIEC62325/InfExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.resource_group_req import (
        ResourceGroupReq,
    )
    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource


class ResourceGroup(IdentifiedObject):
    """A logical grouping of resources that are used to model location of types of requirements
    for ancillary services such as spinning reserve zones, regulation zones, etc."""

    __slots__ = ("_registered_resources", "_resource_group_reqs", "status", "type")

    type: str | None
    status: Status | None

    registered_resources: Many[RegisteredResource] = Many(
        EndMeta(
            name="registered_resources",
            cim_role="RegisteredResources",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=True,
            lower=1,
            upper=None,
            inverse="resource_groups",
            aggregation="none",
        )
    )
    resource_group_reqs: Many[ResourceGroupReq] = Many(
        EndMeta(
            name="resource_group_reqs",
            cim_role="ResourceGroupReqs",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.resource_group_req:ResourceGroupReq",
            many=True,
            lower=0,
            upper=None,
            inverse="resource_group",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceGroup",
        package="TC57CIM/IEC62325/InfIEC62325/InfExternalInputs",
        guid="{91E0A619-9EE5-4067-842E-1D325BBDF7ED}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            registered_resources.meta,
            resource_group_reqs.meta,
        ),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        status: Status | None = None,
        registered_resources: Iterable[RegisteredResource] | None = None,
        resource_group_reqs: Iterable[ResourceGroupReq] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.status = status
        if registered_resources is not None:
            ResourceGroup.registered_resources.extend(self, registered_resources)
        if resource_group_reqs is not None:
            ResourceGroup.resource_group_reqs.extend(self, resource_group_reqs)

    def add_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return ResourceGroup.registered_resources.add(self, registered_resource)

    def remove_registered_resource(self, registered_resource: RegisteredResource) -> Self:
        return ResourceGroup.registered_resources.remove(self, registered_resource)

    def clear_registered_resources(self) -> Self:
        return ResourceGroup.registered_resources.clear(self)

    def num_registered_resource(self) -> int:
        return ResourceGroup.registered_resources.count(self)

    def get_registered_resource_by_mrid(self, mrid: str) -> RegisteredResource | None:
        return ResourceGroup.registered_resources.get_by_mrid(self, mrid)

    def add_resource_group_req(self, resource_group_req: ResourceGroupReq) -> Self:
        return ResourceGroup.resource_group_reqs.add(self, resource_group_req)

    def remove_resource_group_req(self, resource_group_req: ResourceGroupReq) -> Self:
        return ResourceGroup.resource_group_reqs.remove(self, resource_group_req)

    def clear_resource_group_reqs(self) -> Self:
        return ResourceGroup.resource_group_reqs.clear(self)

    def num_resource_group_req(self) -> int:
        return ResourceGroup.resource_group_reqs.count(self)

    def get_resource_group_req_by_mrid(self, mrid: str) -> ResourceGroupReq | None:
        return ResourceGroup.resource_group_reqs.get_by_mrid(self, mrid)

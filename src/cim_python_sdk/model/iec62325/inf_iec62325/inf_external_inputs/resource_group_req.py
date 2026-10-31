"""CIM class ResourceGroupReq (TC57CIM/IEC62325/InfIEC62325/InfExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.resource_group import (
        ResourceGroup,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO


class ResourceGroupReq(IdentifiedObject):
    """Ancillary service requirements for a market."""

    __slots__ = ("_resource_group", "_rtos")

    rtos: Many[RTO] = Many(
        EndMeta(
            name="rtos",
            cim_role="RTOs",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=True,
            lower=0,
            upper=None,
            inverse="resource_group_reqs",
            aggregation="none",
        )
    )
    resource_group: One[ResourceGroup] = One(
        EndMeta(
            name="resource_group",
            cim_role="ResourceGroup",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_external_inputs.resource_group:ResourceGroup",
            many=False,
            lower=1,
            upper=1,
            inverse="resource_group_reqs",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ResourceGroupReq",
        package="TC57CIM/IEC62325/InfIEC62325/InfExternalInputs",
        guid="{0E838216-C7A6-456b-B0CA-4132390C7B42}",
        ends=(
            rtos.meta,
            resource_group.meta,
        ),
    )

    def __init__(
        self,
        *,
        rtos: Iterable[RTO] | None = None,
        resource_group: ResourceGroup | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if rtos is not None:
            ResourceGroupReq.rtos.extend(self, rtos)
        if resource_group is not None:
            self.resource_group = resource_group

    def add_rto(self, rto: RTO) -> Self:
        return ResourceGroupReq.rtos.add(self, rto)

    def remove_rto(self, rto: RTO) -> Self:
        return ResourceGroupReq.rtos.remove(self, rto)

    def clear_rtos(self) -> Self:
        return ResourceGroupReq.rtos.clear(self)

    def num_rto(self) -> int:
        return ResourceGroupReq.rtos.count(self)

    def get_rto_by_mrid(self, mrid: str) -> RTO | None:
        return ResourceGroupReq.rtos.get_by_mrid(self, mrid)

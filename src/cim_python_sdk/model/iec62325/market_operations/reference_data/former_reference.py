"""CIM class FormerReference (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource


class FormerReference(IdentifiedObject):
    """Used to indicate former references to the same piece of equipment. The ID, name, and
    effectivity dates are utilized."""

    __slots__ = ("_registered_resource",)

    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=1,
            upper=1,
            inverse="former_reference",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FormerReference",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{22991F8A-9D03-4aa7-B881-782BE244E6A6}",
        ends=(registered_resource.meta,),
    )

    def __init__(
        self,
        *,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if registered_resource is not None:
            self.registered_resource = registered_resource

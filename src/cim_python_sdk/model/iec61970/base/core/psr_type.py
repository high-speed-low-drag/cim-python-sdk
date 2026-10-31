"""CIM class PSRType (TC57CIM/IEC61970/Base/Core). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource


class PSRType(IdentifiedObject):
    """Classifying instances of the same class, e.g. overhead and underground ACLineSegments.
    This classification mechanism is intended to provide flexibility outside the scope of
    this document, i.e. provide customisation that is non standard."""

    __slots__ = ("_power_system_resources",)

    power_system_resources: Many[PowerSystemResource] = Many(
        EndMeta(
            name="power_system_resources",
            cim_role="PowerSystemResources",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=True,
            lower=0,
            upper=None,
            inverse="psr_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="PSRType",
        package="TC57CIM/IEC61970/Base/Core",
        guid="{CF59539F-A910-4af6-A84D-A52BBA7300CB}",
        ends=(power_system_resources.meta,),
    )

    def __init__(
        self,
        *,
        power_system_resources: Iterable[PowerSystemResource] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if power_system_resources is not None:
            PSRType.power_system_resources.extend(self, power_system_resources)

    def add_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return PSRType.power_system_resources.add(self, power_system_resource)

    def remove_power_system_resource(self, power_system_resource: PowerSystemResource) -> Self:
        return PSRType.power_system_resources.remove(self, power_system_resource)

    def clear_power_system_resources(self) -> Self:
        return PSRType.power_system_resources.clear(self)

    def num_power_system_resource(self) -> int:
        return PSRType.power_system_resources.count(self)

    def get_power_system_resource_by_mrid(self, mrid: str) -> PowerSystemResource | None:
        return PSRType.power_system_resources.get_by_mrid(self, mrid)

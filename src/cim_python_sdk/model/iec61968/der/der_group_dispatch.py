"""CIM class DERGroupDispatch (TC57CIM/IEC61968/DER). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.end_device_group import EndDeviceGroup


class DERGroupDispatch(IdentifiedObject):
    """Specifies the capabilities of the DER Group that are to be dispatched according to a
    schedule. Each dispatch identifies a DER Group and the specific monitorable parameter to
    be dispatched over a specific time interval."""

    __slots__ = ("_end_device_group",)

    end_device_group: Many[EndDeviceGroup] = Many(
        EndMeta(
            name="end_device_group",
            cim_role="EndDeviceGroup",
            target="cim_python_sdk.model.iec61968.metering.end_device_group:EndDeviceGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="der_group_dispatch",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="DERGroupDispatch",
        package="TC57CIM/IEC61968/DER",
        guid="{83D2BB12-0256-4239-8034-FDF696C945EB}",
        ends=(end_device_group.meta,),
    )

    def __init__(
        self,
        *,
        end_device_group: Iterable[EndDeviceGroup] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if end_device_group is not None:
            DERGroupDispatch.end_device_group.extend(self, end_device_group)

    def add_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return DERGroupDispatch.end_device_group.add(self, end_device_group)

    def remove_end_device_group(self, end_device_group: EndDeviceGroup) -> Self:
        return DERGroupDispatch.end_device_group.remove(self, end_device_group)

    def clear_end_device_group(self) -> Self:
        return DERGroupDispatch.end_device_group.clear(self)

    def num_end_device_group(self) -> int:
        return DERGroupDispatch.end_device_group.count(self)

    def get_end_device_group_by_mrid(self, mrid: str) -> EndDeviceGroup | None:
        return DERGroupDispatch.end_device_group.get_by_mrid(self, mrid)

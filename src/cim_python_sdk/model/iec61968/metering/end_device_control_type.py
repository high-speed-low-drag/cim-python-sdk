"""CIM class EndDeviceControlType (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.metering.end_device_control import EndDeviceControl


class EndDeviceControlType(IdentifiedObject):
    """Detailed description for a control produced by an end device. Values in attributes allow
    for creation of recommended codes to be used for identifying end device controls as
    follows: <type>.<domain>.<subDomain>.<eventOrAction>."""

    __slots__ = ("_end_device_controls", "domain", "event_or_action", "sub_domain", "type")

    type: str | None
    domain: str | None
    sub_domain: str | None
    event_or_action: str | None

    end_device_controls: Many[EndDeviceControl] = Many(
        EndMeta(
            name="end_device_controls",
            cim_role="EndDeviceControls",
            target="cim_python_sdk.model.iec61968.metering.end_device_control:EndDeviceControl",
            many=True,
            lower=0,
            upper=None,
            inverse="end_device_control_type",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EndDeviceControlType",
        package="TC57CIM/IEC61968/Metering",
        guid="{89967067-2948-49a7-80D8-5CAEE2182D20}",
        attributes=(
            AttrMeta("type", "type", "str", 0, 1, "primitive"),
            AttrMeta("domain", "domain", "str", 0, 1, "primitive"),
            AttrMeta("sub_domain", "subDomain", "str", 0, 1, "primitive"),
            AttrMeta("event_or_action", "eventOrAction", "str", 0, 1, "primitive"),
        ),
        ends=(end_device_controls.meta,),
    )

    def __init__(
        self,
        *,
        type: str | None = None,
        domain: str | None = None,
        sub_domain: str | None = None,
        event_or_action: str | None = None,
        end_device_controls: Iterable[EndDeviceControl] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.type = type
        self.domain = domain
        self.sub_domain = sub_domain
        self.event_or_action = event_or_action
        if end_device_controls is not None:
            EndDeviceControlType.end_device_controls.extend(self, end_device_controls)

    def add_end_device_control(self, end_device_control: EndDeviceControl) -> Self:
        return EndDeviceControlType.end_device_controls.add(self, end_device_control)

    def remove_end_device_control(self, end_device_control: EndDeviceControl) -> Self:
        return EndDeviceControlType.end_device_controls.remove(self, end_device_control)

    def clear_end_device_controls(self) -> Self:
        return EndDeviceControlType.end_device_controls.clear(self)

    def num_end_device_control(self) -> int:
        return EndDeviceControlType.end_device_controls.count(self)

    def get_end_device_control_by_mrid(self, mrid: str) -> EndDeviceControl | None:
        return EndDeviceControlType.end_device_controls.get_by_mrid(self, mrid)

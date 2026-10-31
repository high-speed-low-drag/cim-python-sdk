"""CIM class PanDisplay (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.metering.end_device_action import EndDeviceAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.transmission_mode_kind import TransmissionModeKind


class PanDisplay(EndDeviceAction):
    """PAN action/command used to issue the displaying of text messages on PAN devices."""

    __slots__ = ("confirmation_required", "priority", "text_message", "transmission_mode")

    confirmation_required: bool | None
    priority: str | None
    text_message: str | None
    transmission_mode: TransmissionModeKind | None

    _cim_meta = ClassMeta(
        cim_name="PanDisplay",
        package="TC57CIM/IEC61968/Metering",
        guid="{C12437E2-EA2C-4827-8251-42CF56B2C7A3}",
        attributes=(
            AttrMeta("confirmation_required", "confirmationRequired", "bool", 0, 1, "primitive"),
            AttrMeta("priority", "priority", "str", 0, 1, "primitive"),
            AttrMeta("text_message", "textMessage", "str", 0, 1, "primitive"),
            AttrMeta(
                "transmission_mode", "transmissionMode", "TransmissionModeKind", 0, 1, "enumeration"
            ),
        ),
    )

    def __init__(
        self,
        *,
        confirmation_required: bool | None = None,
        priority: str | None = None,
        text_message: str | None = None,
        transmission_mode: TransmissionModeKind | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.confirmation_required = confirmation_required
        self.priority = priority
        self.text_message = text_message
        self.transmission_mode = transmission_mode

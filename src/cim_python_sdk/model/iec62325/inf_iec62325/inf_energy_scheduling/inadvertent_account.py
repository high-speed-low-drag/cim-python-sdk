"""CIM class InadvertentAccount (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area import (
        SubControlArea,
    )


class InadvertentAccount(CimObject):
    """An account for tracking inadvertent interchange versus time for each control area. A
    control area may have more than one inadvertent account in order to track inadvertent
    over one or more specific tie points in addition to the usual overall net inadvertent.
    Separate accounts would also be used to track designated time periods, such as on-peak
    and off-peak."""

    __slots__ = ("_sub_control_area",)

    sub_control_area: One[SubControlArea] = One(
        EndMeta(
            name="sub_control_area",
            cim_role="SubControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.sub_control_area:SubControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="inadvertent_account",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="InadvertentAccount",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{377EDC82-091E-4abf-8A72-D78C0D98C4D0}",
        ends=(sub_control_area.meta,),
    )

    def __init__(
        self,
        *,
        sub_control_area: SubControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if sub_control_area is not None:
            self.sub_control_area = sub_control_area

"""CIM class ComFunction (TC57CIM/IEC61968/Metering). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.metering.end_device_function import EndDeviceFunction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.metering.com_direction_kind import ComDirectionKind
    from cim_python_sdk.model.iec61968.metering.com_module import ComModule
    from cim_python_sdk.model.iec61968.metering.com_technology_kind import ComTechnologyKind


class ComFunction(EndDeviceFunction):
    """Communication function of communication equipment or a device such as a meter."""

    __slots__ = ("_com_module", "amr_address", "amr_router", "direction", "technology")

    amr_address: str | None
    amr_router: str | None
    direction: ComDirectionKind | None
    technology: ComTechnologyKind | None

    com_module: One[ComModule] = One(
        EndMeta(
            name="com_module",
            cim_role="ComModule",
            target="cim_python_sdk.model.iec61968.metering.com_module:ComModule",
            many=False,
            lower=0,
            upper=1,
            inverse="com_functions",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ComFunction",
        package="TC57CIM/IEC61968/Metering",
        guid="{356285E8-FCBD-4668-B5C4-834A6952A941}",
        attributes=(
            AttrMeta("amr_address", "amrAddress", "str", 0, 1, "primitive"),
            AttrMeta("amr_router", "amrRouter", "str", 0, 1, "primitive"),
            AttrMeta("direction", "direction", "ComDirectionKind", 0, 1, "enumeration"),
            AttrMeta("technology", "technology", "ComTechnologyKind", 0, 1, "enumeration"),
        ),
        ends=(com_module.meta,),
    )

    def __init__(
        self,
        *,
        amr_address: str | None = None,
        amr_router: str | None = None,
        direction: ComDirectionKind | None = None,
        technology: ComTechnologyKind | None = None,
        com_module: ComModule | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.amr_address = amr_address
        self.amr_router = amr_router
        self.direction = direction
        self.technology = technology
        if com_module is not None:
            self.com_module = com_module

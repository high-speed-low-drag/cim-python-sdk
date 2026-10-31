"""CIM class TransferInterface (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transfer_interface_solution import (
        TransferInterfaceSolution,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area import (
        HostControlArea,
    )


class TransferInterface(IdentifiedObject):
    """A Transfer Interface is made up of branches such as transmission lines and transformers."""

    __slots__ = ("_host_control_area", "_transfer_interface_solution")

    host_control_area: One[HostControlArea] = One(
        EndMeta(
            name="host_control_area",
            cim_role="HostControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area:HostControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="transfer_interface",
            aggregation="none",
        )
    )
    transfer_interface_solution: One[TransferInterfaceSolution] = One(
        EndMeta(
            name="transfer_interface_solution",
            cim_role="TransferInterfaceSolution",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transfer_interface_solution:TransferInterfaceSolution",
            many=False,
            lower=1,
            upper=1,
            inverse="transfer_interface",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransferInterface",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{365B4939-767B-4501-8C3C-42C0EDA20A53}",
        ends=(
            host_control_area.meta,
            transfer_interface_solution.meta,
        ),
    )

    def __init__(
        self,
        *,
        host_control_area: HostControlArea | None = None,
        transfer_interface_solution: TransferInterfaceSolution | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if host_control_area is not None:
            self.host_control_area = host_control_area
        if transfer_interface_solution is not None:
            self.transfer_interface_solution = transfer_interface_solution

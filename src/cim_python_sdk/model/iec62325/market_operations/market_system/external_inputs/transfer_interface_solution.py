"""CIM class TransferInterfaceSolution (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transfer_interface import (
        TransferInterface,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_contingency import (
        MktContingency,
    )


class TransferInterfaceSolution(CimObject):
    """TNA Interface Definitions from OPF for VSA."""

    __slots__ = (
        "_mkt_contingency_a",
        "_mkt_contingency_b",
        "_transfer_interface",
        "interface_margin",
        "post_transfer_mw",
        "transfer_limit",
    )

    interface_margin: float | None
    transfer_limit: float | None
    post_transfer_mw: float | None

    mkt_contingency_b: One[MktContingency] = One(
        EndMeta(
            name="mkt_contingency_b",
            cim_role="MktContingencyB",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_contingency:MktContingency",
            many=False,
            lower=0,
            upper=1,
            inverse="transfer_interface_solution_b",
            aggregation="none",
        )
    )
    transfer_interface: One[TransferInterface] = One(
        EndMeta(
            name="transfer_interface",
            cim_role="TransferInterface",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.transfer_interface:TransferInterface",
            many=False,
            lower=1,
            upper=1,
            inverse="transfer_interface_solution",
            aggregation="none",
        )
    )
    mkt_contingency_a: One[MktContingency] = One(
        EndMeta(
            name="mkt_contingency_a",
            cim_role="MktContingencyA",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.mkt_contingency:MktContingency",
            many=False,
            lower=0,
            upper=1,
            inverse="transfer_interface_solution_a",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransferInterfaceSolution",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{FCCDF1D2-4051-4397-837C-9CF9A31A13B6}",
        attributes=(
            AttrMeta("interface_margin", "interfaceMargin", "float", 0, 1, "primitive"),
            AttrMeta("transfer_limit", "transferLimit", "float", 0, 1, "primitive"),
            AttrMeta("post_transfer_mw", "postTransferMW", "float", 0, 1, "primitive"),
        ),
        ends=(
            mkt_contingency_b.meta,
            transfer_interface.meta,
            mkt_contingency_a.meta,
        ),
    )

    def __init__(
        self,
        *,
        interface_margin: float | None = None,
        transfer_limit: float | None = None,
        post_transfer_mw: float | None = None,
        mkt_contingency_b: MktContingency | None = None,
        transfer_interface: TransferInterface | None = None,
        mkt_contingency_a: MktContingency | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.interface_margin = interface_margin
        self.transfer_limit = transfer_limit
        self.post_transfer_mw = post_transfer_mw
        if mkt_contingency_b is not None:
            self.mkt_contingency_b = mkt_contingency_b
        if transfer_interface is not None:
            self.transfer_interface = transfer_interface
        if mkt_contingency_a is not None:
            self.mkt_contingency_a = mkt_contingency_a

"""CIM class TransmissionRightChain (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right import (
        ContractRight,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO


class TransmissionRightChain(IdentifiedObject):
    """Allows chaining of TransmissionContractRights. Many individual contract rights can be
    included in the definition of a TransmissionRightChain. A TransmissionRightChain is also
    defined as a TransmissionContractRight itself."""

    __slots__ = ("_chain_contract_right", "_ind_contract_right", "_rto")

    chain_contract_right: One[ContractRight] = One(
        EndMeta(
            name="chain_contract_right",
            cim_role="Chain_ContractRight",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right:ContractRight",
            many=False,
            lower=1,
            upper=1,
            inverse="chain_transmission_right_chain",
            aggregation="none",
        )
    )
    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=1,
            upper=1,
            inverse="transmission_right_chain",
            aggregation="none",
        )
    )
    ind_contract_right: Many[ContractRight] = Many(
        EndMeta(
            name="ind_contract_right",
            cim_role="Ind_ContractRight",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right:ContractRight",
            many=True,
            lower=1,
            upper=None,
            inverse="ind_transmission_right_chain",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransmissionRightChain",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{7211DE22-106C-4bd9-BCF2-51DB34A7FDBC}",
        ends=(
            chain_contract_right.meta,
            rto.meta,
            ind_contract_right.meta,
        ),
    )

    def __init__(
        self,
        *,
        chain_contract_right: ContractRight | None = None,
        rto: RTO | None = None,
        ind_contract_right: Iterable[ContractRight] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if chain_contract_right is not None:
            self.chain_contract_right = chain_contract_right
        if rto is not None:
            self.rto = rto
        if ind_contract_right is not None:
            TransmissionRightChain.ind_contract_right.extend(self, ind_contract_right)

    def add_ind_contract_right(self, ind_contract_right: ContractRight) -> Self:
        return TransmissionRightChain.ind_contract_right.add(self, ind_contract_right)

    def remove_ind_contract_right(self, ind_contract_right: ContractRight) -> Self:
        return TransmissionRightChain.ind_contract_right.remove(self, ind_contract_right)

    def clear_ind_contract_right(self) -> Self:
        return TransmissionRightChain.ind_contract_right.clear(self)

    def num_ind_contract_right(self) -> int:
        return TransmissionRightChain.ind_contract_right.count(self)

    def get_ind_contract_right_by_mrid(self, mrid: str) -> ContractRight | None:
        return TransmissionRightChain.ind_contract_right.get_by_mrid(self, mrid)

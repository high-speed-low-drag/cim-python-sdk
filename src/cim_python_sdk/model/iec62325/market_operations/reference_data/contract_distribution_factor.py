"""CIM class ContractDistributionFactor (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right import (
        ContractRight,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class ContractDistributionFactor(CimObject):
    """Distribution among resources at the sink point or source point."""

    __slots__ = (
        "_flowgate",
        "_registered_resource",
        "_transmission_contract_right",
        "factor",
        "sink_flag",
        "source_flag",
    )

    factor: float | None
    source_flag: YesNo | None
    sink_flag: YesNo | None

    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=0,
            upper=1,
            inverse="contract_distribution_factor",
            aggregation="none",
        )
    )
    transmission_contract_right: One[ContractRight] = One(
        EndMeta(
            name="transmission_contract_right",
            cim_role="TransmissionContractRight",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right:ContractRight",
            many=False,
            lower=0,
            upper=1,
            inverse="contract_distribution_factor",
            aggregation="none",
        )
    )
    registered_resource: One[RegisteredResource] = One(
        EndMeta(
            name="registered_resource",
            cim_role="RegisteredResource",
            target="cim_python_sdk.model.iec62325.market_common.registered_resource:RegisteredResource",
            many=False,
            lower=0,
            upper=1,
            inverse="contract_distribution_factor",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ContractDistributionFactor",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{55172C10-DFAF-4d6b-9240-8C107107B9C0}",
        attributes=(
            AttrMeta("factor", "factor", "float", 0, 1, "primitive"),
            AttrMeta("source_flag", "sourceFlag", "YesNo", 0, 1, "enumeration"),
            AttrMeta("sink_flag", "sinkFlag", "YesNo", 0, 1, "enumeration"),
        ),
        ends=(
            flowgate.meta,
            transmission_contract_right.meta,
            registered_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        factor: float | None = None,
        source_flag: YesNo | None = None,
        sink_flag: YesNo | None = None,
        flowgate: Flowgate | None = None,
        transmission_contract_right: ContractRight | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.factor = factor
        self.source_flag = source_flag
        self.sink_flag = sink_flag
        if flowgate is not None:
            self.flowgate = flowgate
        if transmission_contract_right is not None:
            self.transmission_contract_right = transmission_contract_right
        if registered_resource is not None:
            self.registered_resource = registered_resource

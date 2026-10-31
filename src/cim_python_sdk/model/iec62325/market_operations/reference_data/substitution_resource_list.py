"""CIM class SubstitutionResourceList (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_common.registered_resource import RegisteredResource
    from cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right import (
        ContractRight,
    )


class SubstitutionResourceList(CimObject):
    """List of resources that can be substituted for within the bounds of a Contract
    definition. This class has a precedence and a resource."""

    __slots__ = ("_registered_resource", "_transmission_contract_right", "precedence")

    precedence: int | None

    transmission_contract_right: One[ContractRight] = One(
        EndMeta(
            name="transmission_contract_right",
            cim_role="TransmissionContractRight",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right:ContractRight",
            many=False,
            lower=0,
            upper=1,
            inverse="substitution_resource_list",
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
            inverse="substitution_resource_list",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SubstitutionResourceList",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{CF27F874-FDF5-429e-8D90-5A174497999A}",
        attributes=(AttrMeta("precedence", "precedence", "int", 0, 1, "primitive"),),
        ends=(
            transmission_contract_right.meta,
            registered_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        precedence: int | None = None,
        transmission_contract_right: ContractRight | None = None,
        registered_resource: RegisteredResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.precedence = precedence
        if transmission_contract_right is not None:
            self.transmission_contract_right = transmission_contract_right
        if registered_resource is not None:
            self.registered_resource = registered_resource

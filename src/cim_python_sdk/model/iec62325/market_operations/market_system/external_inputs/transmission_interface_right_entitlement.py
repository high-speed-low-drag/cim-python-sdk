"""CIM class TransmissionInterfaceRightEntitlement (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right import (
        ContractRight,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class TransmissionInterfaceRightEntitlement(CimObject):
    """This is formally called the branch group ETC/TOR entitlement with the inclusion of CVR
    as ETC. This could be also used to represent the TR entitlement on a POR/POD."""

    __slots__ = (
        "_contract_right",
        "_flowgate",
        "entitlement",
        "pod",
        "por",
        "start_operating_date",
    )

    entitlement: float | None
    pod: str | None
    por: str | None
    start_operating_date: _dt.datetime | None

    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=0,
            upper=1,
            inverse="tranmission_right_entitlement",
            aggregation="none",
        )
    )
    contract_right: One[ContractRight] = One(
        EndMeta(
            name="contract_right",
            cim_role="ContractRight",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right:ContractRight",
            many=False,
            lower=1,
            upper=1,
            inverse="transmission_interface_entitlement",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransmissionInterfaceRightEntitlement",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{7B694F5B-4F2B-483e-B5ED-D993101EEF9D}",
        attributes=(
            AttrMeta("entitlement", "entitlement", "float", 0, 1, "primitive"),
            AttrMeta("pod", "POD", "str", 0, 1, "primitive"),
            AttrMeta("por", "POR", "str", 0, 1, "primitive"),
            AttrMeta("start_operating_date", "startOperatingDate", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            flowgate.meta,
            contract_right.meta,
        ),
    )

    def __init__(
        self,
        *,
        entitlement: float | None = None,
        pod: str | None = None,
        por: str | None = None,
        start_operating_date: _dt.datetime | None = None,
        flowgate: Flowgate | None = None,
        contract_right: ContractRight | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.entitlement = entitlement
        self.pod = pod
        self.por = por
        self.start_operating_date = start_operating_date
        if flowgate is not None:
            self.flowgate = flowgate
        if contract_right is not None:
            self.contract_right = contract_right

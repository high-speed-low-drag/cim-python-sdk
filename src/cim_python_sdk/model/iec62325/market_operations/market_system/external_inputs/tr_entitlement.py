"""CIM class TREntitlement (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right import (
        ContractRight,
    )


class TREntitlement(CimObject):
    """A Transmission Right(TR) can be a chain of TR's or on individual.

    When a transmission right is not a chain, this is formally the ETC/TOR Entitlement for
    each ETC/TOR contract with the inclusion of CVR(Converted Rights) as an ETC. This is the
    sum of all entitlements on all related transmission interfaces for the same TR.

    When TR is a chain, its entitlement is the minimum of all entitlements for the
    individual TRs in the chain."""

    __slots__ = ("_transmission_contract_right", "entitlement", "start_operating_date")

    entitlement: float | None
    start_operating_date: _dt.datetime | None

    transmission_contract_right: One[ContractRight] = One(
        EndMeta(
            name="transmission_contract_right",
            cim_role="TransmissionContractRight",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.contract_right:ContractRight",
            many=False,
            lower=1,
            upper=1,
            inverse="tr_entitlement",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TREntitlement",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{B1B279F7-7A35-4cca-BCD5-612C161CAD68}",
        attributes=(
            AttrMeta("entitlement", "entitlement", "float", 0, 1, "primitive"),
            AttrMeta("start_operating_date", "startOperatingDate", "datetime", 0, 1, "primitive"),
        ),
        ends=(transmission_contract_right.meta,),
    )

    def __init__(
        self,
        *,
        entitlement: float | None = None,
        start_operating_date: _dt.datetime | None = None,
        transmission_contract_right: ContractRight | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.entitlement = entitlement
        self.start_operating_date = start_operating_date
        if transmission_contract_right is not None:
            self.transmission_contract_right = transmission_contract_right

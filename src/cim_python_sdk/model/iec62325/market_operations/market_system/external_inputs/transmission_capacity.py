"""CIM class TransmissionCapacity (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.generic_constraints import (
        GenericConstraints,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class TransmissionCapacity(CimObject):
    """This class models the transmission (either a transmission interface or a POR/POD pair)
    capacity including Total Transfer Capacity (TTC), Operating Transfer Capacity (OTC), and
    Capacity Benefit Margin (CBM)."""

    __slots__ = (
        "_flowgate",
        "_generic_constraints",
        "capacity_benefit_margin",
        "operational_transmission_capacity",
        "ot_cemergency",
        "otc15min_emergency",
        "pod",
        "por",
        "start_operating_date",
        "total_transmission_capacity",
    )

    capacity_benefit_margin: float | None
    operational_transmission_capacity: float | None
    otc15min_emergency: float | None
    ot_cemergency: float | None
    pod: str | None
    por: str | None
    start_operating_date: _dt.datetime | None
    total_transmission_capacity: float | None

    generic_constraints: One[GenericConstraints] = One(
        EndMeta(
            name="generic_constraints",
            cim_role="GenericConstraints",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.generic_constraints:GenericConstraints",
            many=False,
            lower=0,
            upper=1,
            inverse="transmission_capacity",
            aggregation="none",
        )
    )
    flowgate: One[Flowgate] = One(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=False,
            lower=0,
            upper=1,
            inverse="transmission_capacity",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransmissionCapacity",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{2F86A45A-5879-4e81-A18E-AC2BE1406190}",
        attributes=(
            AttrMeta(
                "capacity_benefit_margin", "capacityBenefitMargin", "float", 0, 1, "primitive"
            ),
            AttrMeta(
                "operational_transmission_capacity",
                "operationalTransmissionCapacity",
                "float",
                0,
                1,
                "primitive",
            ),
            AttrMeta("otc15min_emergency", "OTC15min_emergency", "float", 0, 1, "primitive"),
            AttrMeta("ot_cemergency", "OTCemergency", "float", 0, 1, "primitive"),
            AttrMeta("pod", "POD", "str", 0, 1, "primitive"),
            AttrMeta("por", "POR", "str", 0, 1, "primitive"),
            AttrMeta("start_operating_date", "startOperatingDate", "datetime", 0, 1, "primitive"),
            AttrMeta(
                "total_transmission_capacity",
                "totalTransmissionCapacity",
                "float",
                0,
                1,
                "primitive",
            ),
        ),
        ends=(
            generic_constraints.meta,
            flowgate.meta,
        ),
    )

    def __init__(
        self,
        *,
        capacity_benefit_margin: float | None = None,
        operational_transmission_capacity: float | None = None,
        otc15min_emergency: float | None = None,
        ot_cemergency: float | None = None,
        pod: str | None = None,
        por: str | None = None,
        start_operating_date: _dt.datetime | None = None,
        total_transmission_capacity: float | None = None,
        generic_constraints: GenericConstraints | None = None,
        flowgate: Flowgate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.capacity_benefit_margin = capacity_benefit_margin
        self.operational_transmission_capacity = operational_transmission_capacity
        self.otc15min_emergency = otc15min_emergency
        self.ot_cemergency = ot_cemergency
        self.pod = pod
        self.por = por
        self.start_operating_date = start_operating_date
        self.total_transmission_capacity = total_transmission_capacity
        if generic_constraints is not None:
            self.generic_constraints = generic_constraints
        if flowgate is not None:
            self.flowgate = flowgate

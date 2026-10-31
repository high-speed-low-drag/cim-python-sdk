"""CIM class SecurityConstraints (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid import (
        GeneratingBid,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO


class SecurityConstraints(IdentifiedObject):
    """Typical for regional transmission operators (RTOs), these constraints include
    transmission as well as generation group constraints identified in both base case and
    critical contingency cases."""

    __slots__ = ("_flowgate", "_generating_bid", "_rto", "actual_mw", "max_mw", "min_mw")

    min_mw: float | None  # ActivePower
    max_mw: float | None  # ActivePower
    actual_mw: float | None  # ActivePower

    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=0,
            upper=1,
            inverse="security_constraints",
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
            inverse="security_constraints",
            aggregation="none",
        )
    )
    generating_bid: One[GeneratingBid] = One(
        EndMeta(
            name="generating_bid",
            cim_role="GeneratingBid",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.generating_bid:GeneratingBid",
            many=False,
            lower=0,
            upper=1,
            inverse="security_constraints",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SecurityConstraints",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{873BBE76-79B7-4f36-AEB3-B8B95953B700}",
        attributes=(
            AttrMeta("min_mw", "minMW", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_mw", "maxMW", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("actual_mw", "actualMW", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            rto.meta,
            flowgate.meta,
            generating_bid.meta,
        ),
    )

    def __init__(
        self,
        *,
        min_mw: float | None = None,
        max_mw: float | None = None,
        actual_mw: float | None = None,
        rto: RTO | None = None,
        flowgate: Flowgate | None = None,
        generating_bid: GeneratingBid | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.min_mw = min_mw
        self.max_mw = max_mw
        self.actual_mw = actual_mw
        if rto is not None:
            self.rto = rto
        if flowgate is not None:
            self.flowgate = flowgate
        if generating_bid is not None:
            self.generating_bid = generating_bid

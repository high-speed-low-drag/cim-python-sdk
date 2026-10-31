"""CIM class MSSAggregation (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.reference_data.metered_sub_system import (
        MeteredSubSystem,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.rto import RTO


class MSSAggregation(IdentifiedObject):
    """Metered Sub-System aggregation of MSS Zones."""

    __slots__ = (
        "_metered_sub_system",
        "_rto",
        "cost_recovery",
        "gross_settlement",
        "ignore_losses",
        "ignore_marginal_losses",
        "load_following",
        "ruc_procurement",
    )

    cost_recovery: YesNo | None
    gross_settlement: YesNo | None
    ignore_losses: YesNo | None
    ignore_marginal_losses: YesNo | None
    load_following: YesNo | None
    ruc_procurement: YesNo | None

    rto: One[RTO] = One(
        EndMeta(
            name="rto",
            cim_role="RTO",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.rto:RTO",
            many=False,
            lower=1,
            upper=1,
            inverse="mss_aggregation",
            aggregation="none",
        )
    )
    metered_sub_system: Many[MeteredSubSystem] = Many(
        EndMeta(
            name="metered_sub_system",
            cim_role="MeteredSubSystem",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.metered_sub_system:MeteredSubSystem",
            many=True,
            lower=1,
            upper=None,
            inverse="mss_aggregation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MSSAggregation",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{48D5BEFC-9AF1-46b6-8288-509365AD7053}",
        attributes=(
            AttrMeta("cost_recovery", "costRecovery", "YesNo", 0, 1, "enumeration"),
            AttrMeta("gross_settlement", "grossSettlement", "YesNo", 0, 1, "enumeration"),
            AttrMeta("ignore_losses", "ignoreLosses", "YesNo", 0, 1, "enumeration"),
            AttrMeta(
                "ignore_marginal_losses", "ignoreMarginalLosses", "YesNo", 0, 1, "enumeration"
            ),
            AttrMeta("load_following", "loadFollowing", "YesNo", 0, 1, "enumeration"),
            AttrMeta("ruc_procurement", "rucProcurement", "YesNo", 0, 1, "enumeration"),
        ),
        ends=(
            rto.meta,
            metered_sub_system.meta,
        ),
    )

    def __init__(
        self,
        *,
        cost_recovery: YesNo | None = None,
        gross_settlement: YesNo | None = None,
        ignore_losses: YesNo | None = None,
        ignore_marginal_losses: YesNo | None = None,
        load_following: YesNo | None = None,
        ruc_procurement: YesNo | None = None,
        rto: RTO | None = None,
        metered_sub_system: Iterable[MeteredSubSystem] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cost_recovery = cost_recovery
        self.gross_settlement = gross_settlement
        self.ignore_losses = ignore_losses
        self.ignore_marginal_losses = ignore_marginal_losses
        self.load_following = load_following
        self.ruc_procurement = ruc_procurement
        if rto is not None:
            self.rto = rto
        if metered_sub_system is not None:
            MSSAggregation.metered_sub_system.extend(self, metered_sub_system)

    def add_metered_sub_system(self, metered_sub_system: MeteredSubSystem) -> Self:
        return MSSAggregation.metered_sub_system.add(self, metered_sub_system)

    def remove_metered_sub_system(self, metered_sub_system: MeteredSubSystem) -> Self:
        return MSSAggregation.metered_sub_system.remove(self, metered_sub_system)

    def clear_metered_sub_system(self) -> Self:
        return MSSAggregation.metered_sub_system.clear(self)

    def num_metered_sub_system(self) -> int:
        return MSSAggregation.metered_sub_system.count(self)

    def get_metered_sub_system_by_mrid(self, mrid: str) -> MeteredSubSystem | None:
        return MSSAggregation.metered_sub_system.get_by_mrid(self, mrid)

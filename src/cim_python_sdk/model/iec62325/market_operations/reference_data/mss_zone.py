"""CIM class MSSZone (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec62325.market_operations.reference_data.aggregate_node import (
    AggregateNode,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.yes_no import YesNo
    from cim_python_sdk.model.iec62325.market_operations.reference_data.metered_sub_system import (
        MeteredSubSystem,
    )


class MSSZone(AggregateNode):
    """Model to define a zone within a Metered Sub System."""

    __slots__ = ("_metered_sub_system", "ignore_losses", "loss_factor", "ruc_gross_settlement")

    ignore_losses: YesNo | None
    loss_factor: float | None
    ruc_gross_settlement: YesNo | None

    metered_sub_system: One[MeteredSubSystem] = One(
        EndMeta(
            name="metered_sub_system",
            cim_role="MeteredSubSystem",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.metered_sub_system:MeteredSubSystem",
            many=False,
            lower=0,
            upper=1,
            inverse="mss_zone",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MSSZone",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{E27C18F9-46D2-495f-B67A-8548DBCA38F9}",
        attributes=(
            AttrMeta("ignore_losses", "ignoreLosses", "YesNo", 0, 1, "enumeration"),
            AttrMeta("loss_factor", "lossFactor", "float", 0, 1, "primitive"),
            AttrMeta("ruc_gross_settlement", "rucGrossSettlement", "YesNo", 0, 1, "enumeration"),
        ),
        ends=(metered_sub_system.meta,),
    )

    def __init__(
        self,
        *,
        ignore_losses: YesNo | None = None,
        loss_factor: float | None = None,
        ruc_gross_settlement: YesNo | None = None,
        metered_sub_system: MeteredSubSystem | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ignore_losses = ignore_losses
        self.loss_factor = loss_factor
        self.ruc_gross_settlement = ruc_gross_settlement
        if metered_sub_system is not None:
            self.metered_sub_system = metered_sub_system

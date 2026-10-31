"""CIM class ReserveDemandCurve (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.as_requirements import (
        ASRequirements,
    )
    from cim_python_sdk.model.iec62325.market_operations.mkt_domain.reserve_requirement_type import (
        ReserveRequirementType,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.market_region import (
        MarketRegion,
    )


class ReserveDemandCurve(Curve):
    """Reserve demand curve. Models maximum quantities of reserve required per Market Region
    and models a reserve demand curve for the minimum quantities of reserve. The
    ReserveDemandCurve is a relationship between unit operating reserve price in $/MWhr
    (Y-axis) and unit reserves in MW (X-axis)."""

    __slots__ = ("_as_requirements", "_market_region", "req_max_mw", "reserve_requirement_type")

    req_max_mw: float | None
    reserve_requirement_type: ReserveRequirementType | None

    as_requirements: One[ASRequirements] = One(
        EndMeta(
            name="as_requirements",
            cim_role="ASRequirements",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.as_requirements:ASRequirements",
            many=False,
            lower=1,
            upper=1,
            inverse="reserve_demand_curve",
            aggregation="none",
        )
    )
    market_region: One[MarketRegion] = One(
        EndMeta(
            name="market_region",
            cim_role="MarketRegion",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.market_region:MarketRegion",
            many=False,
            lower=1,
            upper=1,
            inverse="reserve_demand_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ReserveDemandCurve",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{E883299B-F114-4f66-A3F5-71A6BEAE650E}",
        attributes=(
            AttrMeta("req_max_mw", "reqMaxMW", "float", 0, 1, "primitive"),
            AttrMeta(
                "reserve_requirement_type",
                "reserveRequirementType",
                "ReserveRequirementType",
                0,
                1,
                "enumeration",
            ),
        ),
        ends=(
            as_requirements.meta,
            market_region.meta,
        ),
    )

    def __init__(
        self,
        *,
        req_max_mw: float | None = None,
        reserve_requirement_type: ReserveRequirementType | None = None,
        as_requirements: ASRequirements | None = None,
        market_region: MarketRegion | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.req_max_mw = req_max_mw
        self.reserve_requirement_type = reserve_requirement_type
        if as_requirements is not None:
            self.as_requirements = as_requirements
        if market_region is not None:
            self.market_region = market_region

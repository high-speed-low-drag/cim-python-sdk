"""CIM class ControlAreaSolutionData (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_control_area import (
        MktControlArea,
    )


class ControlAreaSolutionData(CimObject):
    """State Estimator Solution Pool Interchange and Losses."""

    __slots__ = ("_mkt_control_area", "solved_interchange", "solved_losses")

    solved_losses: float | None
    solved_interchange: float | None

    mkt_control_area: One[MktControlArea] = One(
        EndMeta(
            name="mkt_control_area",
            cim_role="MktControlArea",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.mkt_control_area:MktControlArea",
            many=False,
            lower=0,
            upper=1,
            inverse="control_area_solution_data",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ControlAreaSolutionData",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{04E44222-CA1D-420b-8D13-09E39F714382}",
        attributes=(
            AttrMeta("solved_losses", "solvedLosses", "float", 0, 1, "primitive"),
            AttrMeta("solved_interchange", "solvedInterchange", "float", 0, 1, "primitive"),
        ),
        ends=(mkt_control_area.meta,),
    )

    def __init__(
        self,
        *,
        solved_losses: float | None = None,
        solved_interchange: float | None = None,
        mkt_control_area: MktControlArea | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.solved_losses = solved_losses
        self.solved_interchange = solved_interchange
        if mkt_control_area is not None:
            self.mkt_control_area = mkt_control_area

"""CIM class MktControlArea (TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.control_area.control_area import ControlArea

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.control_area_solution_data import (
        ControlAreaSolutionData,
    )


class MktControlArea(ControlArea):
    """Market subclass of IEC 61970:ControlArea."""

    __slots__ = ("_control_area_solution_data",)

    control_area_solution_data: Many[ControlAreaSolutionData] = Many(
        EndMeta(
            name="control_area_solution_data",
            cim_role="ControlAreaSolutionData",
            target="cim_python_sdk.model.iec62325.market_operations.market_system.external_inputs.control_area_solution_data:ControlAreaSolutionData",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_control_area",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktControlArea",
        package="TC57CIM/IEC62325/MarketOperations/MarketSystem/ExternalInputs",
        guid="{247F6C1A-E9AF-49c0-B00D-05FB8D49CF78}",
        ends=(control_area_solution_data.meta,),
    )

    def __init__(
        self,
        *,
        control_area_solution_data: Iterable[ControlAreaSolutionData] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if control_area_solution_data is not None:
            MktControlArea.control_area_solution_data.extend(self, control_area_solution_data)

    def add_control_area_solution_data(
        self, control_area_solution_data: ControlAreaSolutionData
    ) -> Self:
        return MktControlArea.control_area_solution_data.add(self, control_area_solution_data)

    def remove_control_area_solution_data(
        self, control_area_solution_data: ControlAreaSolutionData
    ) -> Self:
        return MktControlArea.control_area_solution_data.remove(self, control_area_solution_data)

    def clear_control_area_solution_data(self) -> Self:
        return MktControlArea.control_area_solution_data.clear(self)

    def num_control_area_solution_data(self) -> int:
        return MktControlArea.control_area_solution_data.count(self)

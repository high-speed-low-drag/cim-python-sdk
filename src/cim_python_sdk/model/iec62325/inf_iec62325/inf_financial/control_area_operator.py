"""CIM class ControlAreaOperator (TC57CIM/IEC62325/InfIEC62325/InfFinancial). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.organisation import Organisation

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.tie_line import TieLine
    from cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area import (
        HostControlArea,
    )


class ControlAreaOperator(Organisation):
    """Operates the Control Area. Approves and implements energy transactions. Verifies both
    Inter-Control Area and Intra-Control Area transactions for the power system before
    granting approval (and implementing) the transactions."""

    __slots__ = ("_ca_child_of", "_controlled_by")

    controlled_by: One[HostControlArea] = One(
        EndMeta(
            name="controlled_by",
            cim_role="ControlledBy",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.host_control_area:HostControlArea",
            many=False,
            lower=1,
            upper=1,
            inverse="controls_controlled_by",
            aggregation="none",
        )
    )
    ca_child_of: Many[TieLine] = Many(
        EndMeta(
            name="ca_child_of",
            cim_role="CAChildOf",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.tie_line:TieLine",
            many=True,
            lower=0,
            upper=None,
            inverse="parent_of_a",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ControlAreaOperator",
        package="TC57CIM/IEC62325/InfIEC62325/InfFinancial",
        guid="{448C950F-042A-485b-B70B-EE8A08FA381B}",
        ends=(
            controlled_by.meta,
            ca_child_of.meta,
        ),
    )

    def __init__(
        self,
        *,
        controlled_by: HostControlArea | None = None,
        ca_child_of: Iterable[TieLine] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if controlled_by is not None:
            self.controlled_by = controlled_by
        if ca_child_of is not None:
            ControlAreaOperator.ca_child_of.extend(self, ca_child_of)

    def add_ca_child_of(self, ca_child_of: TieLine) -> Self:
        return ControlAreaOperator.ca_child_of.add(self, ca_child_of)

    def remove_ca_child_of(self, ca_child_of: TieLine) -> Self:
        return ControlAreaOperator.ca_child_of.remove(self, ca_child_of)

    def clear_ca_child_of(self) -> Self:
        return ControlAreaOperator.ca_child_of.clear(self)

    def num_ca_child_of(self) -> int:
        return ControlAreaOperator.ca_child_of.count(self)

    def get_ca_child_of_by_mrid(self, mrid: str) -> TieLine | None:
        return ControlAreaOperator.ca_child_of.get_by_mrid(self, mrid)

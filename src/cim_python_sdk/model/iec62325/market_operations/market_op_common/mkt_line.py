"""CIM class MktLine (TC57CIM/IEC62325/MarketOperations/MarketOpCommon). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.wires.line import Line

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.transmission_right_of_way import (
        TransmissionRightOfWay,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate


class MktLine(Line):
    """Subclass for IEC61970:Wires:Line."""

    __slots__ = ("_flowgate", "_transmission_right_of_way")

    transmission_right_of_way: One[TransmissionRightOfWay] = One(
        EndMeta(
            name="transmission_right_of_way",
            cim_role="TransmissionRightOfWay",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.transmission_right_of_way:TransmissionRightOfWay",
            many=False,
            lower=0,
            upper=1,
            inverse="mkt_line",
            aggregation="none",
        )
    )
    flowgate: Many[Flowgate] = Many(
        EndMeta(
            name="flowgate",
            cim_role="Flowgate",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate:Flowgate",
            many=True,
            lower=0,
            upper=None,
            inverse="mkt_line",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MktLine",
        package="TC57CIM/IEC62325/MarketOperations/MarketOpCommon",
        guid="{AC98E4CC-3B82-4c05-BBAE-13FAFC8CEFFD}",
        ends=(
            transmission_right_of_way.meta,
            flowgate.meta,
        ),
    )

    def __init__(
        self,
        *,
        transmission_right_of_way: TransmissionRightOfWay | None = None,
        flowgate: Iterable[Flowgate] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if transmission_right_of_way is not None:
            self.transmission_right_of_way = transmission_right_of_way
        if flowgate is not None:
            MktLine.flowgate.extend(self, flowgate)

    def add_flowgate(self, flowgate: Flowgate) -> Self:
        return MktLine.flowgate.add(self, flowgate)

    def remove_flowgate(self, flowgate: Flowgate) -> Self:
        return MktLine.flowgate.remove(self, flowgate)

    def clear_flowgate(self) -> Self:
        return MktLine.flowgate.clear(self)

    def num_flowgate(self) -> int:
        return MktLine.flowgate.count(self)

    def get_flowgate_by_mrid(self, mrid: str) -> Flowgate | None:
        return MktLine.flowgate.get_by_mrid(self, mrid)

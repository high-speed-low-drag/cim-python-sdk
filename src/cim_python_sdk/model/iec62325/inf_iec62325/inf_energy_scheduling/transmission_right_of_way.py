"""CIM class TransmissionRightOfWay (TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.transmission_corridor import (
        TransmissionCorridor,
    )
    from cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_line import MktLine


class TransmissionRightOfWay(PowerSystemResource):
    """A collection of transmission lines that are close proximity to each other."""

    __slots__ = ("_mkt_line", "_transmission_corridor")

    mkt_line: Many[MktLine] = Many(
        EndMeta(
            name="mkt_line",
            cim_role="MktLine",
            target="cim_python_sdk.model.iec62325.market_operations.market_op_common.mkt_line:MktLine",
            many=True,
            lower=0,
            upper=None,
            inverse="transmission_right_of_way",
            aggregation="none",
        )
    )
    transmission_corridor: One[TransmissionCorridor] = One(
        EndMeta(
            name="transmission_corridor",
            cim_role="TransmissionCorridor",
            target="cim_python_sdk.model.iec62325.inf_iec62325.inf_energy_scheduling.transmission_corridor:TransmissionCorridor",
            many=False,
            lower=1,
            upper=1,
            inverse="transmission_right_of_ways",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransmissionRightOfWay",
        package="TC57CIM/IEC62325/InfIEC62325/InfEnergyScheduling",
        guid="{3D85EC01-B65A-442a-AECE-5831D6C8BC59}",
        ends=(
            mkt_line.meta,
            transmission_corridor.meta,
        ),
    )

    def __init__(
        self,
        *,
        mkt_line: Iterable[MktLine] | None = None,
        transmission_corridor: TransmissionCorridor | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if mkt_line is not None:
            TransmissionRightOfWay.mkt_line.extend(self, mkt_line)
        if transmission_corridor is not None:
            self.transmission_corridor = transmission_corridor

    def add_mkt_line(self, mkt_line: MktLine) -> Self:
        return TransmissionRightOfWay.mkt_line.add(self, mkt_line)

    def remove_mkt_line(self, mkt_line: MktLine) -> Self:
        return TransmissionRightOfWay.mkt_line.remove(self, mkt_line)

    def clear_mkt_line(self) -> Self:
        return TransmissionRightOfWay.mkt_line.clear(self)

    def num_mkt_line(self) -> int:
        return TransmissionRightOfWay.mkt_line.count(self)

    def get_mkt_line_by_mrid(self, mrid: str) -> MktLine | None:
        return TransmissionRightOfWay.mkt_line.get_by_mrid(self, mrid)

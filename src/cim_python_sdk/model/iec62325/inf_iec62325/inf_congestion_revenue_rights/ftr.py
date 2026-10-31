"""CIM class FTR (TC57CIM/IEC62325/InfIEC62325/InfCongestionRevenueRights). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.agreement import Agreement

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.market_operations.participant_interfaces.energy_price_curve import (
        EnergyPriceCurve,
    )
    from cim_python_sdk.model.iec62325.market_operations.reference_data.flowgate import Flowgate
    from cim_python_sdk.model.iec62325.market_operations.reference_data.pnode import Pnode


class FTR(Agreement):
    """Financial Transmission Rights (FTR) regarding transmission capacity at a flowgate."""

    __slots__ = (
        "_energy_price_curve",
        "_flowgate",
        "_pnodes",
        "action",
        "base_energy",
        "class_",
        "ftr_type",
        "optimized",
    )

    optimized: str | None
    action: str | None
    base_energy: float | None  # ActivePower
    ftr_type: str | None
    class_: str | None

    energy_price_curve: One[EnergyPriceCurve] = One(
        EndMeta(
            name="energy_price_curve",
            cim_role="EnergyPriceCurve",
            target="cim_python_sdk.model.iec62325.market_operations.participant_interfaces.energy_price_curve:EnergyPriceCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="ftrs",
            aggregation="none",
        )
    )
    pnodes: Many[Pnode] = Many(
        EndMeta(
            name="pnodes",
            cim_role="Pnodes",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.pnode:Pnode",
            many=True,
            lower=0,
            upper=None,
            inverse="ftrs",
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
            inverse="ftrs",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="FTR",
        package="TC57CIM/IEC62325/InfIEC62325/InfCongestionRevenueRights",
        guid="{6240D9E7-B494-4a46-926F-3F840BA65ACB}",
        attributes=(
            AttrMeta("optimized", "optimized", "str", 0, 1, "primitive"),
            AttrMeta("action", "action", "str", 0, 1, "primitive"),
            AttrMeta("base_energy", "baseEnergy", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("ftr_type", "ftrType", "str", 0, 1, "primitive"),
            AttrMeta("class_", "class", "str", 0, 1, "primitive"),
        ),
        ends=(
            energy_price_curve.meta,
            pnodes.meta,
            flowgate.meta,
        ),
    )

    def __init__(
        self,
        *,
        optimized: str | None = None,
        action: str | None = None,
        base_energy: float | None = None,
        ftr_type: str | None = None,
        class_: str | None = None,
        energy_price_curve: EnergyPriceCurve | None = None,
        pnodes: Iterable[Pnode] | None = None,
        flowgate: Flowgate | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.optimized = optimized
        self.action = action
        self.base_energy = base_energy
        self.ftr_type = ftr_type
        self.class_ = class_
        if energy_price_curve is not None:
            self.energy_price_curve = energy_price_curve
        if pnodes is not None:
            FTR.pnodes.extend(self, pnodes)
        if flowgate is not None:
            self.flowgate = flowgate

    def add_pnode(self, pnode: Pnode) -> Self:
        return FTR.pnodes.add(self, pnode)

    def remove_pnode(self, pnode: Pnode) -> Self:
        return FTR.pnodes.remove(self, pnode)

    def clear_pnodes(self) -> Self:
        return FTR.pnodes.clear(self)

    def num_pnode(self) -> int:
        return FTR.pnodes.count(self)

    def get_pnode_by_mrid(self, mrid: str) -> Pnode | None:
        return FTR.pnodes.get_by_mrid(self, mrid)

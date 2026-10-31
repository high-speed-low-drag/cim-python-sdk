"""CIM class Bushing (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.assets.asset import Asset

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.interrupter_unit import InterrupterUnit
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.bushing_insulation_pf import (
        BushingInsulationPF,
    )
    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal


class Bushing(Asset):
    """Bushing asset."""

    __slots__ = ("_bushing_insulation_pfs", "_fixed_contact", "_moving_contact", "_terminal")

    moving_contact: One[InterrupterUnit] = One(
        EndMeta(
            name="moving_contact",
            cim_role="MovingContact",
            target="cim_python_sdk.model.iec61968.assets.interrupter_unit:InterrupterUnit",
            many=False,
            lower=0,
            upper=1,
            inverse="bushing",
            aggregation="none",
        )
    )
    terminal: One[Terminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=0,
            upper=1,
            inverse="bushing",
            aggregation="none",
        )
    )
    bushing_insulation_pfs: Many[BushingInsulationPF] = Many(
        EndMeta(
            name="bushing_insulation_pfs",
            cim_role="BushingInsulationPFs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.bushing_insulation_pf:BushingInsulationPF",
            many=True,
            lower=0,
            upper=None,
            inverse="bushing",
            aggregation="none",
        )
    )
    fixed_contact: One[InterrupterUnit] = One(
        EndMeta(
            name="fixed_contact",
            cim_role="FixedContact",
            target="cim_python_sdk.model.iec61968.assets.interrupter_unit:InterrupterUnit",
            many=False,
            lower=0,
            upper=1,
            inverse="bushing_fixed_contact",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Bushing",
        package="TC57CIM/IEC61968/Assets",
        guid="{A29CB50C-9E82-485c-B7B5-78159D2E2C05}",
        ends=(
            moving_contact.meta,
            terminal.meta,
            bushing_insulation_pfs.meta,
            fixed_contact.meta,
        ),
    )

    def __init__(
        self,
        *,
        moving_contact: InterrupterUnit | None = None,
        terminal: Terminal | None = None,
        bushing_insulation_pfs: Iterable[BushingInsulationPF] | None = None,
        fixed_contact: InterrupterUnit | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if moving_contact is not None:
            self.moving_contact = moving_contact
        if terminal is not None:
            self.terminal = terminal
        if bushing_insulation_pfs is not None:
            Bushing.bushing_insulation_pfs.extend(self, bushing_insulation_pfs)
        if fixed_contact is not None:
            self.fixed_contact = fixed_contact

    def add_bushing_insulation_pf(self, bushing_insulation_pf: BushingInsulationPF) -> Self:
        return Bushing.bushing_insulation_pfs.add(self, bushing_insulation_pf)

    def remove_bushing_insulation_pf(self, bushing_insulation_pf: BushingInsulationPF) -> Self:
        return Bushing.bushing_insulation_pfs.remove(self, bushing_insulation_pf)

    def clear_bushing_insulation_pfs(self) -> Self:
        return Bushing.bushing_insulation_pfs.clear(self)

    def num_bushing_insulation_pf(self) -> int:
        return Bushing.bushing_insulation_pfs.count(self)

    def get_bushing_insulation_pf_by_mrid(self, mrid: str) -> BushingInsulationPF | None:
        return Bushing.bushing_insulation_pfs.get_by_mrid(self, mrid)

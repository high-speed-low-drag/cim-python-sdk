"""CIM class Qregulator (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/VSC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay import Delay
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.hvdc_look_up_table import (
        HVDCLookUpTable,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.vs_ctype1 import (
        VSCtype1,
    )


class Qregulator(CimObject):
    """CIM class Qregulator."""

    __slots__ = ("_delay", "_hvd_clook_up_table", "_vs_ctype1")

    vs_ctype1: One[VSCtype1] = One(
        EndMeta(
            name="vs_ctype1",
            cim_role="VSCtype1",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.vsc.vs_ctype1:VSCtype1",
            many=False,
            lower=0,
            upper=1,
            inverse="qregulator",
            aggregation="none",
        )
    )
    hvd_clook_up_table: Many[HVDCLookUpTable] = Many(
        EndMeta(
            name="hvd_clook_up_table",
            cim_role="HVDClookUpTable",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.hvdc_look_up_table:HVDCLookUpTable",
            many=True,
            lower=1,
            upper=None,
            inverse="qregulator",
            aggregation="none",
        )
    )
    delay: One[Delay] = One(
        EndMeta(
            name="delay",
            cim_role="Delay",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay:Delay",
            many=False,
            lower=1,
            upper=1,
            inverse="qregulator",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Qregulator",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/VSC",
        guid="{3D1F7383-2254-4da0-BB6E-38FFA6A5ABCF}",
        ends=(
            vs_ctype1.meta,
            hvd_clook_up_table.meta,
            delay.meta,
        ),
    )

    def __init__(
        self,
        *,
        vs_ctype1: VSCtype1 | None = None,
        hvd_clook_up_table: Iterable[HVDCLookUpTable] | None = None,
        delay: Delay | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if vs_ctype1 is not None:
            self.vs_ctype1 = vs_ctype1
        if hvd_clook_up_table is not None:
            Qregulator.hvd_clook_up_table.extend(self, hvd_clook_up_table)
        if delay is not None:
            self.delay = delay

    def add_hvd_clook_up_table(self, hvd_clook_up_table: HVDCLookUpTable) -> Self:
        return Qregulator.hvd_clook_up_table.add(self, hvd_clook_up_table)

    def remove_hvd_clook_up_table(self, hvd_clook_up_table: HVDCLookUpTable) -> Self:
        return Qregulator.hvd_clook_up_table.remove(self, hvd_clook_up_table)

    def clear_hvd_clook_up_table(self) -> Self:
        return Qregulator.hvd_clook_up_table.clear(self)

    def num_hvd_clook_up_table(self) -> int:
        return Qregulator.hvd_clook_up_table.count(self)

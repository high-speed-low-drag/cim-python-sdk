"""CIM class VDCOL (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, Many, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.idc_inverter_control import (
        IdcInverterControl,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay import Delay
    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.hvdc_look_up_table import (
        HVDCLookUpTable,
    )


class VDCOL(CimObject):
    """CIM class VDCOL."""

    __slots__ = ("_delay", "_hvdc_look_up_tables", "_idc_inverter_control")

    hvdc_look_up_tables: Many[HVDCLookUpTable] = Many(
        EndMeta(
            name="hvdc_look_up_tables",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.hvdc_look_up_table:HVDCLookUpTable",
            many=True,
            lower=1,
            upper=None,
            inverse="vdcol",
            aggregation="none",
        )
    )
    idc_inverter_control: One[IdcInverterControl] = One(
        EndMeta(
            name="idc_inverter_control",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.idc_inverter_control:IdcInverterControl",
            many=False,
            lower=0,
            upper=1,
            inverse="vdcol",
            aggregation="none",
        )
    )
    delay: One[Delay] = One(
        EndMeta(
            name="delay",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.delay:Delay",
            many=False,
            lower=1,
            upper=1,
            inverse="vdcol",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VDCOL",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC",
        guid="{01B1712A-A728-40b7-8289-40834537C20A}",
        ends=(
            hvdc_look_up_tables.meta,
            idc_inverter_control.meta,
            delay.meta,
        ),
    )

    def __init__(
        self,
        *,
        hvdc_look_up_tables: Iterable[HVDCLookUpTable] | None = None,
        idc_inverter_control: IdcInverterControl | None = None,
        delay: Delay | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if hvdc_look_up_tables is not None:
            VDCOL.hvdc_look_up_tables.extend(self, hvdc_look_up_tables)
        if idc_inverter_control is not None:
            self.idc_inverter_control = idc_inverter_control
        if delay is not None:
            self.delay = delay

    def add_hvdc_look_up_table(self, hvdc_look_up_table: HVDCLookUpTable) -> Self:
        return VDCOL.hvdc_look_up_tables.add(self, hvdc_look_up_table)

    def remove_hvdc_look_up_table(self, hvdc_look_up_table: HVDCLookUpTable) -> Self:
        return VDCOL.hvdc_look_up_tables.remove(self, hvdc_look_up_table)

    def clear_hvdc_look_up_tables(self) -> Self:
        return VDCOL.hvdc_look_up_tables.clear(self)

    def num_hvdc_look_up_table(self) -> int:
        return VDCOL.hvdc_look_up_tables.count(self)

"""CIM class VSCDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/HVDCDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.hvdc_dynamics.hvdc_dynamics import (
    HVDCDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.dc.vs_converter import VsConverter


class VSCDynamics(HVDCDynamics):
    """VSC function block whose behaviour is described by reference to a standard model or by
    definition of a user-defined model."""

    __slots__ = ("_vs_converter",)

    vs_converter: One[VsConverter] = One(
        EndMeta(
            name="vs_converter",
            cim_role="VsConverter",
            target="cim_python_sdk.model.iec61970.base.dc.vs_converter:VsConverter",
            many=False,
            lower=1,
            upper=1,
            inverse="vsc_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VSCDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/HVDCDynamics",
        guid="{7A75C445-CEA2-4928-8329-51B05093D7B3}",
        ends=(vs_converter.meta,),
    )

    def __init__(
        self,
        *,
        vs_converter: VsConverter | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if vs_converter is not None:
            self.vs_converter = vs_converter

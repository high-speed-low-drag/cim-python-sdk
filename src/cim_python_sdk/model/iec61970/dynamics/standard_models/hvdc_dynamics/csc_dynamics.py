"""CIM class CSCDynamics (TC57CIM/IEC61970/Dynamics/StandardModels/HVDCDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.dynamics.standard_models.hvdc_dynamics.hvdc_dynamics import (
    HVDCDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.dc.cs_converter import CsConverter


class CSCDynamics(HVDCDynamics):
    """CSC function block whose behaviour is described by reference to a standard model or by
    definition of a user-defined model."""

    __slots__ = ("_cs_converter",)

    cs_converter: One[CsConverter] = One(
        EndMeta(
            name="cs_converter",
            cim_role="CSConverter",
            target="cim_python_sdk.model.iec61970.base.dc.cs_converter:CsConverter",
            many=False,
            lower=1,
            upper=1,
            inverse="csc_dynamics",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CSCDynamics",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/HVDCDynamics",
        guid="{A2A5768C-1A20-4d59-8531-83E3741AE6FD}",
        ends=(cs_converter.meta,),
    )

    def __init__(
        self,
        *,
        cs_converter: CsConverter | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if cs_converter is not None:
            self.cs_converter = cs_converter

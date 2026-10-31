"""CIM class IgnAngleContInverter (TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cs_ctype1 import (
        CSCtype1,
    )


class IgnAngleContInverter(CimObject):
    """CIM class IgnAngleContInverter."""

    __slots__ = ("_cs_ctype1",)

    cs_ctype1: One[CSCtype1] = One(
        EndMeta(
            name="cs_ctype1",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.inf_hvdc_dynamics.csc.cs_ctype1:CSCtype1",
            many=False,
            lower=0,
            upper=1,
            inverse="ign_angle_cont_inverter",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="IgnAngleContInverter",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/InfHVDCDynamics/CSC",
        guid="{AD744D8D-7206-4601-B9D5-C353A05517CB}",
        ends=(cs_ctype1.meta,),
    )

    def __init__(
        self,
        *,
        cs_ctype1: CSCtype1 | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if cs_ctype1 is not None:
            self.cs_ctype1 = cs_ctype1

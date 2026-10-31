"""CIM class StartRampCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.startup_model import StartupModel


class StartRampCurve(Curve):
    """Rate in gross active power per minute (Y-axis) at which a unit can be loaded versus the
    number of hours (X-axis) the unit was off line."""

    __slots__ = ("_startup_model", "hot_standby_ramp")

    hot_standby_ramp: float | None  # ActivePowerChangeRate

    startup_model: One[StartupModel] = One(
        EndMeta(
            name="startup_model",
            cim_role="StartupModel",
            target="cim_python_sdk.model.iec61970.base.generation.production.startup_model:StartupModel",
            many=False,
            lower=1,
            upper=1,
            inverse="start_ramp_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StartRampCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{EA64A047-C475-45e4-A0AA-A2D208152FA8}",
        attributes=(
            AttrMeta(
                "hot_standby_ramp", "hotStandbyRamp", "ActivePowerChangeRate", 0, 1, "cimdatatype"
            ),
        ),
        ends=(startup_model.meta,),
    )

    def __init__(
        self,
        *,
        hot_standby_ramp: float | None = None,
        startup_model: StartupModel | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.hot_standby_ramp = hot_standby_ramp
        if startup_model is not None:
            self.startup_model = startup_model

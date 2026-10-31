"""CIM class StartMainFuelCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.fuel_type import FuelType
    from cim_python_sdk.model.iec61970.base.generation.production.startup_model import StartupModel


class StartMainFuelCurve(Curve):
    """The quantity of main fuel (Y-axis) used to restart and repay the auxiliary power
    consumed versus the number of hours (X-axis) the unit was off line."""

    __slots__ = ("_startup_model", "main_fuel_type")

    main_fuel_type: FuelType | None

    startup_model: One[StartupModel] = One(
        EndMeta(
            name="startup_model",
            cim_role="StartupModel",
            target="cim_python_sdk.model.iec61970.base.generation.production.startup_model:StartupModel",
            many=False,
            lower=1,
            upper=1,
            inverse="start_main_fuel_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StartMainFuelCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{7E3057A5-5274-4743-BE6B-832426F6EC3F}",
        attributes=(AttrMeta("main_fuel_type", "mainFuelType", "FuelType", 0, 1, "enumeration"),),
        ends=(startup_model.meta,),
    )

    def __init__(
        self,
        *,
        main_fuel_type: FuelType | None = None,
        startup_model: StartupModel | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.main_fuel_type = main_fuel_type
        if startup_model is not None:
            self.startup_model = startup_model

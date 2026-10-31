"""CIM class StartIgnFuelCurve (TC57CIM/IEC61970/Base/Generation/Production). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.curve import Curve

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.generation.production.fuel_type import FuelType
    from cim_python_sdk.model.iec61970.base.generation.production.startup_model import StartupModel


class StartIgnFuelCurve(Curve):
    """The quantity of ignition fuel (Y-axis) used to restart and repay the auxiliary power
    consumed versus the number of hours (X-axis) the unit was off line."""

    __slots__ = ("_startup_model", "ignition_fuel_type")

    ignition_fuel_type: FuelType | None

    startup_model: One[StartupModel] = One(
        EndMeta(
            name="startup_model",
            cim_role="StartupModel",
            target="cim_python_sdk.model.iec61970.base.generation.production.startup_model:StartupModel",
            many=False,
            lower=1,
            upper=1,
            inverse="start_ign_fuel_curve",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="StartIgnFuelCurve",
        package="TC57CIM/IEC61970/Base/Generation/Production",
        guid="{D6091F0C-3817-4ed9-83F2-42DFCAA3BDBD}",
        attributes=(
            AttrMeta("ignition_fuel_type", "ignitionFuelType", "FuelType", 0, 1, "enumeration"),
        ),
        ends=(startup_model.meta,),
    )

    def __init__(
        self,
        *,
        ignition_fuel_type: FuelType | None = None,
        startup_model: StartupModel | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.ignition_fuel_type = ignition_fuel_type
        if startup_model is not None:
            self.startup_model = startup_model

"""CIM class RegulatingCondEq (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.wires.energy_connection import EnergyConnection

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.regulating_control import RegulatingControl


class RegulatingCondEq(EnergyConnection):
    """A type of conducting equipment that can regulate a quantity (i.e. voltage or flow) at a
    specific point in the network."""

    __slots__ = ("_regulating_control", "control_enabled")

    control_enabled: bool | None

    regulating_control: One[RegulatingControl] = One(
        EndMeta(
            name="regulating_control",
            cim_role="RegulatingControl",
            target="cim_python_sdk.model.iec61970.base.wires.regulating_control:RegulatingControl",
            many=False,
            lower=0,
            upper=1,
            inverse="regulating_cond_eq",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="RegulatingCondEq",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{598D5E45-FF89-4074-B3C1-3F40425EE8D6}",
        attributes=(AttrMeta("control_enabled", "controlEnabled", "bool", 0, 1, "primitive"),),
        ends=(regulating_control.meta,),
    )

    def __init__(
        self,
        *,
        control_enabled: bool | None = None,
        regulating_control: RegulatingControl | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.control_enabled = control_enabled
        if regulating_control is not None:
            self.regulating_control = regulating_control

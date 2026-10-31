"""CIM class SvTapStep (TC57CIM/IEC61970/Base/StateVariables). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.state_variables.state_variable import StateVariable

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.tap_changer import TapChanger


class SvTapStep(StateVariable):
    """State variable for transformer tap step."""

    __slots__ = ("_tap_changer", "position")

    position: float | None

    tap_changer: One[TapChanger] = One(
        EndMeta(
            name="tap_changer",
            cim_role="TapChanger",
            target="cim_python_sdk.model.iec61970.base.wires.tap_changer:TapChanger",
            many=False,
            lower=1,
            upper=1,
            inverse="sv_tap_step",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="SvTapStep",
        package="TC57CIM/IEC61970/Base/StateVariables",
        guid="{EDA41BC3-4A8F-46d0-851F-EFCAB8942211}",
        attributes=(AttrMeta("position", "position", "float", 0, 1, "primitive"),),
        ends=(tap_changer.meta,),
    )

    def __init__(
        self,
        *,
        position: float | None = None,
        tap_changer: TapChanger | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.position = position
        if tap_changer is not None:
            self.tap_changer = tap_changer

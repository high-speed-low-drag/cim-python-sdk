"""CIM class ProtectiveActionRegulation (TC57CIM/IEC61970/InfIEC61970/InfSIPS). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.inf_iec61970.inf_sips.protective_action import ProtectiveAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.wires.regulating_control import RegulatingControl


class ProtectiveActionRegulation(ProtectiveAction):
    """Protective action to change regulation to Equipment."""

    __slots__ = ("_regulating_control", "is_regulating", "target_value")

    is_regulating: bool | None
    target_value: float | None

    regulating_control: One[RegulatingControl] = One(
        EndMeta(
            name="regulating_control",
            cim_role="RegulatingControl",
            target="cim_python_sdk.model.iec61970.base.wires.regulating_control:RegulatingControl",
            many=False,
            lower=1,
            upper=1,
            inverse="protective_action_regulation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProtectiveActionRegulation",
        package="TC57CIM/IEC61970/InfIEC61970/InfSIPS",
        guid="{B30177E0-4A8A-4ab2-AA46-7101297B969D}",
        attributes=(
            AttrMeta("is_regulating", "isRegulating", "bool", 0, 1, "primitive"),
            AttrMeta("target_value", "targetValue", "float", 0, 1, "primitive"),
        ),
        ends=(regulating_control.meta,),
    )

    def __init__(
        self,
        *,
        is_regulating: bool | None = None,
        target_value: float | None = None,
        regulating_control: RegulatingControl | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.is_regulating = is_regulating
        self.target_value = target_value
        if regulating_control is not None:
            self.regulating_control = regulating_control

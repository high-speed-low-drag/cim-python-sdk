"""CIM class LoadGenericNonLinear (TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.load_dynamics import (
    LoadDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.load_dynamics.generic_non_linear_load_model_kind import (
        GenericNonLinearLoadModelKind,
    )


class LoadGenericNonLinear(LoadDynamics):
    """Generic non-linear dynamic (GNLD) load. This model can be used in mid-term and long-term
    voltage stability simulations (i.e., to study voltage collapse), as it can replace a
    more detailed representation of aggregate load, including induction motors,
    thermostatically controlled and static loads."""

    __slots__ = ("bs", "bt", "generic_non_linear_load_model_type", "ls", "lt", "tp", "tq")

    generic_non_linear_load_model_type: GenericNonLinearLoadModelKind | None
    tp: float | None  # Seconds
    tq: float | None  # Seconds
    ls: float | None
    lt: float | None
    bs: float | None
    bt: float | None

    _cim_meta = ClassMeta(
        cim_name="LoadGenericNonLinear",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/LoadDynamics",
        guid="{66917254-AB0B-4699-936A-BDFABC710CD5}",
        attributes=(
            AttrMeta(
                "generic_non_linear_load_model_type",
                "genericNonLinearLoadModelType",
                "GenericNonLinearLoadModelKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("tp", "tp", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tq", "tq", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("ls", "ls", "float", 0, 1, "primitive"),
            AttrMeta("lt", "lt", "float", 0, 1, "primitive"),
            AttrMeta("bs", "bs", "float", 0, 1, "primitive"),
            AttrMeta("bt", "bt", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        generic_non_linear_load_model_type: GenericNonLinearLoadModelKind | None = None,
        tp: float | None = None,
        tq: float | None = None,
        ls: float | None = None,
        lt: float | None = None,
        bs: float | None = None,
        bt: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.generic_non_linear_load_model_type = generic_non_linear_load_model_type
        self.tp = tp
        self.tq = tq
        self.ls = ls
        self.lt = lt
        self.bs = bs
        self.bt = bt

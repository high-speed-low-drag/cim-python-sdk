"""CIM class MechLoad1 (TC57CIM/IEC61970/Dynamics/StandardModels/MechanicalLoadDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.mechanical_load_dynamics.mechanical_load_dynamics import (
    MechanicalLoadDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class MechLoad1(MechanicalLoadDynamics):
    """Mechanical load model type 1."""

    __slots__ = ("a", "b", "d", "e")

    a: float | None
    b: float | None
    d: float | None
    e: float | None

    _cim_meta = ClassMeta(
        cim_name="MechLoad1",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/MechanicalLoadDynamics",
        guid="{114B65DF-8F90-46c6-952D-2FC3E46F9169}",
        attributes=(
            AttrMeta("a", "a", "float", 0, 1, "primitive"),
            AttrMeta("b", "b", "float", 0, 1, "primitive"),
            AttrMeta("d", "d", "float", 0, 1, "primitive"),
            AttrMeta("e", "e", "float", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        a: float | None = None,
        b: float | None = None,
        d: float | None = None,
        e: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.a = a
        self.b = b
        self.d = d
        self.e = e

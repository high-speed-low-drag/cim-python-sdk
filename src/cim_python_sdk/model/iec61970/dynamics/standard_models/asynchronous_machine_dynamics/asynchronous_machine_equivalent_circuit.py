"""CIM class AsynchronousMachineEquivalentCircuit (TC57CIM/IEC61970/Dynamics/StandardModels/AsynchronousMachineDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.asynchronous_machine_dynamics.asynchronous_machine_dynamics import (
    AsynchronousMachineDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class AsynchronousMachineEquivalentCircuit(AsynchronousMachineDynamics):
    """The electrical equations of all variations of the asynchronous model are based on the
    AsynchronousEquivalentCircuit diagram for the direct- and quadrature- axes, with two
    equivalent rotor windings in each axis.

    Equations for conversion between equivalent circuit and time constant reactance forms:

    Xs = Xm + Xl

    X' = Xl + Xm x Xlr1 / (Xm + Xlr1)

    X'' = Xl + Xm x Xlr1 x Xlr2 / (Xm x Xlr1 + Xm x Xlr2 + Xlr1 x Xlr2)

    T'o = (Xm + Xlr1) / (omega0 x Rr1)

    T''o = (Xm x Xlr1 + Xm x Xlr2 + Xlr1 x Xlr2) / (omega0 x Rr2 x (Xm + Xlr1)

    Same equations using CIM attributes from AsynchronousMachineTimeConstantReactance class
    on left of "=" and AsynchronousMachineEquivalentCircuit class on right (except as
    noted):

    xs = xm + RotatingMachineDynamics.statorLeakageReactance

    xp = RotatingMachineDynamics.statorLeakageReactance + xm x xlr1 / (xm + xlr1)

    xpp = RotatingMachineDynamics.statorLeakageReactance + xm x xlr1 x xlr2 / (xm x xlr1 +
    xm x xlr2 + xlr1 x xlr2)

    tpo = (xm + xlr1) / (2 x pi x nominal frequency x rr1)

    tppo = (xm x xlr1 + xm x xlr2 + xlr1 x xlr2) / (2 x pi x nominal frequency x rr2 x (xm +
    xlr1)."""

    __slots__ = ("rr1", "rr2", "xlr1", "xlr2", "xm")

    xm: float | None  # PU
    rr1: float | None  # PU
    xlr1: float | None  # PU
    rr2: float | None  # PU
    xlr2: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="AsynchronousMachineEquivalentCircuit",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/AsynchronousMachineDynamics",
        guid="{68994963-39CA-4837-BEE1-D4F0807E421F}",
        attributes=(
            AttrMeta("xm", "xm", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rr1", "rr1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xlr1", "xlr1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rr2", "rr2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xlr2", "xlr2", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        xm: float | None = None,
        rr1: float | None = None,
        xlr1: float | None = None,
        rr2: float | None = None,
        xlr2: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.xm = xm
        self.rr1 = rr1
        self.xlr1 = xlr1
        self.rr2 = rr2
        self.xlr2 = xlr2

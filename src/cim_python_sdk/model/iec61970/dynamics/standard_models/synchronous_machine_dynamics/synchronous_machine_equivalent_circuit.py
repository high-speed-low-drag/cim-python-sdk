"""CIM class SynchronousMachineEquivalentCircuit (TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_detailed import (
    SynchronousMachineDetailed,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class SynchronousMachineEquivalentCircuit(SynchronousMachineDetailed):
    """The electrical equations for all variations of the synchronous models are based on the
    SynchronousEquivalentCircuit diagram for the direct- and quadrature- axes.

    Equations for conversion between equivalent circuit and time constant reactance forms:

    Xd = Xad + Xl

    X’d = Xl + Xad x Xfd / (Xad + Xfd)

    X”d = Xl + Xad x Xfd x X1d / (Xad x Xfd + Xad x X1d + Xfd x X1d)

    Xq = Xaq + Xl

    X’q = Xl + Xaq x X1q / (Xaq + X1q)

    X”q = Xl + Xaq x X1q x X2q / (Xaq x X1q + Xaq x X2q + X1q x X2q)

    T’do = (Xad + Xfd) / (omega0 x Rfd)

    T”do = (Xad x Xfd + Xad x X1d + Xfd x X1d) / (omega0 x R1d x (Xad + Xfd)

    T’qo = (Xaq + X1q) / (omega0 x R1q)

    T”qo = (Xaq x X1q + Xaq x X2q + X1q x X2q) / (omega0 x R2q x (Xaq + X1q)

    Same equations using CIM attributes from SynchronousMachineTimeConstantReactance class
    on left of "=" and SynchronousMachineEquivalentCircuit class on right (except as noted):

    xDirectSync = xad + RotatingMachineDynamics.statorLeakageReactance

    xDirectTrans = RotatingMachineDynamics.statorLeakageReactance + xad x xfd / (xad + xfd)

    xDirectSubtrans = RotatingMachineDynamics.statorLeakageReactance + xad x xfd x x1d /
    (xad x xfd + xad x x1d + xfd x x1d)

    xQuadSync = xaq + RotatingMachineDynamics.statorLeakageReactance

    xQuadTrans = RotatingMachineDynamics.statorLeakageReactance + xaq x x1q / (xaq+ x1q)

    xQuadSubtrans = RotatingMachineDynamics.statorLeakageReactance + xaq x x1q x x2q / (xaq
    x x1q + xaq x x2q + x1q x x2q)

    tpdo = (xad + xfd) / (2 x pi x nominal frequency x rfd)

    tppdo = (xad x xfd + xad x x1d + xfd x x1d) / (2 x pi x nominal frequency x r1d x (xad +
    xfd)

    tpqo = (xaq + x1q) / (2 x pi x nominal frequency x r1q)

    tppqo = (xaq x x1q + xaq x x2q + x1q x x2q) / (2 x pi x nominal frequency x r2q x (xaq +
    x1q)

    These are only valid for a simplified model where "Canay" reactance is zero."""

    __slots__ = ("r1d", "r1q", "r2q", "rfd", "x1d", "x1q", "x2q", "xad", "xaq", "xf1d", "xfd")

    xad: float | None  # PU
    rfd: float | None  # PU
    xfd: float | None  # PU
    r1d: float | None  # PU
    x1d: float | None  # PU
    xf1d: float | None  # PU
    xaq: float | None  # PU
    r1q: float | None  # PU
    x1q: float | None  # PU
    r2q: float | None  # PU
    x2q: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="SynchronousMachineEquivalentCircuit",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics",
        guid="{A0EB0748-18CF-4602-AD73-7FB0E75DC126}",
        attributes=(
            AttrMeta("xad", "xad", "PU", 0, 1, "cimdatatype"),
            AttrMeta("rfd", "rfd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xfd", "xfd", "PU", 0, 1, "cimdatatype"),
            AttrMeta("r1d", "r1d", "PU", 0, 1, "cimdatatype"),
            AttrMeta("x1d", "x1d", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xf1d", "xf1d", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xaq", "xaq", "PU", 0, 1, "cimdatatype"),
            AttrMeta("r1q", "r1q", "PU", 0, 1, "cimdatatype"),
            AttrMeta("x1q", "x1q", "PU", 0, 1, "cimdatatype"),
            AttrMeta("r2q", "r2q", "PU", 0, 1, "cimdatatype"),
            AttrMeta("x2q", "x2q", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        xad: float | None = None,
        rfd: float | None = None,
        xfd: float | None = None,
        r1d: float | None = None,
        x1d: float | None = None,
        xf1d: float | None = None,
        xaq: float | None = None,
        r1q: float | None = None,
        x1q: float | None = None,
        r2q: float | None = None,
        x2q: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.xad = xad
        self.rfd = rfd
        self.xfd = xfd
        self.r1d = r1d
        self.x1d = x1d
        self.xf1d = xf1d
        self.xaq = xaq
        self.r1q = r1q
        self.x1q = x1q
        self.r2q = r2q
        self.x2q = x2q

"""CIM class AsynchronousMachineTimeConstantReactance (TC57CIM/IEC61970/Dynamics/StandardModels/AsynchronousMachineDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.asynchronous_machine_dynamics.asynchronous_machine_dynamics import (
    AsynchronousMachineDynamics,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class AsynchronousMachineTimeConstantReactance(AsynchronousMachineDynamics):
    """Parameter details:

    - If X'' = X', a single cage (one equivalent rotor winding per axis) is modelled.

    - The “p” in the attribute names is a substitution for a “prime” in the usual parameter
    notation, e.g. tpo refers to T'o.

    The parameters used for models expressed in time constant reactance form include:

    - RotatingMachine.ratedS (MVAbase);

    - RotatingMachineDynamics.damping (D);

    - RotatingMachineDynamics.inertia (H);

    - RotatingMachineDynamics.saturationFactor (S1);

    - RotatingMachineDynamics.saturationFactor120 (S12);

    - RotatingMachineDynamics.statorLeakageReactance (Xl);

    - RotatingMachineDynamics.statorResistance (Rs);

    - .xs (Xs);

    - .xp (X');

    - .xpp (X'');

    - .tpo (T'o);

    - .tppo (T''o)."""

    __slots__ = ("tpo", "tppo", "xp", "xpp", "xs")

    xs: float | None  # PU
    xp: float | None  # PU
    xpp: float | None  # PU
    tpo: float | None  # Seconds
    tppo: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="AsynchronousMachineTimeConstantReactance",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/AsynchronousMachineDynamics",
        guid="{20220E3A-DD4F-41fc-B00D-188C7FDCE8D9}",
        attributes=(
            AttrMeta("xs", "xs", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xp", "xp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("xpp", "xpp", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tpo", "tpo", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tppo", "tppo", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        xs: float | None = None,
        xp: float | None = None,
        xpp: float | None = None,
        tpo: float | None = None,
        tppo: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.xs = xs
        self.xp = xp
        self.xpp = xpp
        self.tpo = tpo
        self.tppo = tppo

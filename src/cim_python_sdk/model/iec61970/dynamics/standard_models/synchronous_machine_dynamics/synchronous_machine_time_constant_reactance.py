"""CIM class SynchronousMachineTimeConstantReactance (TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_detailed import (
    SynchronousMachineDetailed,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.rotor_kind import (
        RotorKind,
    )
    from cim_python_sdk.model.iec61970.dynamics.standard_models.synchronous_machine_dynamics.synchronous_machine_model_kind import (
        SynchronousMachineModelKind,
    )


class SynchronousMachineTimeConstantReactance(SynchronousMachineDetailed):
    """Synchronous machine detailed modelling types are defined by the combination of the
    attributes SynchronousMachineTimeConstantReactance.modelType and
    SynchronousMachineTimeConstantReactance.rotorType.

    Parameter details:

    - The “p” in the time-related attribute names is a substitution for a “prime” in the
    usual parameter notation, e.g. tpdo refers to T'do.

    - The parameters used for models expressed in time constant reactance form include:

    - RotatingMachine.ratedS (MVAbase);

    - RotatingMachineDynamics.damping (D);

    - RotatingMachineDynamics.inertia (H);

    - RotatingMachineDynamics.saturationFactor (S1);

    - RotatingMachineDynamics.saturationFactor120 (S12);

    - RotatingMachineDynamics.statorLeakageReactance (Xl);

    - RotatingMachineDynamics.statorResistance (Rs);

    - SynchronousMachineTimeConstantReactance.ks (Ks);

    - SynchronousMachineDetailed.saturationFactorQAxis (S1q);

    - SynchronousMachineDetailed.saturationFactor120QAxis (S12q);

    - SynchronousMachineDetailed.efdBaseRatio;

    - SynchronousMachineDetailed.ifdBaseType;

    - .xDirectSync (Xd);

    - .xDirectTrans (X'd);

    - .xDirectSubtrans (X''d);

    - .xQuadSync (Xq);

    - .xQuadTrans (X'q);

    - .xQuadSubtrans (X''q);

    - .tpdo (T'do);

    - .tppdo (T''do);

    - .tpqo (T'qo);

    - .tppqo (T''qo);

    - .tc."""

    __slots__ = (
        "ks",
        "model_type",
        "rotor_type",
        "tc",
        "tpdo",
        "tppdo",
        "tppqo",
        "tpqo",
        "x_direct_subtrans",
        "x_direct_sync",
        "x_direct_trans",
        "x_quad_subtrans",
        "x_quad_sync",
        "x_quad_trans",
    )

    rotor_type: RotorKind | None
    model_type: SynchronousMachineModelKind | None
    ks: float | None
    x_direct_sync: float | None  # PU
    x_direct_trans: float | None  # PU
    x_direct_subtrans: float | None  # PU
    x_quad_sync: float | None  # PU
    x_quad_trans: float | None  # PU
    x_quad_subtrans: float | None  # PU
    tpdo: float | None  # Seconds
    tppdo: float | None  # Seconds
    tpqo: float | None  # Seconds
    tppqo: float | None  # Seconds
    tc: float | None  # Seconds

    _cim_meta = ClassMeta(
        cim_name="SynchronousMachineTimeConstantReactance",
        package="TC57CIM/IEC61970/Dynamics/StandardModels/SynchronousMachineDynamics",
        guid="{C6F04365-226C-4457-AE52-86A30D76F764}",
        attributes=(
            AttrMeta("rotor_type", "rotorType", "RotorKind", 0, 1, "enumeration"),
            AttrMeta("model_type", "modelType", "SynchronousMachineModelKind", 0, 1, "enumeration"),
            AttrMeta("ks", "ks", "float", 0, 1, "primitive"),
            AttrMeta("x_direct_sync", "xDirectSync", "PU", 0, 1, "cimdatatype"),
            AttrMeta("x_direct_trans", "xDirectTrans", "PU", 0, 1, "cimdatatype"),
            AttrMeta("x_direct_subtrans", "xDirectSubtrans", "PU", 0, 1, "cimdatatype"),
            AttrMeta("x_quad_sync", "xQuadSync", "PU", 0, 1, "cimdatatype"),
            AttrMeta("x_quad_trans", "xQuadTrans", "PU", 0, 1, "cimdatatype"),
            AttrMeta("x_quad_subtrans", "xQuadSubtrans", "PU", 0, 1, "cimdatatype"),
            AttrMeta("tpdo", "tpdo", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tppdo", "tppdo", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tpqo", "tpqo", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tppqo", "tppqo", "Seconds", 0, 1, "cimdatatype"),
            AttrMeta("tc", "tc", "Seconds", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        rotor_type: RotorKind | None = None,
        model_type: SynchronousMachineModelKind | None = None,
        ks: float | None = None,
        x_direct_sync: float | None = None,
        x_direct_trans: float | None = None,
        x_direct_subtrans: float | None = None,
        x_quad_sync: float | None = None,
        x_quad_trans: float | None = None,
        x_quad_subtrans: float | None = None,
        tpdo: float | None = None,
        tppdo: float | None = None,
        tpqo: float | None = None,
        tppqo: float | None = None,
        tc: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.rotor_type = rotor_type
        self.model_type = model_type
        self.ks = ks
        self.x_direct_sync = x_direct_sync
        self.x_direct_trans = x_direct_trans
        self.x_direct_subtrans = x_direct_subtrans
        self.x_quad_sync = x_quad_sync
        self.x_quad_trans = x_quad_trans
        self.x_quad_subtrans = x_quad_subtrans
        self.tpdo = tpdo
        self.tppdo = tppdo
        self.tpqo = tpqo
        self.tppqo = tppqo
        self.tc = tc

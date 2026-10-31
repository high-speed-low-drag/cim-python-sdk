"""CIM class VsConverter (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.dc.acdc_converter import ACDCConverter

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.base.dc.vs_capability_curve import VsCapabilityCurve
    from cim_python_sdk.model.iec61970.base.dc.vs_ppcc_control_kind import VsPpccControlKind
    from cim_python_sdk.model.iec61970.base.dc.vs_qpcc_control_kind import VsQpccControlKind
    from cim_python_sdk.model.iec61970.dynamics.standard_models.hvdc_dynamics.vsc_dynamics import (
        VSCDynamics,
    )


class VsConverter(ACDCConverter):
    """DC side of the voltage source converter (VSC)."""

    __slots__ = (
        "_capability_curve",
        "_vsc_dynamics",
        "delta",
        "droop",
        "droop_compensation",
        "max_modulation_index",
        "max_valve_current",
        "p_pcc_control",
        "q_pcc_control",
        "q_share",
        "target_phase_pcc",
        "target_power_factor_pcc",
        "target_pw_mfactor",
        "target_qpcc",
        "target_upcc",
        "uv",
    )

    delta: float | None  # AngleDegrees
    droop: float | None  # PU
    droop_compensation: float | None  # Resistance
    max_modulation_index: float | None
    max_valve_current: float | None  # CurrentFlow
    p_pcc_control: VsPpccControlKind | None
    q_pcc_control: VsQpccControlKind | None
    q_share: float | None  # PerCent
    target_qpcc: float | None  # ReactivePower
    target_upcc: float | None  # Voltage
    uv: float | None  # Voltage
    target_power_factor_pcc: float | None
    target_phase_pcc: float | None  # AngleDegrees
    target_pw_mfactor: float | None

    capability_curve: One[VsCapabilityCurve] = One(
        EndMeta(
            name="capability_curve",
            cim_role="CapabilityCurve",
            target="cim_python_sdk.model.iec61970.base.dc.vs_capability_curve:VsCapabilityCurve",
            many=False,
            lower=0,
            upper=1,
            inverse="vs_converter_dc_sides",
            aggregation="none",
        )
    )
    vsc_dynamics: One[VSCDynamics] = One(
        EndMeta(
            name="vsc_dynamics",
            cim_role="VSCDynamics",
            target="cim_python_sdk.model.iec61970.dynamics.standard_models.hvdc_dynamics.vsc_dynamics:VSCDynamics",
            many=False,
            lower=0,
            upper=1,
            inverse="vs_converter",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="VsConverter",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{D3B18BC2-AB54-475c-A731-6EBA3D738BF7}",
        attributes=(
            AttrMeta("delta", "delta", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("droop", "droop", "PU", 0, 1, "cimdatatype"),
            AttrMeta("droop_compensation", "droopCompensation", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("max_modulation_index", "maxModulationIndex", "float", 0, 1, "primitive"),
            AttrMeta("max_valve_current", "maxValveCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("p_pcc_control", "pPccControl", "VsPpccControlKind", 0, 1, "enumeration"),
            AttrMeta("q_pcc_control", "qPccControl", "VsQpccControlKind", 0, 1, "enumeration"),
            AttrMeta("q_share", "qShare", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("target_qpcc", "targetQpcc", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("target_upcc", "targetUpcc", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("uv", "uv", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("target_power_factor_pcc", "targetPowerFactorPcc", "float", 0, 1, "primitive"),
            AttrMeta("target_phase_pcc", "targetPhasePcc", "AngleDegrees", 0, 1, "cimdatatype"),
            AttrMeta("target_pw_mfactor", "targetPWMfactor", "float", 0, 1, "primitive"),
        ),
        ends=(
            capability_curve.meta,
            vsc_dynamics.meta,
        ),
    )

    def __init__(
        self,
        *,
        delta: float | None = None,
        droop: float | None = None,
        droop_compensation: float | None = None,
        max_modulation_index: float | None = None,
        max_valve_current: float | None = None,
        p_pcc_control: VsPpccControlKind | None = None,
        q_pcc_control: VsQpccControlKind | None = None,
        q_share: float | None = None,
        target_qpcc: float | None = None,
        target_upcc: float | None = None,
        uv: float | None = None,
        target_power_factor_pcc: float | None = None,
        target_phase_pcc: float | None = None,
        target_pw_mfactor: float | None = None,
        capability_curve: VsCapabilityCurve | None = None,
        vsc_dynamics: VSCDynamics | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.delta = delta
        self.droop = droop
        self.droop_compensation = droop_compensation
        self.max_modulation_index = max_modulation_index
        self.max_valve_current = max_valve_current
        self.p_pcc_control = p_pcc_control
        self.q_pcc_control = q_pcc_control
        self.q_share = q_share
        self.target_qpcc = target_qpcc
        self.target_upcc = target_upcc
        self.uv = uv
        self.target_power_factor_pcc = target_power_factor_pcc
        self.target_phase_pcc = target_phase_pcc
        self.target_pw_mfactor = target_pw_mfactor
        if capability_curve is not None:
            self.capability_curve = capability_curve
        if vsc_dynamics is not None:
            self.vsc_dynamics = vsc_dynamics

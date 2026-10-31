"""CIM class PWRSteamSupply (TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.generation.generation_training_simulation.steam_supply import (
    SteamSupply,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class PWRSteamSupply(SteamSupply):
    """Pressurized water reactor used as a steam supply to a steam turbine."""

    __slots__ = (
        "cold_leg_fb_lag_tc",
        "cold_leg_fb_lead_tc1",
        "cold_leg_fb_lead_tc2",
        "cold_leg_fg1",
        "cold_leg_fg2",
        "cold_leg_lag_tc",
        "core_ht_lag_tc1",
        "core_ht_lag_tc2",
        "core_neutronics_eff_tc",
        "core_neutronics_ht",
        "feedback_factor",
        "hot_leg_lag_tc",
        "hot_leg_steam_gain",
        "hot_leg_to_cold_leg_gain",
        "pressure_cg",
        "steam_flow_fg",
        "steam_pressure_drop_lag_tc",
        "steam_pressure_fg",
        "throttle_pressure_factor",
        "throttle_pressure_sp",
    )

    cold_leg_fb_lag_tc: float | None  # PU
    cold_leg_fb_lead_tc1: float | None  # PU
    cold_leg_fb_lead_tc2: float | None  # PU
    cold_leg_fg1: float | None  # PU
    cold_leg_fg2: float | None  # PU
    cold_leg_lag_tc: float | None  # PU
    core_ht_lag_tc1: float | None  # PU
    core_ht_lag_tc2: float | None  # PU
    core_neutronics_eff_tc: float | None  # PU
    core_neutronics_ht: float | None  # PU
    feedback_factor: float | None  # PU
    hot_leg_lag_tc: float | None  # PU
    hot_leg_steam_gain: float | None  # PU
    hot_leg_to_cold_leg_gain: float | None  # PU
    pressure_cg: float | None  # PU
    steam_flow_fg: float | None  # PU
    steam_pressure_drop_lag_tc: float | None  # PU
    steam_pressure_fg: float | None  # PU
    throttle_pressure_factor: float | None  # PU
    throttle_pressure_sp: float | None  # PU

    _cim_meta = ClassMeta(
        cim_name="PWRSteamSupply",
        package="TC57CIM/IEC61970/Base/Generation/GenerationTrainingSimulation",
        guid="{06990F92-71F6-4b0d-9CAA-2DE6B199C317}",
        attributes=(
            AttrMeta("cold_leg_fb_lag_tc", "coldLegFBLagTC", "PU", 0, 1, "cimdatatype"),
            AttrMeta("cold_leg_fb_lead_tc1", "coldLegFBLeadTC1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("cold_leg_fb_lead_tc2", "coldLegFBLeadTC2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("cold_leg_fg1", "coldLegFG1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("cold_leg_fg2", "coldLegFG2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("cold_leg_lag_tc", "coldLegLagTC", "PU", 0, 1, "cimdatatype"),
            AttrMeta("core_ht_lag_tc1", "coreHTLagTC1", "PU", 0, 1, "cimdatatype"),
            AttrMeta("core_ht_lag_tc2", "coreHTLagTC2", "PU", 0, 1, "cimdatatype"),
            AttrMeta("core_neutronics_eff_tc", "coreNeutronicsEffTC", "PU", 0, 1, "cimdatatype"),
            AttrMeta("core_neutronics_ht", "coreNeutronicsHT", "PU", 0, 1, "cimdatatype"),
            AttrMeta("feedback_factor", "feedbackFactor", "PU", 0, 1, "cimdatatype"),
            AttrMeta("hot_leg_lag_tc", "hotLegLagTC", "PU", 0, 1, "cimdatatype"),
            AttrMeta("hot_leg_steam_gain", "hotLegSteamGain", "PU", 0, 1, "cimdatatype"),
            AttrMeta("hot_leg_to_cold_leg_gain", "hotLegToColdLegGain", "PU", 0, 1, "cimdatatype"),
            AttrMeta("pressure_cg", "pressureCG", "PU", 0, 1, "cimdatatype"),
            AttrMeta("steam_flow_fg", "steamFlowFG", "PU", 0, 1, "cimdatatype"),
            AttrMeta(
                "steam_pressure_drop_lag_tc", "steamPressureDropLagTC", "PU", 0, 1, "cimdatatype"
            ),
            AttrMeta("steam_pressure_fg", "steamPressureFG", "PU", 0, 1, "cimdatatype"),
            AttrMeta(
                "throttle_pressure_factor", "throttlePressureFactor", "PU", 0, 1, "cimdatatype"
            ),
            AttrMeta("throttle_pressure_sp", "throttlePressureSP", "PU", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        cold_leg_fb_lag_tc: float | None = None,
        cold_leg_fb_lead_tc1: float | None = None,
        cold_leg_fb_lead_tc2: float | None = None,
        cold_leg_fg1: float | None = None,
        cold_leg_fg2: float | None = None,
        cold_leg_lag_tc: float | None = None,
        core_ht_lag_tc1: float | None = None,
        core_ht_lag_tc2: float | None = None,
        core_neutronics_eff_tc: float | None = None,
        core_neutronics_ht: float | None = None,
        feedback_factor: float | None = None,
        hot_leg_lag_tc: float | None = None,
        hot_leg_steam_gain: float | None = None,
        hot_leg_to_cold_leg_gain: float | None = None,
        pressure_cg: float | None = None,
        steam_flow_fg: float | None = None,
        steam_pressure_drop_lag_tc: float | None = None,
        steam_pressure_fg: float | None = None,
        throttle_pressure_factor: float | None = None,
        throttle_pressure_sp: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cold_leg_fb_lag_tc = cold_leg_fb_lag_tc
        self.cold_leg_fb_lead_tc1 = cold_leg_fb_lead_tc1
        self.cold_leg_fb_lead_tc2 = cold_leg_fb_lead_tc2
        self.cold_leg_fg1 = cold_leg_fg1
        self.cold_leg_fg2 = cold_leg_fg2
        self.cold_leg_lag_tc = cold_leg_lag_tc
        self.core_ht_lag_tc1 = core_ht_lag_tc1
        self.core_ht_lag_tc2 = core_ht_lag_tc2
        self.core_neutronics_eff_tc = core_neutronics_eff_tc
        self.core_neutronics_ht = core_neutronics_ht
        self.feedback_factor = feedback_factor
        self.hot_leg_lag_tc = hot_leg_lag_tc
        self.hot_leg_steam_gain = hot_leg_steam_gain
        self.hot_leg_to_cold_leg_gain = hot_leg_to_cold_leg_gain
        self.pressure_cg = pressure_cg
        self.steam_flow_fg = steam_flow_fg
        self.steam_pressure_drop_lag_tc = steam_pressure_drop_lag_tc
        self.steam_pressure_fg = steam_pressure_fg
        self.throttle_pressure_factor = throttle_pressure_factor
        self.throttle_pressure_sp = throttle_pressure_sp

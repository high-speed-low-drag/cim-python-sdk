"""CIM class CompositeSwitchInfo (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_info import AssetInfo

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_asset_info.composite_switch_kind import (
        CompositeSwitchKind,
    )
    from cim_python_sdk.model.iec61970.base.core.phase_code import PhaseCode


class CompositeSwitchInfo(AssetInfo):
    """Properties of a composite switch."""

    __slots__ = (
        "ganged",
        "init_op_mode",
        "interrupting_rating",
        "kind",
        "phase_code",
        "phase_count",
        "rated_voltage",
        "remote",
        "switch_state_count",
    )

    init_op_mode: str | None
    kind: CompositeSwitchKind | None
    switch_state_count: int | None
    interrupting_rating: float | None  # CurrentFlow
    rated_voltage: float | None  # Voltage
    phase_code: PhaseCode | None
    phase_count: int | None
    remote: bool | None
    ganged: bool | None

    _cim_meta = ClassMeta(
        cim_name="CompositeSwitchInfo",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
        guid="{BCF8B2B0-005C-4b1d-9A98-EC3C473AFD22}",
        attributes=(
            AttrMeta("init_op_mode", "initOpMode", "str", 0, 1, "primitive"),
            AttrMeta("kind", "kind", "CompositeSwitchKind", 0, 1, "enumeration"),
            AttrMeta("switch_state_count", "switchStateCount", "int", 0, 1, "primitive"),
            AttrMeta(
                "interrupting_rating", "interruptingRating", "CurrentFlow", 0, 1, "cimdatatype"
            ),
            AttrMeta("rated_voltage", "ratedVoltage", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("phase_code", "phaseCode", "PhaseCode", 0, 1, "enumeration"),
            AttrMeta("phase_count", "phaseCount", "int", 0, 1, "primitive"),
            AttrMeta("remote", "remote", "bool", 0, 1, "primitive"),
            AttrMeta("ganged", "ganged", "bool", 0, 1, "primitive"),
        ),
    )

    def __init__(
        self,
        *,
        init_op_mode: str | None = None,
        kind: CompositeSwitchKind | None = None,
        switch_state_count: int | None = None,
        interrupting_rating: float | None = None,
        rated_voltage: float | None = None,
        phase_code: PhaseCode | None = None,
        phase_count: int | None = None,
        remote: bool | None = None,
        ganged: bool | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.init_op_mode = init_op_mode
        self.kind = kind
        self.switch_state_count = switch_state_count
        self.interrupting_rating = interrupting_rating
        self.rated_voltage = rated_voltage
        self.phase_code = phase_code
        self.phase_count = phase_count
        self.remote = remote
        self.ganged = ganged

"""CIM class ExternalNetworkInjection (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta
from cim_python_sdk.model.iec61970.base.wires.regulating_cond_eq import RegulatingCondEq

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any


class ExternalNetworkInjection(RegulatingCondEq):
    """This class represents the external network and it is used for IEC 60909 calculations."""

    __slots__ = (
        "governor_scd",
        "ik_second",
        "max_initial_sym_sh_c_current",
        "max_p",
        "max_q",
        "max_r0_to_x0_ratio",
        "max_r1_to_x1_ratio",
        "max_z0_to_z1_ratio",
        "min_initial_sym_sh_c_current",
        "min_p",
        "min_q",
        "min_r0_to_x0_ratio",
        "min_r1_to_x1_ratio",
        "min_z0_to_z1_ratio",
        "p",
        "q",
        "reference_priority",
        "voltage_factor",
    )

    governor_scd: float | None  # ActivePowerPerFrequency
    ik_second: bool | None
    max_initial_sym_sh_c_current: float | None  # CurrentFlow
    max_p: float | None  # ActivePower
    max_q: float | None  # ReactivePower
    max_r0_to_x0_ratio: float | None
    max_r1_to_x1_ratio: float | None
    max_z0_to_z1_ratio: float | None
    min_initial_sym_sh_c_current: float | None  # CurrentFlow
    min_p: float | None  # ActivePower
    min_q: float | None  # ReactivePower
    min_r0_to_x0_ratio: float | None
    min_r1_to_x1_ratio: float | None
    min_z0_to_z1_ratio: float | None
    reference_priority: int | None
    voltage_factor: float | None  # PU
    p: float | None  # ActivePower
    q: float | None  # ReactivePower

    _cim_meta = ClassMeta(
        cim_name="ExternalNetworkInjection",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{B7E110A4-CE7A-4414-9477-4310D44B43D0}",
        attributes=(
            AttrMeta("governor_scd", "governorSCD", "ActivePowerPerFrequency", 0, 1, "cimdatatype"),
            AttrMeta("ik_second", "ikSecond", "bool", 0, 1, "primitive"),
            AttrMeta(
                "max_initial_sym_sh_c_current",
                "maxInitialSymShCCurrent",
                "CurrentFlow",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("max_p", "maxP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_q", "maxQ", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_r0_to_x0_ratio", "maxR0ToX0Ratio", "float", 0, 1, "primitive"),
            AttrMeta("max_r1_to_x1_ratio", "maxR1ToX1Ratio", "float", 0, 1, "primitive"),
            AttrMeta("max_z0_to_z1_ratio", "maxZ0ToZ1Ratio", "float", 0, 1, "primitive"),
            AttrMeta(
                "min_initial_sym_sh_c_current",
                "minInitialSymShCCurrent",
                "CurrentFlow",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("min_p", "minP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_q", "minQ", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_r0_to_x0_ratio", "minR0ToX0Ratio", "float", 0, 1, "primitive"),
            AttrMeta("min_r1_to_x1_ratio", "minR1ToX1Ratio", "float", 0, 1, "primitive"),
            AttrMeta("min_z0_to_z1_ratio", "minZ0ToZ1Ratio", "float", 0, 1, "primitive"),
            AttrMeta("reference_priority", "referencePriority", "int", 0, 1, "primitive"),
            AttrMeta("voltage_factor", "voltageFactor", "PU", 0, 1, "cimdatatype"),
            AttrMeta("p", "p", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("q", "q", "ReactivePower", 0, 1, "cimdatatype"),
        ),
    )

    def __init__(
        self,
        *,
        governor_scd: float | None = None,
        ik_second: bool | None = None,
        max_initial_sym_sh_c_current: float | None = None,
        max_p: float | None = None,
        max_q: float | None = None,
        max_r0_to_x0_ratio: float | None = None,
        max_r1_to_x1_ratio: float | None = None,
        max_z0_to_z1_ratio: float | None = None,
        min_initial_sym_sh_c_current: float | None = None,
        min_p: float | None = None,
        min_q: float | None = None,
        min_r0_to_x0_ratio: float | None = None,
        min_r1_to_x1_ratio: float | None = None,
        min_z0_to_z1_ratio: float | None = None,
        reference_priority: int | None = None,
        voltage_factor: float | None = None,
        p: float | None = None,
        q: float | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.governor_scd = governor_scd
        self.ik_second = ik_second
        self.max_initial_sym_sh_c_current = max_initial_sym_sh_c_current
        self.max_p = max_p
        self.max_q = max_q
        self.max_r0_to_x0_ratio = max_r0_to_x0_ratio
        self.max_r1_to_x1_ratio = max_r1_to_x1_ratio
        self.max_z0_to_z1_ratio = max_z0_to_z1_ratio
        self.min_initial_sym_sh_c_current = min_initial_sym_sh_c_current
        self.min_p = min_p
        self.min_q = min_q
        self.min_r0_to_x0_ratio = min_r0_to_x0_ratio
        self.min_r1_to_x1_ratio = min_r1_to_x1_ratio
        self.min_z0_to_z1_ratio = min_z0_to_z1_ratio
        self.reference_priority = reference_priority
        self.voltage_factor = voltage_factor
        self.p = p
        self.q = q

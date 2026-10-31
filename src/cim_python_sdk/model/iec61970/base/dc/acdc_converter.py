"""CIM class ACDCConverter (TC57CIM/IEC61970/Base/DC). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal
    from cim_python_sdk.model.iec61970.base.dc.acdc_converter_dc_terminal import (
        ACDCConverterDCTerminal,
    )


class ACDCConverter(ConductingEquipment):
    """A unit with valves for three phases, together with unit control equipment, essential
    protective and switching devices, DC storage capacitors, phase reactors and auxiliaries,
    if any, used for conversion."""

    __slots__ = (
        "_dc_terminals",
        "_pcc_terminal",
        "base_s",
        "idc",
        "idle_loss",
        "max_p",
        "max_udc",
        "min_p",
        "min_udc",
        "number_of_valves",
        "p",
        "pole_loss_p",
        "q",
        "rated_udc",
        "resistive_loss",
        "switching_loss",
        "target_ppcc",
        "target_udc",
        "uc",
        "udc",
        "valve_u0",
    )

    base_s: float | None  # ApparentPower
    idc: float | None  # CurrentFlow
    idle_loss: float | None  # ActivePower
    max_udc: float | None  # Voltage
    min_udc: float | None  # Voltage
    number_of_valves: int | None
    p: float | None  # ActivePower
    pole_loss_p: float | None  # ActivePower
    q: float | None  # ReactivePower
    rated_udc: float | None  # Voltage
    resistive_loss: float | None  # Resistance
    switching_loss: float | None  # ActivePowerPerCurrentFlow
    target_ppcc: float | None  # ActivePower
    target_udc: float | None  # Voltage
    uc: float | None  # Voltage
    udc: float | None  # Voltage
    valve_u0: float | None  # Voltage
    max_p: float | None  # ActivePower
    min_p: float | None  # ActivePower

    dc_terminals: Many[ACDCConverterDCTerminal] = Many(
        EndMeta(
            name="dc_terminals",
            cim_role="DCTerminals",
            target="cim_python_sdk.model.iec61970.base.dc.acdc_converter_dc_terminal:ACDCConverterDCTerminal",
            many=True,
            lower=0,
            upper=None,
            inverse="dc_conducting_equipment",
            aggregation="none",
        )
    )
    pcc_terminal: One[Terminal] = One(
        EndMeta(
            name="pcc_terminal",
            cim_role="PccTerminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=0,
            upper=1,
            inverse="converter_dc_sides",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ACDCConverter",
        package="TC57CIM/IEC61970/Base/DC",
        guid="{7BAF3CFD-55A3-4945-B51F-D3117CCB7F89}",
        attributes=(
            AttrMeta("base_s", "baseS", "ApparentPower", 0, 1, "cimdatatype"),
            AttrMeta("idc", "idc", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("idle_loss", "idleLoss", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("max_udc", "maxUdc", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("min_udc", "minUdc", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("number_of_valves", "numberOfValves", "int", 0, 1, "primitive"),
            AttrMeta("p", "p", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("pole_loss_p", "poleLossP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("q", "q", "ReactivePower", 0, 1, "cimdatatype"),
            AttrMeta("rated_udc", "ratedUdc", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("resistive_loss", "resistiveLoss", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta(
                "switching_loss", "switchingLoss", "ActivePowerPerCurrentFlow", 0, 1, "cimdatatype"
            ),
            AttrMeta("target_ppcc", "targetPpcc", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("target_udc", "targetUdc", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("uc", "uc", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("udc", "udc", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("valve_u0", "valveU0", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("max_p", "maxP", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("min_p", "minP", "ActivePower", 0, 1, "cimdatatype"),
        ),
        ends=(
            dc_terminals.meta,
            pcc_terminal.meta,
        ),
    )

    def __init__(
        self,
        *,
        base_s: float | None = None,
        idc: float | None = None,
        idle_loss: float | None = None,
        max_udc: float | None = None,
        min_udc: float | None = None,
        number_of_valves: int | None = None,
        p: float | None = None,
        pole_loss_p: float | None = None,
        q: float | None = None,
        rated_udc: float | None = None,
        resistive_loss: float | None = None,
        switching_loss: float | None = None,
        target_ppcc: float | None = None,
        target_udc: float | None = None,
        uc: float | None = None,
        udc: float | None = None,
        valve_u0: float | None = None,
        max_p: float | None = None,
        min_p: float | None = None,
        dc_terminals: Iterable[ACDCConverterDCTerminal] | None = None,
        pcc_terminal: Terminal | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.base_s = base_s
        self.idc = idc
        self.idle_loss = idle_loss
        self.max_udc = max_udc
        self.min_udc = min_udc
        self.number_of_valves = number_of_valves
        self.p = p
        self.pole_loss_p = pole_loss_p
        self.q = q
        self.rated_udc = rated_udc
        self.resistive_loss = resistive_loss
        self.switching_loss = switching_loss
        self.target_ppcc = target_ppcc
        self.target_udc = target_udc
        self.uc = uc
        self.udc = udc
        self.valve_u0 = valve_u0
        self.max_p = max_p
        self.min_p = min_p
        if dc_terminals is not None:
            ACDCConverter.dc_terminals.extend(self, dc_terminals)
        if pcc_terminal is not None:
            self.pcc_terminal = pcc_terminal

    def add_dc_terminal(self, dc_terminal: ACDCConverterDCTerminal) -> Self:
        return ACDCConverter.dc_terminals.add(self, dc_terminal)

    def remove_dc_terminal(self, dc_terminal: ACDCConverterDCTerminal) -> Self:
        return ACDCConverter.dc_terminals.remove(self, dc_terminal)

    def clear_dc_terminals(self) -> Self:
        return ACDCConverter.dc_terminals.clear(self)

    def num_dc_terminal(self) -> int:
        return ACDCConverter.dc_terminals.count(self)

    def get_dc_terminal_by_mrid(self, mrid: str) -> ACDCConverterDCTerminal | None:
        return ACDCConverter.dc_terminals.get_by_mrid(self, mrid)

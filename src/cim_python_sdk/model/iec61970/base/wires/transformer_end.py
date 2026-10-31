"""CIM class TransformerEnd (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.winding_insulation import (
        WindingInsulation,
    )
    from cim_python_sdk.model.iec61970.base.core.base_voltage import BaseVoltage
    from cim_python_sdk.model.iec61970.base.core.terminal import Terminal
    from cim_python_sdk.model.iec61970.base.wires.phase_tap_changer import PhaseTapChanger
    from cim_python_sdk.model.iec61970.base.wires.ratio_tap_changer import RatioTapChanger
    from cim_python_sdk.model.iec61970.base.wires.transformer_core_admittance import (
        TransformerCoreAdmittance,
    )
    from cim_python_sdk.model.iec61970.base.wires.transformer_mesh_impedance import (
        TransformerMeshImpedance,
    )
    from cim_python_sdk.model.iec61970.base.wires.transformer_star_impedance import (
        TransformerStarImpedance,
    )


class TransformerEnd(IdentifiedObject):
    """A conducting connection point of a power transformer. It corresponds to a physical
    transformer winding terminal. In earlier CIM versions, the TransformerWinding class
    served a similar purpose, but this class is more flexible because it associates to
    terminal but is not a specialization of ConductingEquipment."""

    __slots__ = (
        "_base_voltage",
        "_core_admittance",
        "_from_mesh_impedance",
        "_from_winding_insulations",
        "_phase_tap_changer",
        "_ratio_tap_changer",
        "_star_impedance",
        "_terminal",
        "_to_mesh_impedance",
        "_to_winding_insulations",
        "bmag_sat",
        "end_number",
        "grounded",
        "mag_base_u",
        "mag_sat_flux",
        "rground",
        "xground",
    )

    bmag_sat: float | None  # PerCent
    end_number: int | None
    grounded: bool | None
    mag_base_u: float | None  # Voltage
    mag_sat_flux: float | None  # PerCent
    rground: float | None  # Resistance
    xground: float | None  # Reactance

    from_mesh_impedance: Many[TransformerMeshImpedance] = Many(
        EndMeta(
            name="from_mesh_impedance",
            cim_role="FromMeshImpedance",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_mesh_impedance:TransformerMeshImpedance",
            many=True,
            lower=0,
            upper=None,
            inverse="from_transformer_end",
            aggregation="none",
        )
    )
    phase_tap_changer: One[PhaseTapChanger] = One(
        EndMeta(
            name="phase_tap_changer",
            cim_role="PhaseTapChanger",
            target="cim_python_sdk.model.iec61970.base.wires.phase_tap_changer:PhaseTapChanger",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_end",
            aggregation="none",
        )
    )
    star_impedance: One[TransformerStarImpedance] = One(
        EndMeta(
            name="star_impedance",
            cim_role="StarImpedance",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_star_impedance:TransformerStarImpedance",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_end",
            aggregation="none",
        )
    )
    from_winding_insulations: Many[WindingInsulation] = Many(
        EndMeta(
            name="from_winding_insulations",
            cim_role="FromWindingInsulations",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.winding_insulation:WindingInsulation",
            many=True,
            lower=0,
            upper=None,
            inverse="from_winding",
            aggregation="none",
        )
    )
    terminal: One[Terminal] = One(
        EndMeta(
            name="terminal",
            cim_role="Terminal",
            target="cim_python_sdk.model.iec61970.base.core.terminal:Terminal",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_end",
            aggregation="none",
        )
    )
    ratio_tap_changer: One[RatioTapChanger] = One(
        EndMeta(
            name="ratio_tap_changer",
            cim_role="RatioTapChanger",
            target="cim_python_sdk.model.iec61970.base.wires.ratio_tap_changer:RatioTapChanger",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_end",
            aggregation="none",
        )
    )
    core_admittance: One[TransformerCoreAdmittance] = One(
        EndMeta(
            name="core_admittance",
            cim_role="CoreAdmittance",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_core_admittance:TransformerCoreAdmittance",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_end",
            aggregation="none",
        )
    )
    base_voltage: One[BaseVoltage] = One(
        EndMeta(
            name="base_voltage",
            cim_role="BaseVoltage",
            target="cim_python_sdk.model.iec61970.base.core.base_voltage:BaseVoltage",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_ends",
            aggregation="none",
        )
    )
    to_mesh_impedance: Many[TransformerMeshImpedance] = Many(
        EndMeta(
            name="to_mesh_impedance",
            cim_role="ToMeshImpedance",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_mesh_impedance:TransformerMeshImpedance",
            many=True,
            lower=0,
            upper=None,
            inverse="to_transformer_end",
            aggregation="none",
        )
    )
    to_winding_insulations: Many[WindingInsulation] = Many(
        EndMeta(
            name="to_winding_insulations",
            cim_role="ToWindingInsulations",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.winding_insulation:WindingInsulation",
            many=True,
            lower=0,
            upper=None,
            inverse="to_winding",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransformerEnd",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{6E6AF445-8CD5-434b-8E74-08970A4E6D95}",
        attributes=(
            AttrMeta("bmag_sat", "bmagSat", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("end_number", "endNumber", "int", 0, 1, "primitive"),
            AttrMeta("grounded", "grounded", "bool", 0, 1, "primitive"),
            AttrMeta("mag_base_u", "magBaseU", "Voltage", 0, 1, "cimdatatype"),
            AttrMeta("mag_sat_flux", "magSatFlux", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta("rground", "rground", "Resistance", 0, 1, "cimdatatype"),
            AttrMeta("xground", "xground", "Reactance", 0, 1, "cimdatatype"),
        ),
        ends=(
            from_mesh_impedance.meta,
            phase_tap_changer.meta,
            star_impedance.meta,
            from_winding_insulations.meta,
            terminal.meta,
            ratio_tap_changer.meta,
            core_admittance.meta,
            base_voltage.meta,
            to_mesh_impedance.meta,
            to_winding_insulations.meta,
        ),
    )

    def __init__(
        self,
        *,
        bmag_sat: float | None = None,
        end_number: int | None = None,
        grounded: bool | None = None,
        mag_base_u: float | None = None,
        mag_sat_flux: float | None = None,
        rground: float | None = None,
        xground: float | None = None,
        from_mesh_impedance: Iterable[TransformerMeshImpedance] | None = None,
        phase_tap_changer: PhaseTapChanger | None = None,
        star_impedance: TransformerStarImpedance | None = None,
        from_winding_insulations: Iterable[WindingInsulation] | None = None,
        terminal: Terminal | None = None,
        ratio_tap_changer: RatioTapChanger | None = None,
        core_admittance: TransformerCoreAdmittance | None = None,
        base_voltage: BaseVoltage | None = None,
        to_mesh_impedance: Iterable[TransformerMeshImpedance] | None = None,
        to_winding_insulations: Iterable[WindingInsulation] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.bmag_sat = bmag_sat
        self.end_number = end_number
        self.grounded = grounded
        self.mag_base_u = mag_base_u
        self.mag_sat_flux = mag_sat_flux
        self.rground = rground
        self.xground = xground
        if from_mesh_impedance is not None:
            TransformerEnd.from_mesh_impedance.extend(self, from_mesh_impedance)
        if phase_tap_changer is not None:
            self.phase_tap_changer = phase_tap_changer
        if star_impedance is not None:
            self.star_impedance = star_impedance
        if from_winding_insulations is not None:
            TransformerEnd.from_winding_insulations.extend(self, from_winding_insulations)
        if terminal is not None:
            self.terminal = terminal
        if ratio_tap_changer is not None:
            self.ratio_tap_changer = ratio_tap_changer
        if core_admittance is not None:
            self.core_admittance = core_admittance
        if base_voltage is not None:
            self.base_voltage = base_voltage
        if to_mesh_impedance is not None:
            TransformerEnd.to_mesh_impedance.extend(self, to_mesh_impedance)
        if to_winding_insulations is not None:
            TransformerEnd.to_winding_insulations.extend(self, to_winding_insulations)

    def add_from_mesh_impedance(self, from_mesh_impedance: TransformerMeshImpedance) -> Self:
        return TransformerEnd.from_mesh_impedance.add(self, from_mesh_impedance)

    def remove_from_mesh_impedance(self, from_mesh_impedance: TransformerMeshImpedance) -> Self:
        return TransformerEnd.from_mesh_impedance.remove(self, from_mesh_impedance)

    def clear_from_mesh_impedance(self) -> Self:
        return TransformerEnd.from_mesh_impedance.clear(self)

    def num_from_mesh_impedance(self) -> int:
        return TransformerEnd.from_mesh_impedance.count(self)

    def get_from_mesh_impedance_by_mrid(self, mrid: str) -> TransformerMeshImpedance | None:
        return TransformerEnd.from_mesh_impedance.get_by_mrid(self, mrid)

    def add_from_winding_insulation(self, from_winding_insulation: WindingInsulation) -> Self:
        return TransformerEnd.from_winding_insulations.add(self, from_winding_insulation)

    def remove_from_winding_insulation(self, from_winding_insulation: WindingInsulation) -> Self:
        return TransformerEnd.from_winding_insulations.remove(self, from_winding_insulation)

    def clear_from_winding_insulations(self) -> Self:
        return TransformerEnd.from_winding_insulations.clear(self)

    def num_from_winding_insulation(self) -> int:
        return TransformerEnd.from_winding_insulations.count(self)

    def get_from_winding_insulation_by_mrid(self, mrid: str) -> WindingInsulation | None:
        return TransformerEnd.from_winding_insulations.get_by_mrid(self, mrid)

    def add_to_mesh_impedance(self, to_mesh_impedance: TransformerMeshImpedance) -> Self:
        return TransformerEnd.to_mesh_impedance.add(self, to_mesh_impedance)

    def remove_to_mesh_impedance(self, to_mesh_impedance: TransformerMeshImpedance) -> Self:
        return TransformerEnd.to_mesh_impedance.remove(self, to_mesh_impedance)

    def clear_to_mesh_impedance(self) -> Self:
        return TransformerEnd.to_mesh_impedance.clear(self)

    def num_to_mesh_impedance(self) -> int:
        return TransformerEnd.to_mesh_impedance.count(self)

    def get_to_mesh_impedance_by_mrid(self, mrid: str) -> TransformerMeshImpedance | None:
        return TransformerEnd.to_mesh_impedance.get_by_mrid(self, mrid)

    def add_to_winding_insulation(self, to_winding_insulation: WindingInsulation) -> Self:
        return TransformerEnd.to_winding_insulations.add(self, to_winding_insulation)

    def remove_to_winding_insulation(self, to_winding_insulation: WindingInsulation) -> Self:
        return TransformerEnd.to_winding_insulations.remove(self, to_winding_insulation)

    def clear_to_winding_insulations(self) -> Self:
        return TransformerEnd.to_winding_insulations.clear(self)

    def num_to_winding_insulation(self) -> int:
        return TransformerEnd.to_winding_insulations.count(self)

    def get_to_winding_insulation_by_mrid(self, mrid: str) -> WindingInsulation | None:
        return TransformerEnd.to_winding_insulations.get_by_mrid(self, mrid)

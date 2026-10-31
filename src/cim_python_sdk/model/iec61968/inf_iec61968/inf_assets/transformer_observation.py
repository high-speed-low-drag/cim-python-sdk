"""CIM class TransformerObservation (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.procedure_data_set import ProcedureDataSet
    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.bushing_insulation_pf import (
        BushingInsulationPF,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.reconditioning import Reconditioning
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.winding_insulation import (
        WindingInsulation,
    )
    from cim_python_sdk.model.iec61970.base.wires.transformer_tank import TransformerTank


class TransformerObservation(IdentifiedObject):
    """Common information captured during transformer inspections and/or diagnostics. Note that
    some properties may be measured through other means and therefore have measurement
    values in addition to the observed values recorded here."""

    __slots__ = (
        "_bushing_insultation_pfs",
        "_procedure_data_sets",
        "_reconditioning",
        "_transformer",
        "_winding_insulation_pfs",
        "bushing_temp",
        "dga",
        "freq_resp",
        "furfural_dp",
        "hot_spot_temp",
        "oil_color",
        "oil_dielectric_strength",
        "oil_ift",
        "oil_level",
        "oil_neutralization_number",
        "pump_vibration",
        "status",
        "top_oil_temp",
        "water_content",
    )

    dga: str | None
    water_content: str | None
    oil_color: str | None
    oil_dielectric_strength: float | None  # Voltage
    oil_neutralization_number: str | None
    oil_ift: str | None
    hot_spot_temp: float | None  # Temperature
    top_oil_temp: float | None  # Temperature
    bushing_temp: float | None  # Temperature
    pump_vibration: str | None
    oil_level: str | None
    freq_resp: str | None
    furfural_dp: str | None
    status: Status | None

    transformer: One[TransformerTank] = One(
        EndMeta(
            name="transformer",
            cim_role="Transformer",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_tank:TransformerTank",
            many=False,
            lower=0,
            upper=1,
            inverse="transformer_observations",
            aggregation="none",
        )
    )
    reconditioning: One[Reconditioning] = One(
        EndMeta(
            name="reconditioning",
            cim_role="Reconditioning",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.reconditioning:Reconditioning",
            many=False,
            lower=1,
            upper=1,
            inverse="transformer_observations",
            aggregation="none",
        )
    )
    procedure_data_sets: Many[ProcedureDataSet] = Many(
        EndMeta(
            name="procedure_data_sets",
            cim_role="ProcedureDataSets",
            target="cim_python_sdk.model.iec61968.assets.procedure_data_set:ProcedureDataSet",
            many=True,
            lower=0,
            upper=None,
            inverse="transformer_observations",
            aggregation="none",
        )
    )
    winding_insulation_pfs: Many[WindingInsulation] = Many(
        EndMeta(
            name="winding_insulation_pfs",
            cim_role="WindingInsulationPFs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.winding_insulation:WindingInsulation",
            many=True,
            lower=0,
            upper=None,
            inverse="transformer_observation",
            aggregation="none",
        )
    )
    bushing_insultation_pfs: Many[BushingInsulationPF] = Many(
        EndMeta(
            name="bushing_insultation_pfs",
            cim_role="BushingInsultationPFs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.bushing_insulation_pf:BushingInsulationPF",
            many=True,
            lower=0,
            upper=None,
            inverse="transformer_observation",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TransformerObservation",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{19852455-FDDC-4a91-966A-A3D1676F6F93}",
        attributes=(
            AttrMeta("dga", "dga", "str", 0, 1, "primitive"),
            AttrMeta("water_content", "waterContent", "str", 0, 1, "primitive"),
            AttrMeta("oil_color", "oilColor", "str", 0, 1, "primitive"),
            AttrMeta(
                "oil_dielectric_strength", "oilDielectricStrength", "Voltage", 0, 1, "cimdatatype"
            ),
            AttrMeta(
                "oil_neutralization_number", "oilNeutralizationNumber", "str", 0, 1, "primitive"
            ),
            AttrMeta("oil_ift", "oilIFT", "str", 0, 1, "primitive"),
            AttrMeta("hot_spot_temp", "hotSpotTemp", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("top_oil_temp", "topOilTemp", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("bushing_temp", "bushingTemp", "Temperature", 0, 1, "cimdatatype"),
            AttrMeta("pump_vibration", "pumpVibration", "str", 0, 1, "primitive"),
            AttrMeta("oil_level", "oilLevel", "str", 0, 1, "primitive"),
            AttrMeta("freq_resp", "freqResp", "str", 0, 1, "primitive"),
            AttrMeta("furfural_dp", "furfuralDP", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            transformer.meta,
            reconditioning.meta,
            procedure_data_sets.meta,
            winding_insulation_pfs.meta,
            bushing_insultation_pfs.meta,
        ),
    )

    def __init__(
        self,
        *,
        dga: str | None = None,
        water_content: str | None = None,
        oil_color: str | None = None,
        oil_dielectric_strength: float | None = None,
        oil_neutralization_number: str | None = None,
        oil_ift: str | None = None,
        hot_spot_temp: float | None = None,
        top_oil_temp: float | None = None,
        bushing_temp: float | None = None,
        pump_vibration: str | None = None,
        oil_level: str | None = None,
        freq_resp: str | None = None,
        furfural_dp: str | None = None,
        status: Status | None = None,
        transformer: TransformerTank | None = None,
        reconditioning: Reconditioning | None = None,
        procedure_data_sets: Iterable[ProcedureDataSet] | None = None,
        winding_insulation_pfs: Iterable[WindingInsulation] | None = None,
        bushing_insultation_pfs: Iterable[BushingInsulationPF] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.dga = dga
        self.water_content = water_content
        self.oil_color = oil_color
        self.oil_dielectric_strength = oil_dielectric_strength
        self.oil_neutralization_number = oil_neutralization_number
        self.oil_ift = oil_ift
        self.hot_spot_temp = hot_spot_temp
        self.top_oil_temp = top_oil_temp
        self.bushing_temp = bushing_temp
        self.pump_vibration = pump_vibration
        self.oil_level = oil_level
        self.freq_resp = freq_resp
        self.furfural_dp = furfural_dp
        self.status = status
        if transformer is not None:
            self.transformer = transformer
        if reconditioning is not None:
            self.reconditioning = reconditioning
        if procedure_data_sets is not None:
            TransformerObservation.procedure_data_sets.extend(self, procedure_data_sets)
        if winding_insulation_pfs is not None:
            TransformerObservation.winding_insulation_pfs.extend(self, winding_insulation_pfs)
        if bushing_insultation_pfs is not None:
            TransformerObservation.bushing_insultation_pfs.extend(self, bushing_insultation_pfs)

    def add_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return TransformerObservation.procedure_data_sets.add(self, procedure_data_set)

    def remove_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return TransformerObservation.procedure_data_sets.remove(self, procedure_data_set)

    def clear_procedure_data_sets(self) -> Self:
        return TransformerObservation.procedure_data_sets.clear(self)

    def num_procedure_data_set(self) -> int:
        return TransformerObservation.procedure_data_sets.count(self)

    def get_procedure_data_set_by_mrid(self, mrid: str) -> ProcedureDataSet | None:
        return TransformerObservation.procedure_data_sets.get_by_mrid(self, mrid)

    def add_winding_insulation_pf(self, winding_insulation_pf: WindingInsulation) -> Self:
        return TransformerObservation.winding_insulation_pfs.add(self, winding_insulation_pf)

    def remove_winding_insulation_pf(self, winding_insulation_pf: WindingInsulation) -> Self:
        return TransformerObservation.winding_insulation_pfs.remove(self, winding_insulation_pf)

    def clear_winding_insulation_pfs(self) -> Self:
        return TransformerObservation.winding_insulation_pfs.clear(self)

    def num_winding_insulation_pf(self) -> int:
        return TransformerObservation.winding_insulation_pfs.count(self)

    def get_winding_insulation_pf_by_mrid(self, mrid: str) -> WindingInsulation | None:
        return TransformerObservation.winding_insulation_pfs.get_by_mrid(self, mrid)

    def add_bushing_insultation_pf(self, bushing_insultation_pf: BushingInsulationPF) -> Self:
        return TransformerObservation.bushing_insultation_pfs.add(self, bushing_insultation_pf)

    def remove_bushing_insultation_pf(self, bushing_insultation_pf: BushingInsulationPF) -> Self:
        return TransformerObservation.bushing_insultation_pfs.remove(self, bushing_insultation_pf)

    def clear_bushing_insultation_pfs(self) -> Self:
        return TransformerObservation.bushing_insultation_pfs.clear(self)

    def num_bushing_insultation_pf(self) -> int:
        return TransformerObservation.bushing_insultation_pfs.count(self)

    def get_bushing_insultation_pf_by_mrid(self, mrid: str) -> BushingInsulationPF | None:
        return TransformerObservation.bushing_insultation_pfs.get_by_mrid(self, mrid)

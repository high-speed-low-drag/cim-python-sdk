"""CIM class WindingInsulation (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.transformer_observation import (
        TransformerObservation,
    )
    from cim_python_sdk.model.iec61970.base.wires.transformer_end import TransformerEnd


class WindingInsulation(IdentifiedObject):
    """Winding insulation condition as a result of a test."""

    __slots__ = (
        "_from_winding",
        "_to_winding",
        "_transformer_observation",
        "insulation_pf_status",
        "insulation_resistance",
        "leakage_reactance",
        "status",
    )

    insulation_pf_status: str | None
    insulation_resistance: str | None
    leakage_reactance: float | None  # Reactance
    status: Status | None

    from_winding: One[TransformerEnd] = One(
        EndMeta(
            name="from_winding",
            cim_role="FromWinding",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_end:TransformerEnd",
            many=False,
            lower=1,
            upper=1,
            inverse="from_winding_insulations",
            aggregation="none",
        )
    )
    transformer_observation: One[TransformerObservation] = One(
        EndMeta(
            name="transformer_observation",
            cim_role="TransformerObservation",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.transformer_observation:TransformerObservation",
            many=False,
            lower=0,
            upper=1,
            inverse="winding_insulation_pfs",
            aggregation="none",
        )
    )
    to_winding: One[TransformerEnd] = One(
        EndMeta(
            name="to_winding",
            cim_role="ToWinding",
            target="cim_python_sdk.model.iec61970.base.wires.transformer_end:TransformerEnd",
            many=False,
            lower=1,
            upper=1,
            inverse="to_winding_insulations",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="WindingInsulation",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{465EC854-7E59-4f11-99E9-A6D9FBA7522B}",
        attributes=(
            AttrMeta("insulation_pf_status", "insulationPFStatus", "str", 0, 1, "primitive"),
            AttrMeta("insulation_resistance", "insulationResistance", "str", 0, 1, "primitive"),
            AttrMeta("leakage_reactance", "leakageReactance", "Reactance", 0, 1, "cimdatatype"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            from_winding.meta,
            transformer_observation.meta,
            to_winding.meta,
        ),
    )

    def __init__(
        self,
        *,
        insulation_pf_status: str | None = None,
        insulation_resistance: str | None = None,
        leakage_reactance: float | None = None,
        status: Status | None = None,
        from_winding: TransformerEnd | None = None,
        transformer_observation: TransformerObservation | None = None,
        to_winding: TransformerEnd | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.insulation_pf_status = insulation_pf_status
        self.insulation_resistance = insulation_resistance
        self.leakage_reactance = leakage_reactance
        self.status = status
        if from_winding is not None:
            self.from_winding = from_winding
        if transformer_observation is not None:
            self.transformer_observation = transformer_observation
        if to_winding is not None:
            self.to_winding = to_winding

"""CIM class Pole (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.structure import Structure

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.streetlight import Streetlight
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.pole_base_kind import PoleBaseKind
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.pole_preservative_kind import (
        PolePreservativeKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.pole_treatment_kind import (
        PoleTreatmentKind,
    )


class Pole(Structure):
    """Pole asset."""

    __slots__ = (
        "_streetlights",
        "base_kind",
        "breast_block",
        "classification",
        "construction",
        "diameter",
        "jpa_reference",
        "length",
        "preservative_kind",
        "species_type",
        "treated_date_time",
        "treatment_kind",
    )

    classification: str | None
    species_type: str | None
    diameter: float | None  # Length
    length: float | None  # Length
    treatment_kind: PoleTreatmentKind | None
    base_kind: PoleBaseKind | None
    preservative_kind: PolePreservativeKind | None
    treated_date_time: _dt.datetime | None
    breast_block: bool | None
    construction: str | None
    jpa_reference: str | None

    streetlights: Many[Streetlight] = Many(
        EndMeta(
            name="streetlights",
            cim_role="Streetlights",
            target="cim_python_sdk.model.iec61968.assets.streetlight:Streetlight",
            many=True,
            lower=0,
            upper=None,
            inverse="pole",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Pole",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{6005F1EA-E3BB-4318-A931-D7584D2B4EFC}",
        attributes=(
            AttrMeta("classification", "classification", "str", 0, 1, "primitive"),
            AttrMeta("species_type", "speciesType", "str", 0, 1, "primitive"),
            AttrMeta("diameter", "diameter", "Length", 0, 1, "cimdatatype"),
            AttrMeta("length", "length", "Length", 0, 1, "cimdatatype"),
            AttrMeta("treatment_kind", "treatmentKind", "PoleTreatmentKind", 0, 1, "enumeration"),
            AttrMeta("base_kind", "baseKind", "PoleBaseKind", 0, 1, "enumeration"),
            AttrMeta(
                "preservative_kind", "preservativeKind", "PolePreservativeKind", 0, 1, "enumeration"
            ),
            AttrMeta("treated_date_time", "treatedDateTime", "datetime", 0, 1, "primitive"),
            AttrMeta("breast_block", "breastBlock", "bool", 0, 1, "primitive"),
            AttrMeta("construction", "construction", "str", 0, 1, "primitive"),
            AttrMeta("jpa_reference", "jpaReference", "str", 0, 1, "primitive"),
        ),
        ends=(streetlights.meta,),
    )

    def __init__(
        self,
        *,
        classification: str | None = None,
        species_type: str | None = None,
        diameter: float | None = None,
        length: float | None = None,
        treatment_kind: PoleTreatmentKind | None = None,
        base_kind: PoleBaseKind | None = None,
        preservative_kind: PolePreservativeKind | None = None,
        treated_date_time: _dt.datetime | None = None,
        breast_block: bool | None = None,
        construction: str | None = None,
        jpa_reference: str | None = None,
        streetlights: Iterable[Streetlight] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.classification = classification
        self.species_type = species_type
        self.diameter = diameter
        self.length = length
        self.treatment_kind = treatment_kind
        self.base_kind = base_kind
        self.preservative_kind = preservative_kind
        self.treated_date_time = treated_date_time
        self.breast_block = breast_block
        self.construction = construction
        self.jpa_reference = jpa_reference
        if streetlights is not None:
            Pole.streetlights.extend(self, streetlights)

    def add_streetlight(self, streetlight: Streetlight) -> Self:
        return Pole.streetlights.add(self, streetlight)

    def remove_streetlight(self, streetlight: Streetlight) -> Self:
        return Pole.streetlights.remove(self, streetlight)

    def clear_streetlights(self) -> Self:
        return Pole.streetlights.clear(self)

    def num_streetlight(self) -> int:
        return Pole.streetlights.count(self)

    def get_streetlight_by_mrid(self, mrid: str) -> Streetlight | None:
        return Pole.streetlights.get_by_mrid(self, mrid)

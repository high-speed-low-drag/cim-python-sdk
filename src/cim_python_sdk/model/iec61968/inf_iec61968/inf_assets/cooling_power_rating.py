"""CIM class CoolingPowerRating (TC57CIM/IEC61968/InfIEC61968/InfAssets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.cooling_kind import CoolingKind
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.reconditioning import Reconditioning


class CoolingPowerRating(IdentifiedObject):
    """There are often stages of power which are associated with stages of cooling. For
    instance, a transformer may be rated 121kV on the primary, 15kV on the secondary and 4kV
    on the tertiary winding. These are voltage ratings and the power ratings are generally
    the same for all three windings and independent of the voltage ratings, there are
    instances where the tertiary may have a lower power rating.

    For example, for three stages, the power rating may be 15/20/25 MVA and the cooling is
    OA/FA/FOA. The 15 MVA rating goes with the OA cooling (Oil and Air cooling). This is
    called the self cooled rating as there are no external cooling enhancements. The 20 MVA
    rating goes with the FA cooling (Forced Air cooling), this means that when the fans are
    running and thus enhancing the cooling characteristics, the transformer can operate at a
    power level of 20 MVA. The 25 MVA rating goes with the FOA cooling (Forced Oil and Air
    cooling), this means that when the fans and pumps are running and thus enhancing the
    cooling characteristics even more than before, the transformer can operate at a power
    level of 25 MVA. This 15/20/25 MVA does not state how the power is split between the
    various windings. It may be 25 MVA input on the primary, 25 MVA output on the secondary
    and 0 MVA output on the tertiary. It may also operate at 25 MVA input on the primary, 17
    MVA output on the secondary and 8 MVA output on the tertiary."""

    __slots__ = ("_reconditionings", "cooling_kind", "power_rating", "stage")

    cooling_kind: CoolingKind | None
    stage: int | None
    power_rating: float | None  # ApparentPower

    reconditionings: Many[Reconditioning] = Many(
        EndMeta(
            name="reconditionings",
            cim_role="Reconditionings",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.reconditioning:Reconditioning",
            many=True,
            lower=0,
            upper=None,
            inverse="power_ratings",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CoolingPowerRating",
        package="TC57CIM/IEC61968/InfIEC61968/InfAssets",
        guid="{2CAE8CD4-F78A-402e-9CF9-45A50E9A7D30}",
        attributes=(
            AttrMeta("cooling_kind", "coolingKind", "CoolingKind", 0, 1, "enumeration"),
            AttrMeta("stage", "stage", "int", 0, 1, "primitive"),
            AttrMeta("power_rating", "powerRating", "ApparentPower", 0, 1, "cimdatatype"),
        ),
        ends=(reconditionings.meta,),
    )

    def __init__(
        self,
        *,
        cooling_kind: CoolingKind | None = None,
        stage: int | None = None,
        power_rating: float | None = None,
        reconditionings: Iterable[Reconditioning] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.cooling_kind = cooling_kind
        self.stage = stage
        self.power_rating = power_rating
        if reconditionings is not None:
            CoolingPowerRating.reconditionings.extend(self, reconditionings)

    def add_reconditioning(self, reconditioning: Reconditioning) -> Self:
        return CoolingPowerRating.reconditionings.add(self, reconditioning)

    def remove_reconditioning(self, reconditioning: Reconditioning) -> Self:
        return CoolingPowerRating.reconditionings.remove(self, reconditioning)

    def clear_reconditionings(self) -> Self:
        return CoolingPowerRating.reconditionings.clear(self)

    def num_reconditioning(self) -> int:
        return CoolingPowerRating.reconditionings.count(self)

    def get_reconditioning_by_mrid(self, mrid: str) -> Reconditioning | None:
        return CoolingPowerRating.reconditionings.get_by_mrid(self, mrid)

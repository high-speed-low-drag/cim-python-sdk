"""CIM class AssetTestSampleTaker (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset_organisation_role import AssetOrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.specimen import Specimen


class AssetTestSampleTaker(AssetOrganisationRole):
    """Identity of person/organization that took sample."""

    __slots__ = ("_specimen",)

    specimen: Many[Specimen] = Many(
        EndMeta(
            name="specimen",
            cim_role="Specimen",
            target="cim_python_sdk.model.iec61968.assets.specimen:Specimen",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_test_sample_taker",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetTestSampleTaker",
        package="TC57CIM/IEC61968/Assets",
        guid="{60605479-B20A-41da-B346-408E713B0070}",
        ends=(specimen.meta,),
    )

    def __init__(
        self,
        *,
        specimen: Iterable[Specimen] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if specimen is not None:
            AssetTestSampleTaker.specimen.extend(self, specimen)

    def add_specimen(self, specimen: Specimen) -> Self:
        return AssetTestSampleTaker.specimen.add(self, specimen)

    def remove_specimen(self, specimen: Specimen) -> Self:
        return AssetTestSampleTaker.specimen.remove(self, specimen)

    def clear_specimen(self) -> Self:
        return AssetTestSampleTaker.specimen.clear(self)

    def num_specimen(self) -> int:
        return AssetTestSampleTaker.specimen.count(self)

    def get_specimen_by_mrid(self, mrid: str) -> Specimen | None:
        return AssetTestSampleTaker.specimen.get_by_mrid(self, mrid)

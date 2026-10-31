"""CIM class AssetTestLab (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.assets.asset_organisation_role import AssetOrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.lab_test_data_set import LabTestDataSet


class AssetTestLab(AssetOrganisationRole):
    """Test lab that performs various types of testing related to assets."""

    __slots__ = ("_lab_test_data_set",)

    lab_test_data_set: Many[LabTestDataSet] = Many(
        EndMeta(
            name="lab_test_data_set",
            cim_role="LabTestDataSet",
            target="cim_python_sdk.model.iec61968.assets.lab_test_data_set:LabTestDataSet",
            many=True,
            lower=0,
            upper=None,
            inverse="asset_test_lab",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetTestLab",
        package="TC57CIM/IEC61968/Assets",
        guid="{C5648348-94C3-4a7e-840C-430396199E06}",
        ends=(lab_test_data_set.meta,),
    )

    def __init__(
        self,
        *,
        lab_test_data_set: Iterable[LabTestDataSet] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if lab_test_data_set is not None:
            AssetTestLab.lab_test_data_set.extend(self, lab_test_data_set)

    def add_lab_test_data_set(self, lab_test_data_set: LabTestDataSet) -> Self:
        return AssetTestLab.lab_test_data_set.add(self, lab_test_data_set)

    def remove_lab_test_data_set(self, lab_test_data_set: LabTestDataSet) -> Self:
        return AssetTestLab.lab_test_data_set.remove(self, lab_test_data_set)

    def clear_lab_test_data_set(self) -> Self:
        return AssetTestLab.lab_test_data_set.clear(self)

    def num_lab_test_data_set(self) -> int:
        return AssetTestLab.lab_test_data_set.count(self)

    def get_lab_test_data_set_by_mrid(self, mrid: str) -> LabTestDataSet | None:
        return AssetTestLab.lab_test_data_set.get_by_mrid(self, mrid)

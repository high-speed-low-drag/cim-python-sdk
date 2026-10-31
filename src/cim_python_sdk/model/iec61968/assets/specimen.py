"""CIM class Specimen (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset_test_sample_taker import AssetTestSampleTaker
    from cim_python_sdk.model.iec61968.assets.lab_test_data_set import LabTestDataSet


class Specimen(IdentifiedObject):
    """Sample or specimen of a material (fluid or solid)."""

    __slots__ = (
        "_asset_test_sample_taker",
        "_lab_test_data_set",
        "ambient_temperature_at_sampling",
        "humidity_at_sampling",
        "specimen_id",
        "specimen_sample_date_time",
        "specimen_to_lab_date_time",
    )

    specimen_id: str | None
    specimen_sample_date_time: _dt.datetime | None
    ambient_temperature_at_sampling: float | None  # Temperature
    humidity_at_sampling: float | None  # PerCent
    specimen_to_lab_date_time: _dt.datetime | None

    asset_test_sample_taker: One[AssetTestSampleTaker] = One(
        EndMeta(
            name="asset_test_sample_taker",
            cim_role="AssetTestSampleTaker",
            target="cim_python_sdk.model.iec61968.assets.asset_test_sample_taker:AssetTestSampleTaker",
            many=False,
            lower=0,
            upper=1,
            inverse="specimen",
            aggregation="none",
        )
    )
    lab_test_data_set: Many[LabTestDataSet] = Many(
        EndMeta(
            name="lab_test_data_set",
            cim_role="LabTestDataSet",
            target="cim_python_sdk.model.iec61968.assets.lab_test_data_set:LabTestDataSet",
            many=True,
            lower=0,
            upper=None,
            inverse="specimen",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Specimen",
        package="TC57CIM/IEC61968/Assets",
        guid="{DCE4CB8A-10F1-401d-AD1A-60AF570E5D09}",
        attributes=(
            AttrMeta("specimen_id", "specimenID", "str", 0, 1, "primitive"),
            AttrMeta(
                "specimen_sample_date_time", "specimenSampleDateTime", "datetime", 0, 1, "primitive"
            ),
            AttrMeta(
                "ambient_temperature_at_sampling",
                "ambientTemperatureAtSampling",
                "Temperature",
                0,
                1,
                "cimdatatype",
            ),
            AttrMeta("humidity_at_sampling", "humidityAtSampling", "PerCent", 0, 1, "cimdatatype"),
            AttrMeta(
                "specimen_to_lab_date_time", "specimenToLabDateTime", "datetime", 0, 1, "primitive"
            ),
        ),
        ends=(
            asset_test_sample_taker.meta,
            lab_test_data_set.meta,
        ),
    )

    def __init__(
        self,
        *,
        specimen_id: str | None = None,
        specimen_sample_date_time: _dt.datetime | None = None,
        ambient_temperature_at_sampling: float | None = None,
        humidity_at_sampling: float | None = None,
        specimen_to_lab_date_time: _dt.datetime | None = None,
        asset_test_sample_taker: AssetTestSampleTaker | None = None,
        lab_test_data_set: Iterable[LabTestDataSet] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.specimen_id = specimen_id
        self.specimen_sample_date_time = specimen_sample_date_time
        self.ambient_temperature_at_sampling = ambient_temperature_at_sampling
        self.humidity_at_sampling = humidity_at_sampling
        self.specimen_to_lab_date_time = specimen_to_lab_date_time
        if asset_test_sample_taker is not None:
            self.asset_test_sample_taker = asset_test_sample_taker
        if lab_test_data_set is not None:
            Specimen.lab_test_data_set.extend(self, lab_test_data_set)

    def add_lab_test_data_set(self, lab_test_data_set: LabTestDataSet) -> Self:
        return Specimen.lab_test_data_set.add(self, lab_test_data_set)

    def remove_lab_test_data_set(self, lab_test_data_set: LabTestDataSet) -> Self:
        return Specimen.lab_test_data_set.remove(self, lab_test_data_set)

    def clear_lab_test_data_set(self) -> Self:
        return Specimen.lab_test_data_set.clear(self)

    def num_lab_test_data_set(self) -> int:
        return Specimen.lab_test_data_set.count(self)

    def get_lab_test_data_set_by_mrid(self, mrid: str) -> LabTestDataSet | None:
        return Specimen.lab_test_data_set.get_by_mrid(self, mrid)

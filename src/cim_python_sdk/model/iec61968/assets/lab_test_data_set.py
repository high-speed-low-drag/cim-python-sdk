"""CIM class LabTestDataSet (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.assets.procedure_data_set import ProcedureDataSet

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.asset_test_lab import AssetTestLab
    from cim_python_sdk.model.iec61968.assets.specimen import Specimen
    from cim_python_sdk.model.iec61968.assets.test_reason import TestReason


class LabTestDataSet(ProcedureDataSet):
    """Results of testing done by a lab."""

    __slots__ = (
        "_asset_test_lab",
        "_specimen",
        "conclusion",
        "conclusion_confidence",
        "reason_for_test",
        "test_equipment_id",
    )

    reason_for_test: TestReason | None
    test_equipment_id: str | None
    conclusion: str | None
    conclusion_confidence: str | None

    asset_test_lab: One[AssetTestLab] = One(
        EndMeta(
            name="asset_test_lab",
            cim_role="AssetTestLab",
            target="cim_python_sdk.model.iec61968.assets.asset_test_lab:AssetTestLab",
            many=False,
            lower=0,
            upper=1,
            inverse="lab_test_data_set",
            aggregation="none",
        )
    )
    specimen: One[Specimen] = One(
        EndMeta(
            name="specimen",
            cim_role="Specimen",
            target="cim_python_sdk.model.iec61968.assets.specimen:Specimen",
            many=False,
            lower=0,
            upper=1,
            inverse="lab_test_data_set",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="LabTestDataSet",
        package="TC57CIM/IEC61968/Assets",
        guid="{E43E62E6-3131-40cd-AFB4-E98F6F6DA528}",
        attributes=(
            AttrMeta("reason_for_test", "reasonForTest", "TestReason", 0, 1, "enumeration"),
            AttrMeta("test_equipment_id", "testEquipmentID", "str", 0, 1, "primitive"),
            AttrMeta("conclusion", "conclusion", "str", 0, 1, "primitive"),
            AttrMeta("conclusion_confidence", "conclusionConfidence", "str", 0, 1, "primitive"),
        ),
        ends=(
            asset_test_lab.meta,
            specimen.meta,
        ),
    )

    def __init__(
        self,
        *,
        reason_for_test: TestReason | None = None,
        test_equipment_id: str | None = None,
        conclusion: str | None = None,
        conclusion_confidence: str | None = None,
        asset_test_lab: AssetTestLab | None = None,
        specimen: Specimen | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.reason_for_test = reason_for_test
        self.test_equipment_id = test_equipment_id
        self.conclusion = conclusion
        self.conclusion_confidence = conclusion_confidence
        if asset_test_lab is not None:
            self.asset_test_lab = asset_test_lab
        if specimen is not None:
            self.specimen = specimen

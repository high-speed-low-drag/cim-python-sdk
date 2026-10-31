"""CIM class AssetAnalog (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.meas.analog import Analog

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.test_standard import TestStandard


class AssetAnalog(Analog):
    """Definition of type of analog useful in asset domain."""

    __slots__ = ("_test_standard", "detection_limit", "precision", "reporting_temperature")

    precision: float | None
    reporting_temperature: float | None  # Temperature
    detection_limit: float | None

    test_standard: One[TestStandard] = One(
        EndMeta(
            name="test_standard",
            cim_role="TestStandard",
            target="cim_python_sdk.model.iec61968.assets.test_standard:TestStandard",
            many=False,
            lower=0,
            upper=1,
            inverse="asset_analog",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetAnalog",
        package="TC57CIM/IEC61968/AssetMeas",
        guid="{E20744C8-D46C-4617-957B-8FC0E2B39179}",
        attributes=(
            AttrMeta("precision", "precision", "float", 0, 1, "primitive"),
            AttrMeta(
                "reporting_temperature", "reportingTemperature", "Temperature", 0, 1, "cimdatatype"
            ),
            AttrMeta("detection_limit", "detectionLimit", "float", 0, 1, "primitive"),
        ),
        ends=(test_standard.meta,),
    )

    def __init__(
        self,
        *,
        precision: float | None = None,
        reporting_temperature: float | None = None,
        detection_limit: float | None = None,
        test_standard: TestStandard | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.precision = precision
        self.reporting_temperature = reporting_temperature
        self.detection_limit = detection_limit
        if test_standard is not None:
            self.test_standard = test_standard

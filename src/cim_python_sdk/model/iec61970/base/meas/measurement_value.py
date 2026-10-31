"""CIM class MeasurementValue (TC57CIM/IEC61970/Base/Meas). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.meas.io_point import IOPoint

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.asset_meas.calculation_method_hierarchy import (
        CalculationMethodHierarchy,
    )
    from cim_python_sdk.model.iec61968.assets.procedure_data_set import ProcedureDataSet
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person import OldPerson
    from cim_python_sdk.model.iec61970.base.meas.measurement_value_quality import (
        MeasurementValueQuality,
    )
    from cim_python_sdk.model.iec61970.base.meas.measurement_value_source import (
        MeasurementValueSource,
    )
    from cim_python_sdk.model.iec61970.base.scada.remote_source import RemoteSource


class MeasurementValue(IOPoint):
    """The current state for a measurement. A state value is an instance of a measurement from
    a specific source. Measurements can be associated with many state values, each
    representing a different source for the measurement."""

    __slots__ = (
        "_calculation_method_hierarchy",
        "_erp_person",
        "_measurement_value_quality",
        "_measurement_value_source",
        "_procedure_data_set",
        "_remote_source",
        "sensor_accuracy",
        "time_stamp",
    )

    time_stamp: _dt.datetime | None
    sensor_accuracy: float | None  # PerCent

    calculation_method_hierarchy: One[CalculationMethodHierarchy] = One(
        EndMeta(
            name="calculation_method_hierarchy",
            cim_role="CalculationMethodHierarchy",
            target="cim_python_sdk.model.iec61968.asset_meas.calculation_method_hierarchy:CalculationMethodHierarchy",
            many=False,
            lower=0,
            upper=1,
            inverse="measurement_value",
            aggregation="none",
        )
    )
    procedure_data_set: Many[ProcedureDataSet] = Many(
        EndMeta(
            name="procedure_data_set",
            cim_role="ProcedureDataSet",
            target="cim_python_sdk.model.iec61968.assets.procedure_data_set:ProcedureDataSet",
            many=True,
            lower=0,
            upper=None,
            inverse="measurement_value",
            aggregation="none",
        )
    )
    measurement_value_source: One[MeasurementValueSource] = One(
        EndMeta(
            name="measurement_value_source",
            cim_role="MeasurementValueSource",
            target="cim_python_sdk.model.iec61970.base.meas.measurement_value_source:MeasurementValueSource",
            many=False,
            lower=1,
            upper=1,
            inverse="measurement_values",
            aggregation="none",
        )
    )
    remote_source: One[RemoteSource] = One(
        EndMeta(
            name="remote_source",
            cim_role="RemoteSource",
            target="cim_python_sdk.model.iec61970.base.scada.remote_source:RemoteSource",
            many=False,
            lower=0,
            upper=1,
            inverse="measurement_value",
            aggregation="none",
        )
    )
    measurement_value_quality: One[MeasurementValueQuality] = One(
        EndMeta(
            name="measurement_value_quality",
            cim_role="MeasurementValueQuality",
            target="cim_python_sdk.model.iec61970.base.meas.measurement_value_quality:MeasurementValueQuality",
            many=False,
            lower=0,
            upper=1,
            inverse="measurement_value",
            aggregation="shared",
        )
    )
    erp_person: One[OldPerson] = One(
        EndMeta(
            name="erp_person",
            cim_role="ErpPerson",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_common.old_person:OldPerson",
            many=False,
            lower=0,
            upper=1,
            inverse="measurement_values",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="MeasurementValue",
        package="TC57CIM/IEC61970/Base/Meas",
        guid="{E6D7B57A-456A-43b5-838B-3CFB466EE4C4}",
        attributes=(
            AttrMeta("time_stamp", "timeStamp", "datetime", 0, 1, "primitive"),
            AttrMeta("sensor_accuracy", "sensorAccuracy", "PerCent", 0, 1, "cimdatatype"),
        ),
        ends=(
            calculation_method_hierarchy.meta,
            procedure_data_set.meta,
            measurement_value_source.meta,
            remote_source.meta,
            measurement_value_quality.meta,
            erp_person.meta,
        ),
    )

    def __init__(
        self,
        *,
        time_stamp: _dt.datetime | None = None,
        sensor_accuracy: float | None = None,
        calculation_method_hierarchy: CalculationMethodHierarchy | None = None,
        procedure_data_set: Iterable[ProcedureDataSet] | None = None,
        measurement_value_source: MeasurementValueSource | None = None,
        remote_source: RemoteSource | None = None,
        measurement_value_quality: MeasurementValueQuality | None = None,
        erp_person: OldPerson | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.time_stamp = time_stamp
        self.sensor_accuracy = sensor_accuracy
        if calculation_method_hierarchy is not None:
            self.calculation_method_hierarchy = calculation_method_hierarchy
        if procedure_data_set is not None:
            MeasurementValue.procedure_data_set.extend(self, procedure_data_set)
        if measurement_value_source is not None:
            self.measurement_value_source = measurement_value_source
        if remote_source is not None:
            self.remote_source = remote_source
        if measurement_value_quality is not None:
            self.measurement_value_quality = measurement_value_quality
        if erp_person is not None:
            self.erp_person = erp_person

    def add_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return MeasurementValue.procedure_data_set.add(self, procedure_data_set)

    def remove_procedure_data_set(self, procedure_data_set: ProcedureDataSet) -> Self:
        return MeasurementValue.procedure_data_set.remove(self, procedure_data_set)

    def clear_procedure_data_set(self) -> Self:
        return MeasurementValue.procedure_data_set.clear(self)

    def num_procedure_data_set(self) -> int:
        return MeasurementValue.procedure_data_set.count(self)

    def get_procedure_data_set_by_mrid(self, mrid: str) -> ProcedureDataSet | None:
        return MeasurementValue.procedure_data_set.get_by_mrid(self, mrid)

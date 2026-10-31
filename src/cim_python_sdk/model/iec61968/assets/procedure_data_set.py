"""CIM class ProcedureDataSet (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.procedure import Procedure
    from cim_python_sdk.model.iec61968.common.user_attribute import UserAttribute
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.transformer_observation import (
        TransformerObservation,
    )
    from cim_python_sdk.model.iec61968.work.work_task import WorkTask
    from cim_python_sdk.model.iec61970.base.meas.measurement_value import MeasurementValue


class ProcedureDataSet(Document):
    """A data set recorded each time a procedure is executed. Observed results are captured in
    associated measurement values and/or values for properties relevant to the type of
    procedure performed."""

    __slots__ = (
        "_asset",
        "_measurement_value",
        "_procedure",
        "_properties",
        "_transformer_observations",
        "_work_task",
        "completed_date_time",
    )

    completed_date_time: _dt.datetime | None

    properties: Many[UserAttribute] = Many(
        EndMeta(
            name="properties",
            cim_role="Properties",
            target="cim_python_sdk.model.iec61968.common.user_attribute:UserAttribute",
            many=True,
            lower=0,
            upper=None,
            inverse="procedure_data_sets",
            aggregation="none",
        )
    )
    work_task: One[WorkTask] = One(
        EndMeta(
            name="work_task",
            cim_role="WorkTask",
            target="cim_python_sdk.model.iec61968.work.work_task:WorkTask",
            many=False,
            lower=0,
            upper=1,
            inverse="procedure_data_set",
            aggregation="none",
        )
    )
    transformer_observations: Many[TransformerObservation] = Many(
        EndMeta(
            name="transformer_observations",
            cim_role="TransformerObservations",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_assets.transformer_observation:TransformerObservation",
            many=True,
            lower=0,
            upper=None,
            inverse="procedure_data_sets",
            aggregation="none",
        )
    )
    measurement_value: Many[MeasurementValue] = Many(
        EndMeta(
            name="measurement_value",
            cim_role="MeasurementValue",
            target="cim_python_sdk.model.iec61970.base.meas.measurement_value:MeasurementValue",
            many=True,
            lower=0,
            upper=None,
            inverse="procedure_data_set",
            aggregation="none",
        )
    )
    procedure: One[Procedure] = One(
        EndMeta(
            name="procedure",
            cim_role="Procedure",
            target="cim_python_sdk.model.iec61968.assets.procedure:Procedure",
            many=False,
            lower=0,
            upper=1,
            inverse="procedure_data_sets",
            aggregation="none",
        )
    )
    asset: One[Asset] = One(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="procedure_data_set",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ProcedureDataSet",
        package="TC57CIM/IEC61968/Assets",
        guid="{2B18C173-DC33-4a5b-9808-CB6A18321039}",
        attributes=(
            AttrMeta("completed_date_time", "completedDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(
            properties.meta,
            work_task.meta,
            transformer_observations.meta,
            measurement_value.meta,
            procedure.meta,
            asset.meta,
        ),
    )

    def __init__(
        self,
        *,
        completed_date_time: _dt.datetime | None = None,
        properties: Iterable[UserAttribute] | None = None,
        work_task: WorkTask | None = None,
        transformer_observations: Iterable[TransformerObservation] | None = None,
        measurement_value: Iterable[MeasurementValue] | None = None,
        procedure: Procedure | None = None,
        asset: Asset | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.completed_date_time = completed_date_time
        if properties is not None:
            ProcedureDataSet.properties.extend(self, properties)
        if work_task is not None:
            self.work_task = work_task
        if transformer_observations is not None:
            ProcedureDataSet.transformer_observations.extend(self, transformer_observations)
        if measurement_value is not None:
            ProcedureDataSet.measurement_value.extend(self, measurement_value)
        if procedure is not None:
            self.procedure = procedure
        if asset is not None:
            self.asset = asset

    def add_property(self, property: UserAttribute) -> Self:
        return ProcedureDataSet.properties.add(self, property)

    def remove_property(self, property: UserAttribute) -> Self:
        return ProcedureDataSet.properties.remove(self, property)

    def clear_properties(self) -> Self:
        return ProcedureDataSet.properties.clear(self)

    def num_property(self) -> int:
        return ProcedureDataSet.properties.count(self)

    def add_transformer_observation(self, transformer_observation: TransformerObservation) -> Self:
        return ProcedureDataSet.transformer_observations.add(self, transformer_observation)

    def remove_transformer_observation(
        self, transformer_observation: TransformerObservation
    ) -> Self:
        return ProcedureDataSet.transformer_observations.remove(self, transformer_observation)

    def clear_transformer_observations(self) -> Self:
        return ProcedureDataSet.transformer_observations.clear(self)

    def num_transformer_observation(self) -> int:
        return ProcedureDataSet.transformer_observations.count(self)

    def get_transformer_observation_by_mrid(self, mrid: str) -> TransformerObservation | None:
        return ProcedureDataSet.transformer_observations.get_by_mrid(self, mrid)

    def add_measurement_value(self, measurement_value: MeasurementValue) -> Self:
        return ProcedureDataSet.measurement_value.add(self, measurement_value)

    def remove_measurement_value(self, measurement_value: MeasurementValue) -> Self:
        return ProcedureDataSet.measurement_value.remove(self, measurement_value)

    def clear_measurement_value(self) -> Self:
        return ProcedureDataSet.measurement_value.clear(self)

    def num_measurement_value(self) -> int:
        return ProcedureDataSet.measurement_value.count(self)

    def get_measurement_value_by_mrid(self, mrid: str) -> MeasurementValue | None:
        return ProcedureDataSet.measurement_value.get_by_mrid(self, mrid)

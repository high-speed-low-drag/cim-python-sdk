"""CIM class AlternateModel (TC57CIM/IEC61970/InfIEC61970/InfPart303/AlternateModels). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.alternate_models.alternate_model_group import (
        AlternateModelGroup,
    )
    from cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.data_set import DataSet


class AlternateModel(IdentifiedObject):
    """CIM class AlternateModel."""

    __slots__ = ("_alternate_model_group", "_dataset")

    dataset: One[DataSet] = One(
        EndMeta(
            name="dataset",
            cim_role="Dataset",
            target="cim_python_sdk.model.iec61970.inf_iec61970.part303.generic_data_set.data_set:DataSet",
            many=False,
            lower=1,
            upper=1,
            inverse="alternate_model",
            aggregation="none",
        )
    )
    alternate_model_group: One[AlternateModelGroup] = One(
        EndMeta(
            name="alternate_model_group",
            cim_role="AlternateModelGroup",
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_part303.alternate_models.alternate_model_group:AlternateModelGroup",
            many=False,
            lower=1,
            upper=1,
            inverse="alternate_model",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AlternateModel",
        package="TC57CIM/IEC61970/InfIEC61970/InfPart303/AlternateModels",
        guid="{EE7CCD9D-C684-4b3d-816F-16343649AE68}",
        ends=(
            dataset.meta,
            alternate_model_group.meta,
        ),
    )

    def __init__(
        self,
        *,
        dataset: DataSet | None = None,
        alternate_model_group: AlternateModelGroup | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if dataset is not None:
            self.dataset = dataset
        if alternate_model_group is not None:
            self.alternate_model_group = alternate_model_group

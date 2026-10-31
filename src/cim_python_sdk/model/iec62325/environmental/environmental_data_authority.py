"""CIM class EnvironmentalDataAuthority (TC57CIM/IEC62325/Environmental). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.common.organisation_role import OrganisationRole

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec62325.environmental.alert_type_list import AlertTypeList
    from cim_python_sdk.model.iec62325.environmental.phenomenon_classification import (
        PhenomenonClassification,
    )


class EnvironmentalDataAuthority(OrganisationRole):
    """An entity defining classifications or categories of environmental information, like
    phenomena or alerts."""

    __slots__ = ("_alert_type_list", "_phenomenon_classification")

    alert_type_list: Many[AlertTypeList] = Many(
        EndMeta(
            name="alert_type_list",
            cim_role="AlertTypeList",
            target="cim_python_sdk.model.iec62325.environmental.alert_type_list:AlertTypeList",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_data_authority",
            aggregation="none",
        )
    )
    phenomenon_classification: Many[PhenomenonClassification] = Many(
        EndMeta(
            name="phenomenon_classification",
            cim_role="PhenomenonClassification",
            target="cim_python_sdk.model.iec62325.environmental.phenomenon_classification:PhenomenonClassification",
            many=True,
            lower=0,
            upper=None,
            inverse="environmental_data_authority",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="EnvironmentalDataAuthority",
        package="TC57CIM/IEC62325/Environmental",
        guid="{4CAE75CE-D7C1-4346-9DC7-DBDCE2A5B59F}",
        ends=(
            alert_type_list.meta,
            phenomenon_classification.meta,
        ),
    )

    def __init__(
        self,
        *,
        alert_type_list: Iterable[AlertTypeList] | None = None,
        phenomenon_classification: Iterable[PhenomenonClassification] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if alert_type_list is not None:
            EnvironmentalDataAuthority.alert_type_list.extend(self, alert_type_list)
        if phenomenon_classification is not None:
            EnvironmentalDataAuthority.phenomenon_classification.extend(
                self, phenomenon_classification
            )

    def add_alert_type_list(self, alert_type_list: AlertTypeList) -> Self:
        return EnvironmentalDataAuthority.alert_type_list.add(self, alert_type_list)

    def remove_alert_type_list(self, alert_type_list: AlertTypeList) -> Self:
        return EnvironmentalDataAuthority.alert_type_list.remove(self, alert_type_list)

    def clear_alert_type_list(self) -> Self:
        return EnvironmentalDataAuthority.alert_type_list.clear(self)

    def num_alert_type_list(self) -> int:
        return EnvironmentalDataAuthority.alert_type_list.count(self)

    def get_alert_type_list_by_mrid(self, mrid: str) -> AlertTypeList | None:
        return EnvironmentalDataAuthority.alert_type_list.get_by_mrid(self, mrid)

    def add_phenomenon_classification(
        self, phenomenon_classification: PhenomenonClassification
    ) -> Self:
        return EnvironmentalDataAuthority.phenomenon_classification.add(
            self, phenomenon_classification
        )

    def remove_phenomenon_classification(
        self, phenomenon_classification: PhenomenonClassification
    ) -> Self:
        return EnvironmentalDataAuthority.phenomenon_classification.remove(
            self, phenomenon_classification
        )

    def clear_phenomenon_classification(self) -> Self:
        return EnvironmentalDataAuthority.phenomenon_classification.clear(self)

    def num_phenomenon_classification(self) -> int:
        return EnvironmentalDataAuthority.phenomenon_classification.count(self)

    def get_phenomenon_classification_by_mrid(self, mrid: str) -> PhenomenonClassification | None:
        return EnvironmentalDataAuthority.phenomenon_classification.get_by_mrid(self, mrid)

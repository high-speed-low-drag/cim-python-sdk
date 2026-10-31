"""CIM class ConditionFactor (TC57CIM/IEC61968/InfIEC61968/InfWork). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.work_identified_object import (
    WorkIdentifiedObject,
)

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.common.status import Status
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.condition_factor_kind import (
        ConditionFactorKind,
    )
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design import Design
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location import DesignLocation
    from cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location_cu import (
        DesignLocationCU,
    )


class ConditionFactor(WorkIdentifiedObject):
    """This is to specify the various condition factors for a design that may alter the cost
    estimate or the allocation."""

    __slots__ = (
        "_design_location_cus",
        "_design_locations",
        "_designs",
        "cf_value",
        "kind",
        "status",
    )

    kind: ConditionFactorKind | None
    cf_value: str | None
    status: Status | None

    design_locations: Many[DesignLocation] = Many(
        EndMeta(
            name="design_locations",
            cim_role="DesignLocations",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location:DesignLocation",
            many=True,
            lower=0,
            upper=None,
            inverse="condition_factors",
            aggregation="none",
        )
    )
    design_location_cus: Many[DesignLocationCU] = Many(
        EndMeta(
            name="design_location_cus",
            cim_role="DesignLocationCUs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design_location_cu:DesignLocationCU",
            many=True,
            lower=0,
            upper=None,
            inverse="condition_factors",
            aggregation="none",
        )
    )
    designs: Many[Design] = Many(
        EndMeta(
            name="designs",
            cim_role="Designs",
            target="cim_python_sdk.model.iec61968.inf_iec61968.inf_work.design:Design",
            many=True,
            lower=0,
            upper=None,
            inverse="condition_factors",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ConditionFactor",
        package="TC57CIM/IEC61968/InfIEC61968/InfWork",
        guid="{0AD42B70-60D4-4b5a-85BF-A4647C70D45A}",
        attributes=(
            AttrMeta("kind", "kind", "ConditionFactorKind", 0, 1, "enumeration"),
            AttrMeta("cf_value", "cfValue", "str", 0, 1, "primitive"),
            AttrMeta("status", "status", "Status", 0, 1, "compound"),
        ),
        ends=(
            design_locations.meta,
            design_location_cus.meta,
            designs.meta,
        ),
    )

    def __init__(
        self,
        *,
        kind: ConditionFactorKind | None = None,
        cf_value: str | None = None,
        status: Status | None = None,
        design_locations: Iterable[DesignLocation] | None = None,
        design_location_cus: Iterable[DesignLocationCU] | None = None,
        designs: Iterable[Design] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        self.cf_value = cf_value
        self.status = status
        if design_locations is not None:
            ConditionFactor.design_locations.extend(self, design_locations)
        if design_location_cus is not None:
            ConditionFactor.design_location_cus.extend(self, design_location_cus)
        if designs is not None:
            ConditionFactor.designs.extend(self, designs)

    def add_design_location(self, design_location: DesignLocation) -> Self:
        return ConditionFactor.design_locations.add(self, design_location)

    def remove_design_location(self, design_location: DesignLocation) -> Self:
        return ConditionFactor.design_locations.remove(self, design_location)

    def clear_design_locations(self) -> Self:
        return ConditionFactor.design_locations.clear(self)

    def num_design_location(self) -> int:
        return ConditionFactor.design_locations.count(self)

    def get_design_location_by_mrid(self, mrid: str) -> DesignLocation | None:
        return ConditionFactor.design_locations.get_by_mrid(self, mrid)

    def add_design_location_cu(self, design_location_cu: DesignLocationCU) -> Self:
        return ConditionFactor.design_location_cus.add(self, design_location_cu)

    def remove_design_location_cu(self, design_location_cu: DesignLocationCU) -> Self:
        return ConditionFactor.design_location_cus.remove(self, design_location_cu)

    def clear_design_location_cus(self) -> Self:
        return ConditionFactor.design_location_cus.clear(self)

    def num_design_location_cu(self) -> int:
        return ConditionFactor.design_location_cus.count(self)

    def get_design_location_cu_by_mrid(self, mrid: str) -> DesignLocationCU | None:
        return ConditionFactor.design_location_cus.get_by_mrid(self, mrid)

    def add_design(self, design: Design) -> Self:
        return ConditionFactor.designs.add(self, design)

    def remove_design(self, design: Design) -> Self:
        return ConditionFactor.designs.remove(self, design)

    def clear_designs(self) -> Self:
        return ConditionFactor.designs.clear(self)

    def num_design(self) -> int:
        return ConditionFactor.designs.count(self)

    def get_design_by_mrid(self, mrid: str) -> Design | None:
        return ConditionFactor.designs.get_by_mrid(self, mrid)

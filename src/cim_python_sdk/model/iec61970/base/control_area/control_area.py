"""CIM class ControlArea (TC57CIM/IEC61970/Base/ControlArea). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.control_area.control_area_generating_unit import (
        ControlAreaGeneratingUnit,
    )
    from cim_python_sdk.model.iec61970.base.control_area.control_area_type_kind import (
        ControlAreaTypeKind,
    )
    from cim_python_sdk.model.iec61970.base.control_area.tie_flow import TieFlow
    from cim_python_sdk.model.iec61970.base.load_model.energy_area import EnergyArea
    from cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_group import EnergyGroup


class ControlArea(PowerSystemResource):
    """A control area is a grouping of generating units and/or loads and a cutset of tie lines
    (as terminals) which may be used for a variety of purposes including automatic
    generation control, power flow solution area interchange control specification, and
    input to load forecasting. All generation and load within the area defined by the
    terminals on the border are considered in the area interchange control. Note that any
    number of overlapping control area specifications can be superimposed on the physical
    model. The following general principles apply to ControlArea:

    1. The control area orientation for net interchange is positive for an import, negative
    for an export.

    2. The control area net interchange is determined by summing flows in Terminals. The
    Terminals are identified by creating a set of TieFlow objects associated with a
    ControlArea object. Each TieFlow object identifies one Terminal.

    3. In a single network model, a tie between two control areas must be modelled in both
    control area specifications, such that the two representations of the tie flow sum to
    zero.

    4. The normal orientation of Terminal flow is positive for flow into the conducting
    equipment that owns the Terminal. (i.e. flow from a bus into a device is positive.)
    However, the orientation of each flow in the control area specification must align with
    the control area convention, i.e. import is positive. If the orientation of the Terminal
    flow referenced by a TieFlow is positive into the control area, then this is confirmed
    by setting TieFlow.positiveFlowIn flag TRUE. If not, the orientation must be reversed by
    setting the TieFlow.positiveFlowIn flag FALSE."""

    __slots__ = (
        "_control_area_generating_unit",
        "_energy_area",
        "_energy_groups",
        "_tie_flow",
        "net_interchange",
        "p_tolerance",
        "type",
    )

    net_interchange: float | None  # ActivePower
    p_tolerance: float | None  # ActivePower
    type: ControlAreaTypeKind | None

    tie_flow: Many[TieFlow] = Many(
        EndMeta(
            name="tie_flow",
            cim_role="TieFlow",
            target="cim_python_sdk.model.iec61970.base.control_area.tie_flow:TieFlow",
            many=True,
            lower=0,
            upper=None,
            inverse="control_area",
            aggregation="shared",
        )
    )
    energy_area: One[EnergyArea] = One(
        EndMeta(
            name="energy_area",
            cim_role="EnergyArea",
            target="cim_python_sdk.model.iec61970.base.load_model.energy_area:EnergyArea",
            many=False,
            lower=0,
            upper=1,
            inverse="control_area",
            aggregation="none",
        )
    )
    control_area_generating_unit: Many[ControlAreaGeneratingUnit] = Many(
        EndMeta(
            name="control_area_generating_unit",
            cim_role="ControlAreaGeneratingUnit",
            target="cim_python_sdk.model.iec61970.base.control_area.control_area_generating_unit:ControlAreaGeneratingUnit",
            many=True,
            lower=0,
            upper=None,
            inverse="control_area",
            aggregation="shared",
        )
    )
    energy_groups: Many[EnergyGroup] = Many(
        EndMeta(
            name="energy_groups",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.energy_area.energy_group:EnergyGroup",
            many=True,
            lower=0,
            upper=None,
            inverse="control_area",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="ControlArea",
        package="TC57CIM/IEC61970/Base/ControlArea",
        guid="{EB35F9FE-F63C-47f6-B2E8-774B9B2735C8}",
        attributes=(
            AttrMeta("net_interchange", "netInterchange", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("p_tolerance", "pTolerance", "ActivePower", 0, 1, "cimdatatype"),
            AttrMeta("type", "type", "ControlAreaTypeKind", 0, 1, "enumeration"),
        ),
        ends=(
            tie_flow.meta,
            energy_area.meta,
            control_area_generating_unit.meta,
            energy_groups.meta,
        ),
    )

    def __init__(
        self,
        *,
        net_interchange: float | None = None,
        p_tolerance: float | None = None,
        type: ControlAreaTypeKind | None = None,
        tie_flow: Iterable[TieFlow] | None = None,
        energy_area: EnergyArea | None = None,
        control_area_generating_unit: Iterable[ControlAreaGeneratingUnit] | None = None,
        energy_groups: Iterable[EnergyGroup] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.net_interchange = net_interchange
        self.p_tolerance = p_tolerance
        self.type = type
        if tie_flow is not None:
            ControlArea.tie_flow.extend(self, tie_flow)
        if energy_area is not None:
            self.energy_area = energy_area
        if control_area_generating_unit is not None:
            ControlArea.control_area_generating_unit.extend(self, control_area_generating_unit)
        if energy_groups is not None:
            ControlArea.energy_groups.extend(self, energy_groups)

    def add_tie_flow(self, tie_flow: TieFlow) -> Self:
        return ControlArea.tie_flow.add(self, tie_flow)

    def remove_tie_flow(self, tie_flow: TieFlow) -> Self:
        return ControlArea.tie_flow.remove(self, tie_flow)

    def clear_tie_flow(self) -> Self:
        return ControlArea.tie_flow.clear(self)

    def num_tie_flow(self) -> int:
        return ControlArea.tie_flow.count(self)

    def get_tie_flow_by_mrid(self, mrid: str) -> TieFlow | None:
        return ControlArea.tie_flow.get_by_mrid(self, mrid)

    def add_control_area_generating_unit(
        self, control_area_generating_unit: ControlAreaGeneratingUnit
    ) -> Self:
        return ControlArea.control_area_generating_unit.add(self, control_area_generating_unit)

    def remove_control_area_generating_unit(
        self, control_area_generating_unit: ControlAreaGeneratingUnit
    ) -> Self:
        return ControlArea.control_area_generating_unit.remove(self, control_area_generating_unit)

    def clear_control_area_generating_unit(self) -> Self:
        return ControlArea.control_area_generating_unit.clear(self)

    def num_control_area_generating_unit(self) -> int:
        return ControlArea.control_area_generating_unit.count(self)

    def get_control_area_generating_unit_by_mrid(
        self, mrid: str
    ) -> ControlAreaGeneratingUnit | None:
        return ControlArea.control_area_generating_unit.get_by_mrid(self, mrid)

    def add_energy_group(self, energy_group: EnergyGroup) -> Self:
        return ControlArea.energy_groups.add(self, energy_group)

    def remove_energy_group(self, energy_group: EnergyGroup) -> Self:
        return ControlArea.energy_groups.remove(self, energy_group)

    def clear_energy_groups(self) -> Self:
        return ControlArea.energy_groups.clear(self)

    def num_energy_group(self) -> int:
        return ControlArea.energy_groups.count(self)

    def get_energy_group_by_mrid(self, mrid: str) -> EnergyGroup | None:
        return ControlArea.energy_groups.get_by_mrid(self, mrid)

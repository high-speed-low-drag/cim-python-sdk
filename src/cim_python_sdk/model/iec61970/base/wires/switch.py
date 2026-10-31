"""CIM class Switch (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many, One
from cim_python_sdk.model.iec61970.base.core.conducting_equipment import ConductingEquipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61968.load_control.connect_disconnect_function import (
        ConnectDisconnectFunction,
    )
    from cim_python_sdk.model.iec61968.operations.switch_action import SwitchAction
    from cim_python_sdk.model.iec61970.base.state_variables.sv_switch import SvSwitch
    from cim_python_sdk.model.iec61970.base.wires.composite_switch import CompositeSwitch
    from cim_python_sdk.model.iec61970.base.wires.switch_phase import SwitchPhase
    from cim_python_sdk.model.iec61970.base.wires.switch_schedule import SwitchSchedule
    from cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailability_switch_action import (
        UnavailabilitySwitchAction,
    )


class Switch(ConductingEquipment):
    """A generic device designed to close, or open, or both, one or more electric circuits. All
    switches are two terminal devices including grounding switches. The
    ACDCTerminal.connected at the two sides of the switch shall not be considered for
    assessing switch connectivity, i.e. only Switch.open, .normalOpen and .locked are
    relevant."""

    __slots__ = (
        "_composite_switch",
        "_connect_disconnect_functions",
        "_sv_switch",
        "_switch_action",
        "_switch_phase",
        "_switch_schedules",
        "_unavailability_switch_actions",
        "locked",
        "normal_open",
        "open",
        "rated_current",
        "retained",
        "switch_on_count",
        "switch_on_date",
    )

    normal_open: bool | None
    rated_current: float | None  # CurrentFlow
    switch_on_count: int | None
    switch_on_date: _dt.datetime | None
    retained: bool | None
    open: bool | None
    locked: bool | None

    unavailability_switch_actions: Many[UnavailabilitySwitchAction] = Many(
        EndMeta(
            name="unavailability_switch_actions",
            cim_role=None,
            target="cim_python_sdk.model.iec61970.inf_iec61970.inf_availability_plans.unavailability_switch_action:UnavailabilitySwitchAction",
            many=True,
            lower=0,
            upper=None,
            inverse="switch",
            aggregation="none",
        )
    )
    switch_schedules: Many[SwitchSchedule] = Many(
        EndMeta(
            name="switch_schedules",
            cim_role="SwitchSchedules",
            target="cim_python_sdk.model.iec61970.base.wires.switch_schedule:SwitchSchedule",
            many=True,
            lower=0,
            upper=None,
            inverse="switch",
            aggregation="none",
        )
    )
    connect_disconnect_functions: Many[ConnectDisconnectFunction] = Many(
        EndMeta(
            name="connect_disconnect_functions",
            cim_role="ConnectDisconnectFunctions",
            target="cim_python_sdk.model.iec61968.load_control.connect_disconnect_function:ConnectDisconnectFunction",
            many=True,
            lower=0,
            upper=None,
            inverse="switches",
            aggregation="none",
        )
    )
    composite_switch: One[CompositeSwitch] = One(
        EndMeta(
            name="composite_switch",
            cim_role="CompositeSwitch",
            target="cim_python_sdk.model.iec61970.base.wires.composite_switch:CompositeSwitch",
            many=False,
            lower=0,
            upper=1,
            inverse="switches",
            aggregation="none",
        )
    )
    switch_phase: Many[SwitchPhase] = Many(
        EndMeta(
            name="switch_phase",
            cim_role="SwitchPhase",
            target="cim_python_sdk.model.iec61970.base.wires.switch_phase:SwitchPhase",
            many=True,
            lower=0,
            upper=None,
            inverse="switch",
            aggregation="none",
        )
    )
    sv_switch: Many[SvSwitch] = Many(
        EndMeta(
            name="sv_switch",
            cim_role="SvSwitch",
            target="cim_python_sdk.model.iec61970.base.state_variables.sv_switch:SvSwitch",
            many=True,
            lower=0,
            upper=None,
            inverse="switch",
            aggregation="none",
        )
    )
    switch_action: One[SwitchAction] = One(
        EndMeta(
            name="switch_action",
            cim_role="SwitchAction",
            target="cim_python_sdk.model.iec61968.operations.switch_action:SwitchAction",
            many=False,
            lower=0,
            upper=1,
            inverse="operated_switch",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Switch",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{ACE2DDBB-536E-489a-A3A8-22589256302D}",
        attributes=(
            AttrMeta("normal_open", "normalOpen", "bool", 0, 1, "primitive"),
            AttrMeta("rated_current", "ratedCurrent", "CurrentFlow", 0, 1, "cimdatatype"),
            AttrMeta("switch_on_count", "switchOnCount", "int", 0, 1, "primitive", deprecated=True),
            AttrMeta(
                "switch_on_date", "switchOnDate", "datetime", 0, 1, "primitive", deprecated=True
            ),
            AttrMeta("retained", "retained", "bool", 0, 1, "primitive"),
            AttrMeta("open", "open", "bool", 0, 1, "primitive"),
            AttrMeta("locked", "locked", "bool", 0, 1, "primitive"),
        ),
        ends=(
            unavailability_switch_actions.meta,
            switch_schedules.meta,
            connect_disconnect_functions.meta,
            composite_switch.meta,
            switch_phase.meta,
            sv_switch.meta,
            switch_action.meta,
        ),
    )

    def __init__(
        self,
        *,
        normal_open: bool | None = None,
        rated_current: float | None = None,
        switch_on_count: int | None = None,
        switch_on_date: _dt.datetime | None = None,
        retained: bool | None = None,
        open: bool | None = None,
        locked: bool | None = None,
        unavailability_switch_actions: Iterable[UnavailabilitySwitchAction] | None = None,
        switch_schedules: Iterable[SwitchSchedule] | None = None,
        connect_disconnect_functions: Iterable[ConnectDisconnectFunction] | None = None,
        composite_switch: CompositeSwitch | None = None,
        switch_phase: Iterable[SwitchPhase] | None = None,
        sv_switch: Iterable[SvSwitch] | None = None,
        switch_action: SwitchAction | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.normal_open = normal_open
        self.rated_current = rated_current
        self.switch_on_count = switch_on_count
        self.switch_on_date = switch_on_date
        self.retained = retained
        self.open = open
        self.locked = locked
        if unavailability_switch_actions is not None:
            Switch.unavailability_switch_actions.extend(self, unavailability_switch_actions)
        if switch_schedules is not None:
            Switch.switch_schedules.extend(self, switch_schedules)
        if connect_disconnect_functions is not None:
            Switch.connect_disconnect_functions.extend(self, connect_disconnect_functions)
        if composite_switch is not None:
            self.composite_switch = composite_switch
        if switch_phase is not None:
            Switch.switch_phase.extend(self, switch_phase)
        if sv_switch is not None:
            Switch.sv_switch.extend(self, sv_switch)
        if switch_action is not None:
            self.switch_action = switch_action

    def add_unavailability_switch_action(
        self, unavailability_switch_action: UnavailabilitySwitchAction
    ) -> Self:
        return Switch.unavailability_switch_actions.add(self, unavailability_switch_action)

    def remove_unavailability_switch_action(
        self, unavailability_switch_action: UnavailabilitySwitchAction
    ) -> Self:
        return Switch.unavailability_switch_actions.remove(self, unavailability_switch_action)

    def clear_unavailability_switch_actions(self) -> Self:
        return Switch.unavailability_switch_actions.clear(self)

    def num_unavailability_switch_action(self) -> int:
        return Switch.unavailability_switch_actions.count(self)

    def get_unavailability_switch_action_by_mrid(
        self, mrid: str
    ) -> UnavailabilitySwitchAction | None:
        return Switch.unavailability_switch_actions.get_by_mrid(self, mrid)

    def add_switch_schedule(self, switch_schedule: SwitchSchedule) -> Self:
        return Switch.switch_schedules.add(self, switch_schedule)

    def remove_switch_schedule(self, switch_schedule: SwitchSchedule) -> Self:
        return Switch.switch_schedules.remove(self, switch_schedule)

    def clear_switch_schedules(self) -> Self:
        return Switch.switch_schedules.clear(self)

    def num_switch_schedule(self) -> int:
        return Switch.switch_schedules.count(self)

    def get_switch_schedule_by_mrid(self, mrid: str) -> SwitchSchedule | None:
        return Switch.switch_schedules.get_by_mrid(self, mrid)

    def add_connect_disconnect_function(
        self, connect_disconnect_function: ConnectDisconnectFunction
    ) -> Self:
        return Switch.connect_disconnect_functions.add(self, connect_disconnect_function)

    def remove_connect_disconnect_function(
        self, connect_disconnect_function: ConnectDisconnectFunction
    ) -> Self:
        return Switch.connect_disconnect_functions.remove(self, connect_disconnect_function)

    def clear_connect_disconnect_functions(self) -> Self:
        return Switch.connect_disconnect_functions.clear(self)

    def num_connect_disconnect_function(self) -> int:
        return Switch.connect_disconnect_functions.count(self)

    def get_connect_disconnect_function_by_mrid(
        self, mrid: str
    ) -> ConnectDisconnectFunction | None:
        return Switch.connect_disconnect_functions.get_by_mrid(self, mrid)

    def add_switch_phase(self, switch_phase: SwitchPhase) -> Self:
        return Switch.switch_phase.add(self, switch_phase)

    def remove_switch_phase(self, switch_phase: SwitchPhase) -> Self:
        return Switch.switch_phase.remove(self, switch_phase)

    def clear_switch_phase(self) -> Self:
        return Switch.switch_phase.clear(self)

    def num_switch_phase(self) -> int:
        return Switch.switch_phase.count(self)

    def get_switch_phase_by_mrid(self, mrid: str) -> SwitchPhase | None:
        return Switch.switch_phase.get_by_mrid(self, mrid)

    def add_sv_switch(self, sv_switch: SvSwitch) -> Self:
        return Switch.sv_switch.add(self, sv_switch)

    def remove_sv_switch(self, sv_switch: SvSwitch) -> Self:
        return Switch.sv_switch.remove(self, sv_switch)

    def clear_sv_switch(self) -> Self:
        return Switch.sv_switch.clear(self)

    def num_sv_switch(self) -> int:
        return Switch.sv_switch.count(self)

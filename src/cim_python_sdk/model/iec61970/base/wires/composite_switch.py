"""CIM class CompositeSwitch (TC57CIM/IEC61970/Base/Wires). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, Many
from cim_python_sdk.model.iec61970.base.core.equipment import Equipment

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any, Self

    from cim_python_sdk.model.iec61970.base.wires.switch import Switch


class CompositeSwitch(Equipment):
    """A model of a set of individual Switches normally enclosed within the same cabinet and
    possibly with interlocks that restrict the combination of switch positions. These are
    typically found in medium voltage distribution networks.

    A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear,
    with primitive internal devices such as an internal bus-bar plus 3 or 4 internal
    switches each of which may individually be open or closed. A CompositeSwitch and a set
    of contained Switches can also be used to represent a multi-position switch e.g. a
    switch that can connect a circuit to Ground, Open or Busbar."""

    __slots__ = ("_switches", "composite_switch_type")

    composite_switch_type: str | None

    switches: Many[Switch] = Many(
        EndMeta(
            name="switches",
            cim_role="Switches",
            target="cim_python_sdk.model.iec61970.base.wires.switch:Switch",
            many=True,
            lower=0,
            upper=None,
            inverse="composite_switch",
            aggregation="shared",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CompositeSwitch",
        package="TC57CIM/IEC61970/Base/Wires",
        guid="{6A5875D8-2294-45a2-BEE1-C33F5FEDF914}",
        attributes=(
            AttrMeta("composite_switch_type", "compositeSwitchType", "str", 0, 1, "primitive"),
        ),
        ends=(switches.meta,),
    )

    def __init__(
        self,
        *,
        composite_switch_type: str | None = None,
        switches: Iterable[Switch] | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.composite_switch_type = composite_switch_type
        if switches is not None:
            CompositeSwitch.switches.extend(self, switches)

    def add_switche(self, switche: Switch) -> Self:
        return CompositeSwitch.switches.add(self, switche)

    def remove_switche(self, switche: Switch) -> Self:
        return CompositeSwitch.switches.remove(self, switche)

    def clear_switches(self) -> Self:
        return CompositeSwitch.switches.clear(self)

    def num_switche(self) -> int:
        return CompositeSwitch.switches.count(self)

    def get_switche_by_mrid(self, mrid: str) -> Switch | None:
        return CompositeSwitch.switches.get_by_mrid(self, mrid)

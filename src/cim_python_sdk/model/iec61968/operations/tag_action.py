"""CIM class TagAction (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.operations.switching_action import SwitchingAction

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.operations.operational_tag import OperationalTag
    from cim_python_sdk.model.iec61968.operations.tag_action_kind import TagActionKind


class TagAction(SwitchingAction):
    """Action on operation tag as a switching step."""

    __slots__ = ("_operational_tag", "kind")

    kind: TagActionKind | None

    operational_tag: One[OperationalTag] = One(
        EndMeta(
            name="operational_tag",
            cim_role="OperationalTag",
            target="cim_python_sdk.model.iec61968.operations.operational_tag:OperationalTag",
            many=False,
            lower=0,
            upper=1,
            inverse="tag_action",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="TagAction",
        package="TC57CIM/IEC61968/Operations",
        guid="{E2B02A1D-2648-4060-90ED-13641B1782DF}",
        attributes=(AttrMeta("kind", "kind", "TagActionKind", 0, 1, "enumeration"),),
        ends=(operational_tag.meta,),
    )

    def __init__(
        self,
        *,
        kind: TagActionKind | None = None,
        operational_tag: OperationalTag | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.kind = kind
        if operational_tag is not None:
            self.operational_tag = operational_tag

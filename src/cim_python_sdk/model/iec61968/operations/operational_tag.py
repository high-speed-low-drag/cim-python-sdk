"""CIM class OperationalTag (TC57CIM/IEC61968/Operations). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61968.common.document import Document

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.operations.tag_action import TagAction
    from cim_python_sdk.model.iec61970.base.core.power_system_resource import PowerSystemResource


class OperationalTag(Document):
    """Operational tag placed on a power system resource or asset in the context of switching
    plan execution or other work in the field."""

    __slots__ = ("_asset", "_power_system_resource", "_tag_action")

    asset: One[Asset] = One(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="operational_tags",
            aggregation="none",
        )
    )
    tag_action: One[TagAction] = One(
        EndMeta(
            name="tag_action",
            cim_role="TagAction",
            target="cim_python_sdk.model.iec61968.operations.tag_action:TagAction",
            many=False,
            lower=0,
            upper=1,
            inverse="operational_tag",
            aggregation="none",
        )
    )
    power_system_resource: One[PowerSystemResource] = One(
        EndMeta(
            name="power_system_resource",
            cim_role="PowerSystemResource",
            target="cim_python_sdk.model.iec61970.base.core.power_system_resource:PowerSystemResource",
            many=False,
            lower=0,
            upper=1,
            inverse="operational_tags",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="OperationalTag",
        package="TC57CIM/IEC61968/Operations",
        guid="{2F8EE3CF-2319-4078-A5C2-CA89E6C8B884}",
        ends=(
            asset.meta,
            tag_action.meta,
            power_system_resource.meta,
        ),
    )

    def __init__(
        self,
        *,
        asset: Asset | None = None,
        tag_action: TagAction | None = None,
        power_system_resource: PowerSystemResource | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        if asset is not None:
            self.asset = asset
        if tag_action is not None:
            self.tag_action = tag_action
        if power_system_resource is not None:
            self.power_system_resource = power_system_resource

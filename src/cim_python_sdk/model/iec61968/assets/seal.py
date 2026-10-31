"""CIM class Seal (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    import datetime as _dt
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.asset_container import AssetContainer
    from cim_python_sdk.model.iec61968.assets.seal_condition_kind import SealConditionKind
    from cim_python_sdk.model.iec61968.assets.seal_kind import SealKind


class Seal(IdentifiedObject):
    """Physically controls access to AssetContainers."""

    __slots__ = ("_asset_container", "applied_date_time", "condition", "kind", "seal_number")

    seal_number: str | None
    kind: SealKind | None
    condition: SealConditionKind | None
    applied_date_time: _dt.datetime | None

    asset_container: One[AssetContainer] = One(
        EndMeta(
            name="asset_container",
            cim_role="AssetContainer",
            target="cim_python_sdk.model.iec61968.assets.asset_container:AssetContainer",
            many=False,
            lower=0,
            upper=1,
            inverse="seals",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Seal",
        package="TC57CIM/IEC61968/Assets",
        guid="{5CF7300B-8B0C-4c1e-AC84-6CD0EB5F8B4B}",
        attributes=(
            AttrMeta("seal_number", "sealNumber", "str", 0, 1, "primitive"),
            AttrMeta("kind", "kind", "SealKind", 0, 1, "enumeration"),
            AttrMeta("condition", "condition", "SealConditionKind", 0, 1, "enumeration"),
            AttrMeta("applied_date_time", "appliedDateTime", "datetime", 0, 1, "primitive"),
        ),
        ends=(asset_container.meta,),
    )

    def __init__(
        self,
        *,
        seal_number: str | None = None,
        kind: SealKind | None = None,
        condition: SealConditionKind | None = None,
        applied_date_time: _dt.datetime | None = None,
        asset_container: AssetContainer | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.seal_number = seal_number
        self.kind = kind
        self.condition = condition
        self.applied_date_time = applied_date_time
        if asset_container is not None:
            self.asset_container = asset_container

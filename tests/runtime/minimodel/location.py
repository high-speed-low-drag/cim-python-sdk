"""CIM class Location (TC57CIM/IEC61968/Common). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from tests.runtime.minimodel.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from tests.runtime.minimodel.asset import Asset
    from tests.runtime.minimodel.street_address import StreetAddress


class Location(IdentifiedObject):
    """The place, scene, or point of something where someone or something has been, is,
    and/or will be at a given moment in time."""

    __slots__ = ("_asset", "main_address")

    main_address: StreetAddress | None

    asset: One[Asset] = One(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="tests.runtime.minimodel.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="location",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="Location",
        package="TC57CIM/IEC61968/Common",
        guid="{00000000-0000-0000-0000-00000000C007}",
        attributes=(AttrMeta("main_address", "mainAddress", "StreetAddress", 0, 1, "compound"),),
        ends=(asset.meta,),
    )

    def __init__(
        self,
        *,
        main_address: StreetAddress | None = None,
        asset: Asset | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.main_address = main_address
        if asset is not None:
            self.asset = asset

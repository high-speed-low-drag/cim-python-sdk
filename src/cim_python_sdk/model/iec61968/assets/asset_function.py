"""CIM class AssetFunction (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.asset import Asset


class AssetFunction(IdentifiedObject):
    """Function performed by an asset."""

    __slots__ = ("_asset", "config_id", "firmware_id", "hardware_id", "password", "program_id")

    program_id: str | None
    firmware_id: str | None
    hardware_id: str | None
    password: str | None
    config_id: str | None

    asset: One[Asset] = One(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="asset_function",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetFunction",
        package="TC57CIM/IEC61968/Assets",
        guid="{D61C3FF0-8CA9-4806-B99C-92A36C8B1194}",
        attributes=(
            AttrMeta("program_id", "programID", "str", 0, 1, "primitive"),
            AttrMeta("firmware_id", "firmwareID", "str", 0, 1, "primitive"),
            AttrMeta("hardware_id", "hardwareID", "str", 0, 1, "primitive"),
            AttrMeta("password", "password", "str", 0, 1, "primitive"),
            AttrMeta("config_id", "configID", "str", 0, 1, "primitive"),
        ),
        ends=(asset.meta,),
    )

    def __init__(
        self,
        *,
        program_id: str | None = None,
        firmware_id: str | None = None,
        hardware_id: str | None = None,
        password: str | None = None,
        config_id: str | None = None,
        asset: Asset | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.program_id = program_id
        self.firmware_id = firmware_id
        self.hardware_id = hardware_id
        self.password = password
        self.config_id = config_id
        if asset is not None:
            self.asset = asset

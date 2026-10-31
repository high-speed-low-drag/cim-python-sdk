"""CIM class AssetUser (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import ClassMeta
from cim_python_sdk.model.iec61968.assets.asset_organisation_role import AssetOrganisationRole


class AssetUser(AssetOrganisationRole):
    """Organisation that is a user of the asset."""

    __slots__ = ()

    _cim_meta = ClassMeta(
        cim_name="AssetUser",
        package="TC57CIM/IEC61968/Assets",
        guid="{A64B92C7-CE4E-4fa7-BD95-00DA376237FF}",
    )

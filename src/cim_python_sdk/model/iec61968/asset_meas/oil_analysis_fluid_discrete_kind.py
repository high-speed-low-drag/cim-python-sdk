"""CIM enumeration OilAnalysisFluidDiscreteKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilAnalysisFluidDiscreteKind(CimEnum):
    """Discretes representing oil fluid test analysis result."""

    colorNumber = "colorNumber"
    colorNumberPlatinumCobaltScale = "colorNumberPlatinumCobaltScale"
    corrosiveSulphurByD1275 = "corrosiveSulphurByD1275"
    corrosiveSulphurBy62535 = "corrosiveSulphurBy62535"
    corrosiveSulphurBy51353 = "corrosiveSulphurBy51353"
    tarnishLevel = "tarnishLevel"
    sludgePrecipitation = "sludgePrecipitation"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilAnalysisFluidDiscreteKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{696E81B8-3FE5-4b76-A9F4-4AECE5D7031D}",
            kind="enumeration",
        )
    )

"""CIM enumeration OilAnalysisParticleAnalogKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilAnalysisParticleAnalogKind(CimEnum):
    """Analogs representing oil particulate analysis result."""

    count2Plus = "count2Plus"
    count4Plus = "count4Plus"
    count5Plus = "count5Plus"
    count6Plus = "count6Plus"
    count10Plus = "count10Plus"
    count14Plus = "count14Plus"
    count15Plus = "count15Plus"
    count21Plus = "count21Plus"
    count25Plus = "count25Plus"
    count38Plus = "count38Plus"
    count50Plus = "count50Plus"
    count70Plus = "count70Plus"
    count100Plus = "count100Plus"
    fibrePercent = "fibrePercent"
    metalPercent = "metalPercent"
    carbonPercent = "carbonPercent"
    otherPercent = "otherPercent"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilAnalysisParticleAnalogKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{A13775D6-E276-411b-A46F-EDA3477B6EB6}",
            kind="enumeration",
        )
    )

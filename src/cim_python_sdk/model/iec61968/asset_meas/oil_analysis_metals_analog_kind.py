"""CIM enumeration OilAnalysisMetalsAnalogKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilAnalysisMetalsAnalogKind(CimEnum):
    """Analogs representing oil metals and elements analysis result."""

    aluminum = "aluminum"
    aluminumParticulate = "aluminumParticulate"
    barium = "barium"
    boron = "boron"
    calcium = "calcium"
    cadmium = "cadmium"
    chromium = "chromium"
    copper = "copper"
    copperParticulate = "copperParticulate"
    iron = "iron"
    ironParticulate = "ironParticulate"
    lead = "lead"
    leadParticulate = "leadParticulate"
    lithium = "lithium"
    molybdenum = "molybdenum"
    magnesium = "magnesium"
    nickel = "nickel"
    phosphorus = "phosphorus"
    silicon = "silicon"
    silver = "silver"
    silverParticulate = "silverParticulate"
    sodium = "sodium"
    tin = "tin"
    titanium = "titanium"
    tungsten = "tungsten"
    vanadium = "vanadium"
    zinc = "zinc"
    zincParticulate = "zincParticulate"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilAnalysisMetalsAnalogKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{6A648944-7C96-4758-9F5F-8FB935CB2505}",
            kind="enumeration",
        )
    )

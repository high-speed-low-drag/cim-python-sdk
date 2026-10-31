"""CIM enumeration WireInsulationKind (TC57CIM/IEC61968/AssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class WireInsulationKind(CimEnum):
    """Kind of wire insulation."""

    asbestosAndVarnishedCambric = "asbestosAndVarnishedCambric"
    butyl = "butyl"
    ethylenePropyleneRubber = "ethylenePropyleneRubber"
    highMolecularWeightPolyethylene = "highMolecularWeightPolyethylene"
    treeResistantHighMolecularWeightPolyethylene = "treeResistantHighMolecularWeightPolyethylene"
    lowCapacitanceRubber = "lowCapacitanceRubber"
    oilPaper = "oilPaper"
    ozoneResistantRubber = "ozoneResistantRubber"
    beltedPilc = "beltedPilc"
    unbeltedPilc = "unbeltedPilc"
    rubber = "rubber"
    siliconRubber = "siliconRubber"
    varnishedCambricCloth = "varnishedCambricCloth"
    varnishedDacronGlass = "varnishedDacronGlass"
    crosslinkedPolyethylene = "crosslinkedPolyethylene"
    treeRetardantCrosslinkedPolyethylene = "treeRetardantCrosslinkedPolyethylene"
    highPressureFluidFilled = "highPressureFluidFilled"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="WireInsulationKind",
            package="TC57CIM/IEC61968/AssetInfo",
            guid="{5DEE00A8-4B14-4375-95B6-F07914121D9E}",
            kind="enumeration",
        )
    )

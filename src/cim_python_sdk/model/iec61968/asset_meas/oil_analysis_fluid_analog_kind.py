"""CIM enumeration OilAnalysisFluidAnalogKind (TC57CIM/IEC61968/AssetMeas). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class OilAnalysisFluidAnalogKind(CimEnum):
    """Analogs representing oil fluid test analysis result."""

    acidNumber = "acidNumber"
    interfacialTension = "interfacialTension"
    dielectricBreakdown = "dielectricBreakdown"
    powerFactorPercent = "powerFactorPercent"
    dissipationFactor = "dissipationFactor"
    dissipationFactorPercent = "dissipationFactorPercent"
    oxidationInhibitorDBP = "oxidationInhibitorDBP"
    oxidationInhibitorDBPC = "oxidationInhibitorDBPC"
    oxidationInhibitorD2668 = "oxidationInhibitorD2668"
    additiveDBDS = "additiveDBDS"
    specificGravity = "specificGravity"
    density = "density"
    firePoint = "firePoint"
    flashPointOpenCup = "flashPointOpenCup"
    flashPointClosedCup = "flashPointClosedCup"
    pourPoint = "pourPoint"
    pourPointAutomatic = "pourPointAutomatic"
    kinematicViscosity = "kinematicViscosity"
    staticElectrification = "staticElectrification"
    resistivity = "resistivity"
    passivatorContent = "passivatorContent"
    passivatorIrgamet39 = "passivatorIrgamet39"
    passivatorTTA = "passivatorTTA"
    passivatorBTA = "passivatorBTA"
    sedimentAndSludgePercent = "sedimentAndSludgePercent"
    carbonyl = "carbonyl"
    aromatics = "aromatics"
    oxidation = "oxidation"
    sludge = "sludge"
    solubleAcids = "solubleAcids"
    volatileAcids = "volatileAcids"
    totalAcids = "totalAcids"
    inductionTime = "inductionTime"
    inhibitor61125MethodC = "inhibitor61125MethodC"
    duration61125MethodC = "duration61125MethodC"
    petroleumOrigin = "petroleumOrigin"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="OilAnalysisFluidAnalogKind",
            package="TC57CIM/IEC61968/AssetMeas",
            guid="{DD11BE9A-3F55-4866-A1B7-5C835F6B2DD9}",
            kind="enumeration",
        )
    )

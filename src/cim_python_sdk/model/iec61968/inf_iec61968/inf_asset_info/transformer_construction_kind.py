"""CIM enumeration TransformerConstructionKind (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TransformerConstructionKind(CimEnum):
    """Kind of transformer construction."""

    onePhase = "onePhase"
    threePhase = "threePhase"
    aerial = "aerial"
    overhead = "overhead"
    dryType = "dryType"
    network = "network"
    padmountDeadFront = "padmountDeadFront"
    padmountFeedThrough = "padmountFeedThrough"
    padmountLiveFront = "padmountLiveFront"
    padmountLoopThrough = "padmountLoopThrough"
    padmounted = "padmounted"
    subway = "subway"
    underground = "underground"
    vault = "vault"
    vaultThreePhase = "vaultThreePhase"
    unknown = "unknown"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TransformerConstructionKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
            guid="{5FDFF2F1-83A7-4a56-9ACA-6B15F6866D49}",
            kind="enumeration",
        )
    )

"""CIM enumeration TransformerFunctionKind (TC57CIM/IEC61968/InfIEC61968/InfAssetInfo). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TransformerFunctionKind(CimEnum):
    """Function of a transformer."""

    powerTransformer = "powerTransformer"
    voltageRegulator = "voltageRegulator"
    autotransformer = "autotransformer"
    secondaryTransformer = "secondaryTransformer"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TransformerFunctionKind",
            package="TC57CIM/IEC61968/InfIEC61968/InfAssetInfo",
            guid="{297A1B39-7634-4195-B755-AF5F6638BC15}",
            kind="enumeration",
        )
    )

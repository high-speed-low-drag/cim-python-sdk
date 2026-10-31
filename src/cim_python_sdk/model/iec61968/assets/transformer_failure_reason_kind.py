"""CIM enumeration TransformerFailureReasonKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TransformerFailureReasonKind(CimEnum):
    """Reason for transformer failure.

    Note: This enumeration provides essential information to asset health analytics. The
    existing list is a starting point and is anticipated to be fleshed out further as
    requirements are better understood. (PAB 2016/01/09)."""

    bushingFailure = "bushingFailure"
    lossOfOil = "lossOfOil"
    oilRelatedFailure = "oilRelatedFailure"
    poorOilQuality = "poorOilQuality"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TransformerFailureReasonKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{24239988-FB55-4831-9713-30FB47C94C6C}",
            kind="enumeration",
        )
    )

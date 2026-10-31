"""CIM enumeration TransformerApplicationKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class TransformerApplicationKind(CimEnum):
    """Classifications of network roles in which transformers can be deployed. The
    classifications are intended to reflect both criticality of transformer in network
    operations and typical usage experienced by transformer.

    Note: This enumeration provides essential information to asset health analytics. The
    existing list is a starting point and is anticipated to be fleshed out further as
    requirements are better understood (PAB 2016/01/09)."""

    transmissionBusToBus = "transmissionBusToBus"
    transmissionBusToDistribution = "transmissionBusToDistribution"
    generatorStepUp = "generatorStepUp"
    distribution = "distribution"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="TransformerApplicationKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{5B47EE8F-11D0-49d9-A4BF-3CBA8AFCBB5C}",
            kind="enumeration",
        )
    )

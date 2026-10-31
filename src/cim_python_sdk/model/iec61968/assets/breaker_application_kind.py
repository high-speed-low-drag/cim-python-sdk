"""CIM enumeration BreakerApplicationKind (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from enum import nonmember

from cim_python_sdk._runtime import CimEnum, ClassMeta


class BreakerApplicationKind(CimEnum):
    """Classifications of network roles in which breakers can be deployed. The classifications
    are intended to reflect both criticality of breaker in network operations and typical
    usage experienced by breaker.

    Note: This enumeration provides essential information to asset health analytics. The
    existing list is a starting point and is anticipated to be fleshed out further as
    requirements are better understood (PAB 2016/01/09)."""

    capacitorOrReactorBankBreaker = "capacitorOrReactorBankBreaker"
    busBreaker = "busBreaker"
    busTieBreaker = "busTieBreaker"
    feederBreaker = "feederBreaker"
    stepUpTransformerBreakerHydro = "stepUpTransformerBreakerHydro"
    stepUpTransformerBreakerFossil = "stepUpTransformerBreakerFossil"
    stepUpTransformerBreakerNuclear = "stepUpTransformerBreakerNuclear"
    stepUpTransformerBreakerPumpedStorage = "stepUpTransformerBreakerPumpedStorage"
    substationTransformerBreaker = "substationTransformerBreaker"
    transmissionFlowGateLineBreaker = "transmissionFlowGateLineBreaker"
    transmissionLineBreaker = "transmissionLineBreaker"
    transmissionTieLineBreaker = "transmissionTieLineBreaker"
    spare = "spare"
    other = "other"

    _cim_meta = nonmember(
        ClassMeta(
            cim_name="BreakerApplicationKind",
            package="TC57CIM/IEC61968/Assets",
            guid="{7FAB5599-1820-47d6-93FA-D35DB54D1DAA}",
            kind="enumeration",
        )
    )

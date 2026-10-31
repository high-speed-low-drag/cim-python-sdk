"""CIM class CombinedCycleTransitionState (TC57CIM/IEC62325/MarketOperations/ReferenceData). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, CimObject, ClassMeta, EndMeta, One

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_configuration import (
        CombinedCycleConfiguration,
    )


class CombinedCycleTransitionState(CimObject):
    """Defines the available from and to Transition States for the Combine Cycle
    Configurations."""

    __slots__ = ("_from_configuration", "_to_configuration", "up_transition")

    up_transition: bool | None

    from_configuration: One[CombinedCycleConfiguration] = One(
        EndMeta(
            name="from_configuration",
            cim_role="FromConfiguration",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_configuration:CombinedCycleConfiguration",
            many=False,
            lower=1,
            upper=1,
            inverse="from_transition_state",
            aggregation="none",
        )
    )
    to_configuration: One[CombinedCycleConfiguration] = One(
        EndMeta(
            name="to_configuration",
            cim_role="ToConfiguration",
            target="cim_python_sdk.model.iec62325.market_operations.reference_data.combined_cycle_configuration:CombinedCycleConfiguration",
            many=False,
            lower=1,
            upper=1,
            inverse="to_transition_state",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="CombinedCycleTransitionState",
        package="TC57CIM/IEC62325/MarketOperations/ReferenceData",
        guid="{82FAAEFD-CC36-4327-95CD-730766F8E669}",
        attributes=(AttrMeta("up_transition", "upTransition", "bool", 0, 1, "primitive"),),
        ends=(
            from_configuration.meta,
            to_configuration.meta,
        ),
    )

    def __init__(
        self,
        *,
        up_transition: bool | None = None,
        from_configuration: CombinedCycleConfiguration | None = None,
        to_configuration: CombinedCycleConfiguration | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.up_transition = up_transition
        if from_configuration is not None:
            self.from_configuration = from_configuration
        if to_configuration is not None:
            self.to_configuration = to_configuration

"""CIM class AssetDeployment (TC57CIM/IEC61968/Assets). Generated code: do not edit."""

from __future__ import annotations

from cim_python_sdk._runtime import AttrMeta, ClassMeta, EndMeta, One
from cim_python_sdk.model.iec61970.base.core.identified_object import IdentifiedObject

TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import Any

    from cim_python_sdk.model.iec61968.assets.asset import Asset
    from cim_python_sdk.model.iec61968.assets.breaker_application_kind import BreakerApplicationKind
    from cim_python_sdk.model.iec61968.assets.deployment_date import DeploymentDate
    from cim_python_sdk.model.iec61968.assets.deployment_state_kind import DeploymentStateKind
    from cim_python_sdk.model.iec61968.assets.facility_kind import FacilityKind
    from cim_python_sdk.model.iec61968.assets.transformer_application_kind import (
        TransformerApplicationKind,
    )
    from cim_python_sdk.model.iec61970.base.core.base_voltage import BaseVoltage


class AssetDeployment(IdentifiedObject):
    """Deployment of asset deployment in a power system resource role."""

    __slots__ = (
        "_asset",
        "_base_voltage",
        "breaker_application",
        "deployment_date",
        "deployment_state",
        "facility_kind",
        "likelihood_of_failure",
        "transformer_application",
    )

    deployment_state: DeploymentStateKind | None
    deployment_date: DeploymentDate | None
    breaker_application: BreakerApplicationKind | None
    transformer_application: TransformerApplicationKind | None
    likelihood_of_failure: int | None
    facility_kind: FacilityKind | None

    asset: One[Asset] = One(
        EndMeta(
            name="asset",
            cim_role="Asset",
            target="cim_python_sdk.model.iec61968.assets.asset:Asset",
            many=False,
            lower=0,
            upper=1,
            inverse="asset_deployment",
            aggregation="none",
        )
    )
    base_voltage: One[BaseVoltage] = One(
        EndMeta(
            name="base_voltage",
            cim_role="BaseVoltage",
            target="cim_python_sdk.model.iec61970.base.core.base_voltage:BaseVoltage",
            many=False,
            lower=1,
            upper=1,
            inverse="network_asset_deployment",
            aggregation="none",
        )
    )

    _cim_meta = ClassMeta(
        cim_name="AssetDeployment",
        package="TC57CIM/IEC61968/Assets",
        guid="{D5998006-5A79-4d0d-8E31-D6F88DD4C413}",
        attributes=(
            AttrMeta(
                "deployment_state", "deploymentState", "DeploymentStateKind", 0, 1, "enumeration"
            ),
            AttrMeta("deployment_date", "deploymentDate", "DeploymentDate", 0, 1, "compound"),
            AttrMeta(
                "breaker_application",
                "breakerApplication",
                "BreakerApplicationKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta(
                "transformer_application",
                "transformerApplication",
                "TransformerApplicationKind",
                0,
                1,
                "enumeration",
            ),
            AttrMeta("likelihood_of_failure", "likelihoodOfFailure", "int", 0, 1, "primitive"),
            AttrMeta("facility_kind", "facilityKind", "FacilityKind", 0, 1, "enumeration"),
        ),
        ends=(
            asset.meta,
            base_voltage.meta,
        ),
    )

    def __init__(
        self,
        *,
        deployment_state: DeploymentStateKind | None = None,
        deployment_date: DeploymentDate | None = None,
        breaker_application: BreakerApplicationKind | None = None,
        transformer_application: TransformerApplicationKind | None = None,
        likelihood_of_failure: int | None = None,
        facility_kind: FacilityKind | None = None,
        asset: Asset | None = None,
        base_voltage: BaseVoltage | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.deployment_state = deployment_state
        self.deployment_date = deployment_date
        self.breaker_application = breaker_application
        self.transformer_application = transformer_application
        self.likelihood_of_failure = likelihood_of_failure
        self.facility_kind = facility_kind
        if asset is not None:
            self.asset = asset
        if base_voltage is not None:
            self.base_voltage = base_voltage

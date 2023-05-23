import datetime
import typing

import kubernetes.client

class V1PodFailurePolicyRule:
    action: str
    on_exit_codes: typing.Optional[
        kubernetes.client.V1PodFailurePolicyOnExitCodesRequirement
    ]
    on_pod_conditions: list[kubernetes.client.V1PodFailurePolicyOnPodConditionsPattern]
    def __init__(
        self,
        *,
        action: str,
        on_exit_codes: typing.Optional[
            kubernetes.client.V1PodFailurePolicyOnExitCodesRequirement
        ] = ...,
        on_pod_conditions: list[
            kubernetes.client.V1PodFailurePolicyOnPodConditionsPattern
        ]
    ) -> None: ...
    def to_dict(self) -> V1PodFailurePolicyRuleDict: ...

class V1PodFailurePolicyRuleDict(typing.TypedDict, total=False):
    action: str
    onExitCodes: typing.Optional[
        kubernetes.client.V1PodFailurePolicyOnExitCodesRequirementDict
    ]
    onPodConditions: list[
        kubernetes.client.V1PodFailurePolicyOnPodConditionsPatternDict
    ]

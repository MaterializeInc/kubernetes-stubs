import datetime
import typing

import kubernetes.client

class V2HorizontalPodAutoscalerBehavior:
    scale_down: typing.Optional[kubernetes.client.V2HPAScalingRules]
    scale_up: typing.Optional[kubernetes.client.V2HPAScalingRules]
    def __init__(
        self,
        *,
        scale_down: typing.Optional[kubernetes.client.V2HPAScalingRules] = ...,
        scale_up: typing.Optional[kubernetes.client.V2HPAScalingRules] = ...
    ) -> None: ...
    def to_dict(self) -> V2HorizontalPodAutoscalerBehaviorDict: ...

class V2HorizontalPodAutoscalerBehaviorDict(typing.TypedDict, total=False):
    scaleDown: typing.Optional[kubernetes.client.V2HPAScalingRulesDict]
    scaleUp: typing.Optional[kubernetes.client.V2HPAScalingRulesDict]

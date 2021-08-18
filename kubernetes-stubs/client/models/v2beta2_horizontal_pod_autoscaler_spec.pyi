import datetime
import typing

import kubernetes.client

class V2beta2HorizontalPodAutoscalerSpec:
    behavior: typing.Optional[kubernetes.client.V2beta2HorizontalPodAutoscalerBehavior]
    max_replicas: int
    metrics: typing.Optional[list[kubernetes.client.V2beta2MetricSpec]]
    min_replicas: typing.Optional[int]
    scale_target_ref: kubernetes.client.V2beta2CrossVersionObjectReference
    def __init__(
        self,
        *,
        behavior: typing.Optional[
            kubernetes.client.V2beta2HorizontalPodAutoscalerBehavior
        ] = ...,
        max_replicas: int,
        metrics: typing.Optional[list[kubernetes.client.V2beta2MetricSpec]] = ...,
        min_replicas: typing.Optional[int] = ...,
        scale_target_ref: kubernetes.client.V2beta2CrossVersionObjectReference
    ) -> None: ...

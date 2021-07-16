import datetime
import typing

import kubernetes.client

class V2beta2HorizontalPodAutoscalerStatus:
    conditions: list[kubernetes.client.V2beta2HorizontalPodAutoscalerCondition]
    current_metrics: typing.Optional[list[kubernetes.client.V2beta2MetricStatus]]
    current_replicas: int
    desired_replicas: int
    last_scale_time: typing.Optional[datetime.datetime]
    observed_generation: typing.Optional[int]
    def __init__(
        self,
        *,
        conditions: list[kubernetes.client.V2beta2HorizontalPodAutoscalerCondition],
        current_metrics: typing.Optional[
            list[kubernetes.client.V2beta2MetricStatus]
        ] = ...,
        current_replicas: int,
        desired_replicas: int,
        last_scale_time: typing.Optional[datetime.datetime] = ...,
        observed_generation: typing.Optional[int] = ...
    ) -> None: ...

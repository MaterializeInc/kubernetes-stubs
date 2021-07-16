import datetime
import typing

import kubernetes.client

class V1HorizontalPodAutoscalerStatus:
    current_cpu_utilization_percentage: typing.Optional[int]
    current_replicas: int
    desired_replicas: int
    last_scale_time: typing.Optional[datetime.datetime]
    observed_generation: typing.Optional[int]
    def __init__(
        self,
        *,
        current_cpu_utilization_percentage: typing.Optional[int] = ...,
        current_replicas: int,
        desired_replicas: int,
        last_scale_time: typing.Optional[datetime.datetime] = ...,
        observed_generation: typing.Optional[int] = ...
    ) -> None: ...

import datetime
import typing

import kubernetes.client

class V2beta2HPAScalingRules:
    policies: typing.Optional[list[kubernetes.client.V2beta2HPAScalingPolicy]]
    select_policy: typing.Optional[str]
    stabilization_window_seconds: typing.Optional[int]
    def __init__(
        self,
        *,
        policies: typing.Optional[
            list[kubernetes.client.V2beta2HPAScalingPolicy]
        ] = ...,
        select_policy: typing.Optional[str] = ...,
        stabilization_window_seconds: typing.Optional[int] = ...
    ) -> None: ...

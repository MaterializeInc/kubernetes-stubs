import datetime
import typing

import kubernetes.client

class V1DaemonSetStatus:
    collision_count: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes.client.V1DaemonSetCondition]]
    current_number_scheduled: int
    desired_number_scheduled: int
    number_available: typing.Optional[int]
    number_misscheduled: int
    number_ready: int
    number_unavailable: typing.Optional[int]
    observed_generation: typing.Optional[int]
    updated_number_scheduled: typing.Optional[int]
    def __init__(
        self,
        *,
        collision_count: typing.Optional[int] = ...,
        conditions: typing.Optional[list[kubernetes.client.V1DaemonSetCondition]] = ...,
        current_number_scheduled: int,
        desired_number_scheduled: int,
        number_available: typing.Optional[int] = ...,
        number_misscheduled: int,
        number_ready: int,
        number_unavailable: typing.Optional[int] = ...,
        observed_generation: typing.Optional[int] = ...,
        updated_number_scheduled: typing.Optional[int] = ...
    ) -> None: ...

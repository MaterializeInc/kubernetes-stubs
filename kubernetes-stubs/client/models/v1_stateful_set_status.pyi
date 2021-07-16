import datetime
import typing

import kubernetes.client

class V1StatefulSetStatus:
    collision_count: typing.Optional[int]
    conditions: typing.Optional[list[kubernetes.client.V1StatefulSetCondition]]
    current_replicas: typing.Optional[int]
    current_revision: typing.Optional[str]
    observed_generation: typing.Optional[int]
    ready_replicas: typing.Optional[int]
    replicas: int
    update_revision: typing.Optional[str]
    updated_replicas: typing.Optional[int]
    def __init__(
        self,
        *,
        collision_count: typing.Optional[int] = ...,
        conditions: typing.Optional[
            list[kubernetes.client.V1StatefulSetCondition]
        ] = ...,
        current_replicas: typing.Optional[int] = ...,
        current_revision: typing.Optional[str] = ...,
        observed_generation: typing.Optional[int] = ...,
        ready_replicas: typing.Optional[int] = ...,
        replicas: int,
        update_revision: typing.Optional[str] = ...,
        updated_replicas: typing.Optional[int] = ...
    ) -> None: ...

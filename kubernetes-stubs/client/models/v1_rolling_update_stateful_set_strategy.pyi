import datetime
import typing

import kubernetes.client

class V1RollingUpdateStatefulSetStrategy:
    max_unavailable: typing.Optional[typing.Any]
    partition: typing.Optional[int]
    def __init__(
        self,
        *,
        max_unavailable: typing.Optional[typing.Any] = ...,
        partition: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1RollingUpdateStatefulSetStrategyDict: ...

class V1RollingUpdateStatefulSetStrategyDict(typing.TypedDict, total=False):
    maxUnavailable: typing.Optional[typing.Any]
    partition: typing.Optional[int]

import datetime
import typing

import kubernetes.client

class V1beta2QueuingConfiguration:
    hand_size: typing.Optional[int]
    queue_length_limit: typing.Optional[int]
    queues: typing.Optional[int]
    def __init__(
        self,
        *,
        hand_size: typing.Optional[int] = ...,
        queue_length_limit: typing.Optional[int] = ...,
        queues: typing.Optional[int] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta2QueuingConfigurationDict: ...

class V1beta2QueuingConfigurationDict(typing.TypedDict, total=False):
    handSize: typing.Optional[int]
    queueLengthLimit: typing.Optional[int]
    queues: typing.Optional[int]

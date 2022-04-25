import datetime
import typing

import kubernetes.client

class V1beta2LimitResponse:
    queuing: typing.Optional[kubernetes.client.V1beta2QueuingConfiguration]
    type: str
    def __init__(
        self,
        *,
        queuing: typing.Optional[kubernetes.client.V1beta2QueuingConfiguration] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V1beta2LimitResponseDict: ...

class V1beta2LimitResponseDict(typing.TypedDict, total=False):
    queuing: typing.Optional[kubernetes.client.V1beta2QueuingConfigurationDict]
    type: str

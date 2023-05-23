import datetime
import typing

import kubernetes.client

class V1beta3LimitResponse:
    queuing: typing.Optional[kubernetes.client.V1beta3QueuingConfiguration]
    type: str
    def __init__(
        self,
        *,
        queuing: typing.Optional[kubernetes.client.V1beta3QueuingConfiguration] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V1beta3LimitResponseDict: ...

class V1beta3LimitResponseDict(typing.TypedDict, total=False):
    queuing: typing.Optional[kubernetes.client.V1beta3QueuingConfigurationDict]
    type: str

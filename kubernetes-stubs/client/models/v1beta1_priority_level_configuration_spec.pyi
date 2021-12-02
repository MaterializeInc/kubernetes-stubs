import datetime
import typing

import kubernetes.client

class V1beta1PriorityLevelConfigurationSpec:
    limited: typing.Optional[kubernetes.client.V1beta1LimitedPriorityLevelConfiguration]
    type: str
    def __init__(
        self,
        *,
        limited: typing.Optional[
            kubernetes.client.V1beta1LimitedPriorityLevelConfiguration
        ] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V1beta1PriorityLevelConfigurationSpecDict: ...

class V1beta1PriorityLevelConfigurationSpecDict(typing.TypedDict, total=False):
    limited: typing.Optional[
        kubernetes.client.V1beta1LimitedPriorityLevelConfigurationDict
    ]
    type: str

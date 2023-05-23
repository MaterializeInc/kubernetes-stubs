import datetime
import typing

import kubernetes.client

class V1beta3PriorityLevelConfigurationSpec:
    limited: typing.Optional[kubernetes.client.V1beta3LimitedPriorityLevelConfiguration]
    type: str
    def __init__(
        self,
        *,
        limited: typing.Optional[
            kubernetes.client.V1beta3LimitedPriorityLevelConfiguration
        ] = ...,
        type: str
    ) -> None: ...
    def to_dict(self) -> V1beta3PriorityLevelConfigurationSpecDict: ...

class V1beta3PriorityLevelConfigurationSpecDict(typing.TypedDict, total=False):
    limited: typing.Optional[
        kubernetes.client.V1beta3LimitedPriorityLevelConfigurationDict
    ]
    type: str

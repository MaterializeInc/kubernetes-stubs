import datetime
import typing

import kubernetes.client

class V1beta2PriorityLevelConfigurationStatus:
    conditions: typing.Optional[
        list[kubernetes.client.V1beta2PriorityLevelConfigurationCondition]
    ]
    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes.client.V1beta2PriorityLevelConfigurationCondition]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta2PriorityLevelConfigurationStatusDict: ...

class V1beta2PriorityLevelConfigurationStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[
        list[kubernetes.client.V1beta2PriorityLevelConfigurationConditionDict]
    ]

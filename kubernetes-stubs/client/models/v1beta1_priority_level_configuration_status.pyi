import datetime
import typing

import kubernetes.client

class V1beta1PriorityLevelConfigurationStatus:
    conditions: typing.Optional[
        list[kubernetes.client.V1beta1PriorityLevelConfigurationCondition]
    ]
    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes.client.V1beta1PriorityLevelConfigurationCondition]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta1PriorityLevelConfigurationStatusDict: ...

class V1beta1PriorityLevelConfigurationStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[
        list[kubernetes.client.V1beta1PriorityLevelConfigurationConditionDict]
    ]

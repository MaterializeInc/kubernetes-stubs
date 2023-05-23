import datetime
import typing

import kubernetes.client

class V1beta3PriorityLevelConfigurationStatus:
    conditions: typing.Optional[
        list[kubernetes.client.V1beta3PriorityLevelConfigurationCondition]
    ]
    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes.client.V1beta3PriorityLevelConfigurationCondition]
        ] = ...
    ) -> None: ...
    def to_dict(self) -> V1beta3PriorityLevelConfigurationStatusDict: ...

class V1beta3PriorityLevelConfigurationStatusDict(typing.TypedDict, total=False):
    conditions: typing.Optional[
        list[kubernetes.client.V1beta3PriorityLevelConfigurationConditionDict]
    ]

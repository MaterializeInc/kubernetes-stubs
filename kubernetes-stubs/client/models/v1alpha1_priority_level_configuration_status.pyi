import datetime
import typing

import kubernetes.client

class V1alpha1PriorityLevelConfigurationStatus:
    conditions: typing.Optional[
        list[kubernetes.client.V1alpha1PriorityLevelConfigurationCondition]
    ]
    def __init__(
        self,
        *,
        conditions: typing.Optional[
            list[kubernetes.client.V1alpha1PriorityLevelConfigurationCondition]
        ] = ...
    ) -> None: ...

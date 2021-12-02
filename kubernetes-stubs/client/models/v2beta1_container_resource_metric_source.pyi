import datetime
import typing

import kubernetes.client

class V2beta1ContainerResourceMetricSource:
    container: str
    name: str
    target_average_utilization: typing.Optional[int]
    target_average_value: typing.Optional[str]
    def __init__(
        self,
        *,
        container: str,
        name: str,
        target_average_utilization: typing.Optional[int] = ...,
        target_average_value: typing.Optional[str] = ...
    ) -> None: ...
    def to_dict(self) -> V2beta1ContainerResourceMetricSourceDict: ...

class V2beta1ContainerResourceMetricSourceDict(typing.TypedDict, total=False):
    container: str
    name: str
    targetAverageUtilization: typing.Optional[int]
    targetAverageValue: typing.Optional[str]

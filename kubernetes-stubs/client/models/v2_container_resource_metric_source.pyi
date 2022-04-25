import datetime
import typing

import kubernetes.client

class V2ContainerResourceMetricSource:
    container: str
    name: str
    target: kubernetes.client.V2MetricTarget
    def __init__(
        self, *, container: str, name: str, target: kubernetes.client.V2MetricTarget
    ) -> None: ...
    def to_dict(self) -> V2ContainerResourceMetricSourceDict: ...

class V2ContainerResourceMetricSourceDict(typing.TypedDict, total=False):
    container: str
    name: str
    target: kubernetes.client.V2MetricTargetDict

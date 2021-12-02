import datetime
import typing

import kubernetes.client

class V2beta2ContainerResourceMetricSource:
    container: str
    name: str
    target: kubernetes.client.V2beta2MetricTarget
    def __init__(
        self,
        *,
        container: str,
        name: str,
        target: kubernetes.client.V2beta2MetricTarget
    ) -> None: ...
    def to_dict(self) -> V2beta2ContainerResourceMetricSourceDict: ...

class V2beta2ContainerResourceMetricSourceDict(typing.TypedDict, total=False):
    container: str
    name: str
    target: kubernetes.client.V2beta2MetricTargetDict

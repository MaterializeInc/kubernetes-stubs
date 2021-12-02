import datetime
import typing

import kubernetes.client

class V2beta2ContainerResourceMetricStatus:
    container: str
    current: kubernetes.client.V2beta2MetricValueStatus
    name: str
    def __init__(
        self,
        *,
        container: str,
        current: kubernetes.client.V2beta2MetricValueStatus,
        name: str
    ) -> None: ...
    def to_dict(self) -> V2beta2ContainerResourceMetricStatusDict: ...

class V2beta2ContainerResourceMetricStatusDict(typing.TypedDict, total=False):
    container: str
    current: kubernetes.client.V2beta2MetricValueStatusDict
    name: str

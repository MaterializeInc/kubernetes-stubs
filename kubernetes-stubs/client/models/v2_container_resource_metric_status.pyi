import datetime
import typing

import kubernetes.client

class V2ContainerResourceMetricStatus:
    container: str
    current: kubernetes.client.V2MetricValueStatus
    name: str
    def __init__(
        self,
        *,
        container: str,
        current: kubernetes.client.V2MetricValueStatus,
        name: str
    ) -> None: ...
    def to_dict(self) -> V2ContainerResourceMetricStatusDict: ...

class V2ContainerResourceMetricStatusDict(typing.TypedDict, total=False):
    container: str
    current: kubernetes.client.V2MetricValueStatusDict
    name: str

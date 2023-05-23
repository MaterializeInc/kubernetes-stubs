import datetime
import typing

import kubernetes.client

class V2ResourceMetricStatus:
    current: kubernetes.client.V2MetricValueStatus
    name: str
    def __init__(
        self, *, current: kubernetes.client.V2MetricValueStatus, name: str
    ) -> None: ...
    def to_dict(self) -> V2ResourceMetricStatusDict: ...

class V2ResourceMetricStatusDict(typing.TypedDict, total=False):
    current: kubernetes.client.V2MetricValueStatusDict
    name: str

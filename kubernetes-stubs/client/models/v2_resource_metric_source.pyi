import datetime
import typing

import kubernetes.client

class V2ResourceMetricSource:
    name: str
    target: kubernetes.client.V2MetricTarget
    def __init__(
        self, *, name: str, target: kubernetes.client.V2MetricTarget
    ) -> None: ...
    def to_dict(self) -> V2ResourceMetricSourceDict: ...

class V2ResourceMetricSourceDict(typing.TypedDict, total=False):
    name: str
    target: kubernetes.client.V2MetricTargetDict

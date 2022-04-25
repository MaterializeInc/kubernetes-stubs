import datetime
import typing

import kubernetes.client

class V2ExternalMetricSource:
    metric: kubernetes.client.V2MetricIdentifier
    target: kubernetes.client.V2MetricTarget
    def __init__(
        self,
        *,
        metric: kubernetes.client.V2MetricIdentifier,
        target: kubernetes.client.V2MetricTarget
    ) -> None: ...
    def to_dict(self) -> V2ExternalMetricSourceDict: ...

class V2ExternalMetricSourceDict(typing.TypedDict, total=False):
    metric: kubernetes.client.V2MetricIdentifierDict
    target: kubernetes.client.V2MetricTargetDict

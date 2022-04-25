import datetime
import typing

import kubernetes.client

class V2ExternalMetricStatus:
    current: kubernetes.client.V2MetricValueStatus
    metric: kubernetes.client.V2MetricIdentifier
    def __init__(
        self,
        *,
        current: kubernetes.client.V2MetricValueStatus,
        metric: kubernetes.client.V2MetricIdentifier
    ) -> None: ...
    def to_dict(self) -> V2ExternalMetricStatusDict: ...

class V2ExternalMetricStatusDict(typing.TypedDict, total=False):
    current: kubernetes.client.V2MetricValueStatusDict
    metric: kubernetes.client.V2MetricIdentifierDict

import datetime
import typing

import kubernetes.client

class V2ObjectMetricStatus:
    current: kubernetes.client.V2MetricValueStatus
    described_object: kubernetes.client.V2CrossVersionObjectReference
    metric: kubernetes.client.V2MetricIdentifier
    def __init__(
        self,
        *,
        current: kubernetes.client.V2MetricValueStatus,
        described_object: kubernetes.client.V2CrossVersionObjectReference,
        metric: kubernetes.client.V2MetricIdentifier
    ) -> None: ...
    def to_dict(self) -> V2ObjectMetricStatusDict: ...

class V2ObjectMetricStatusDict(typing.TypedDict, total=False):
    current: kubernetes.client.V2MetricValueStatusDict
    describedObject: kubernetes.client.V2CrossVersionObjectReferenceDict
    metric: kubernetes.client.V2MetricIdentifierDict

import datetime
import typing

import kubernetes.client

class V2ObjectMetricSource:
    described_object: kubernetes.client.V2CrossVersionObjectReference
    metric: kubernetes.client.V2MetricIdentifier
    target: kubernetes.client.V2MetricTarget
    def __init__(
        self,
        *,
        described_object: kubernetes.client.V2CrossVersionObjectReference,
        metric: kubernetes.client.V2MetricIdentifier,
        target: kubernetes.client.V2MetricTarget
    ) -> None: ...
    def to_dict(self) -> V2ObjectMetricSourceDict: ...

class V2ObjectMetricSourceDict(typing.TypedDict, total=False):
    describedObject: kubernetes.client.V2CrossVersionObjectReferenceDict
    metric: kubernetes.client.V2MetricIdentifierDict
    target: kubernetes.client.V2MetricTargetDict

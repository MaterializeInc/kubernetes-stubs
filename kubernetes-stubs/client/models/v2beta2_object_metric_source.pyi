import datetime
import typing

import kubernetes.client

class V2beta2ObjectMetricSource:
    described_object: kubernetes.client.V2beta2CrossVersionObjectReference
    metric: kubernetes.client.V2beta2MetricIdentifier
    target: kubernetes.client.V2beta2MetricTarget
    def __init__(
        self,
        *,
        described_object: kubernetes.client.V2beta2CrossVersionObjectReference,
        metric: kubernetes.client.V2beta2MetricIdentifier,
        target: kubernetes.client.V2beta2MetricTarget
    ) -> None: ...

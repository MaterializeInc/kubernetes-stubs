import datetime
import typing

import kubernetes.client

class V2beta2ObjectMetricStatus:
    current: kubernetes.client.V2beta2MetricValueStatus
    described_object: kubernetes.client.V2beta2CrossVersionObjectReference
    metric: kubernetes.client.V2beta2MetricIdentifier
    def __init__(
        self,
        *,
        current: kubernetes.client.V2beta2MetricValueStatus,
        described_object: kubernetes.client.V2beta2CrossVersionObjectReference,
        metric: kubernetes.client.V2beta2MetricIdentifier
    ) -> None: ...

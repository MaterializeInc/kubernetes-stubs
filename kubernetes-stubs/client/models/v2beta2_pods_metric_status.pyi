import datetime
import typing

import kubernetes.client

class V2beta2PodsMetricStatus:
    current: kubernetes.client.V2beta2MetricValueStatus
    metric: kubernetes.client.V2beta2MetricIdentifier
    def __init__(
        self,
        *,
        current: kubernetes.client.V2beta2MetricValueStatus,
        metric: kubernetes.client.V2beta2MetricIdentifier
    ) -> None: ...

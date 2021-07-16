import datetime
import typing

import kubernetes.client

class V2beta2PodsMetricSource:
    metric: kubernetes.client.V2beta2MetricIdentifier
    target: kubernetes.client.V2beta2MetricTarget
    def __init__(
        self,
        *,
        metric: kubernetes.client.V2beta2MetricIdentifier,
        target: kubernetes.client.V2beta2MetricTarget
    ) -> None: ...

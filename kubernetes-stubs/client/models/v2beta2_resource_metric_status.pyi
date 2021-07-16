import datetime
import typing

import kubernetes.client

class V2beta2ResourceMetricStatus:
    current: kubernetes.client.V2beta2MetricValueStatus
    name: str
    def __init__(
        self, *, current: kubernetes.client.V2beta2MetricValueStatus, name: str
    ) -> None: ...

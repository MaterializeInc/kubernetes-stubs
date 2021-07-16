import datetime
import typing

import kubernetes.client

class V2beta1PodsMetricStatus:
    current_average_value: str
    metric_name: str
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    def __init__(
        self,
        *,
        current_average_value: str,
        metric_name: str,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...
    ) -> None: ...

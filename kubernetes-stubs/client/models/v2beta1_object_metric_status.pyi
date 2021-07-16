import datetime
import typing

import kubernetes.client

class V2beta1ObjectMetricStatus:
    average_value: typing.Optional[str]
    current_value: str
    metric_name: str
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    target: kubernetes.client.V2beta1CrossVersionObjectReference
    def __init__(
        self,
        *,
        average_value: typing.Optional[str] = ...,
        current_value: str,
        metric_name: str,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        target: kubernetes.client.V2beta1CrossVersionObjectReference
    ) -> None: ...

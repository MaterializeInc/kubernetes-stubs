import datetime
import typing

import kubernetes.client

class V2beta1ObjectMetricSource:
    average_value: typing.Optional[str]
    metric_name: str
    selector: typing.Optional[kubernetes.client.V1LabelSelector]
    target: kubernetes.client.V2beta1CrossVersionObjectReference
    target_value: str
    def __init__(
        self,
        *,
        average_value: typing.Optional[str] = ...,
        metric_name: str,
        selector: typing.Optional[kubernetes.client.V1LabelSelector] = ...,
        target: kubernetes.client.V2beta1CrossVersionObjectReference,
        target_value: str
    ) -> None: ...

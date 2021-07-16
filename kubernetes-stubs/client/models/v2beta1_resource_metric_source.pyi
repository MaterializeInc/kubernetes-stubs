import datetime
import typing

import kubernetes.client

class V2beta1ResourceMetricSource:
    name: str
    target_average_utilization: typing.Optional[int]
    target_average_value: typing.Optional[str]
    def __init__(
        self,
        *,
        name: str,
        target_average_utilization: typing.Optional[int] = ...,
        target_average_value: typing.Optional[str] = ...
    ) -> None: ...

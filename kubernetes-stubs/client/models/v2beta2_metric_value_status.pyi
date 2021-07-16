import datetime
import typing

import kubernetes.client

class V2beta2MetricValueStatus:
    average_utilization: typing.Optional[int]
    average_value: typing.Optional[str]
    value: typing.Optional[str]
    def __init__(
        self,
        *,
        average_utilization: typing.Optional[int] = ...,
        average_value: typing.Optional[str] = ...,
        value: typing.Optional[str] = ...
    ) -> None: ...

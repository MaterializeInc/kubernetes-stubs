import datetime
import typing

import kubernetes.client

class V2beta1ResourceMetricStatus:
    current_average_utilization: typing.Optional[int]
    current_average_value: str
    name: str
    def __init__(
        self,
        *,
        current_average_utilization: typing.Optional[int] = ...,
        current_average_value: str,
        name: str
    ) -> None: ...

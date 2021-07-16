import datetime
import typing

import kubernetes.client

class V1EventSeries:
    count: typing.Optional[int]
    last_observed_time: typing.Optional[datetime.datetime]
    state: typing.Optional[str]
    def __init__(
        self,
        *,
        count: typing.Optional[int] = ...,
        last_observed_time: typing.Optional[datetime.datetime] = ...,
        state: typing.Optional[str] = ...
    ) -> None: ...

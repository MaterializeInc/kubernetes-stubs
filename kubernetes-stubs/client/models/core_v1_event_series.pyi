import datetime
import typing

import kubernetes.client

class CoreV1EventSeries:
    count: typing.Optional[int]
    last_observed_time: typing.Optional[datetime.datetime]
    def __init__(
        self,
        *,
        count: typing.Optional[int] = ...,
        last_observed_time: typing.Optional[datetime.datetime] = ...
    ) -> None: ...
    def to_dict(self) -> CoreV1EventSeriesDict: ...

class CoreV1EventSeriesDict(typing.TypedDict, total=False):
    count: typing.Optional[int]
    lastObservedTime: typing.Optional[datetime.datetime]

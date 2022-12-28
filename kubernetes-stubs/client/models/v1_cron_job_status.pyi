import datetime
import typing

import kubernetes.client

class V1CronJobStatus:
    active: typing.Optional[list[kubernetes.client.V1ObjectReference]]
    last_schedule_time: typing.Optional[datetime.datetime]
    last_successful_time: typing.Optional[datetime.datetime]

    def __init__(
        self,
        *,
        active: typing.Optional[list[kubernetes.client.V1ObjectReference]] = ...,
        last_schedule_time: typing.Optional[datetime.datetime] = ...,
        last_successful_time: typing.Optional[datetime.datetime] = ...
    ) -> None: ...
    def to_dict(self) -> V1CronJobStatusDict: ...

class V1CronJobStatusDict(typing.TypedDict, total=False):
    active: typing.Optional[list[kubernetes.client.V1ObjectReferenceDict]]
    lastScheduleTime: typing.Optional[datetime.datetime]
    lastSuccessfulTime: typing.Optional[datetime.datetime]
